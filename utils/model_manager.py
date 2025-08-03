#!/usr/bin/env python3
"""
Model Manager - RSC03 OpenHands Multi-Agent System
Centralized management for multi-model API distribution and optimization
"""

import os
import json
import time
import logging
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum

class ModelProvider(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    DEEPSEEK = "deepseek"

class CostTier(Enum):
    PREMIUM = "premium"
    BALANCED = "balanced"
    EFFICIENT = "efficient"

@dataclass
class ModelUsage:
    """Track model usage statistics"""
    requests: int = 0
    tokens_input: int = 0
    tokens_output: int = 0
    cost: float = 0.0
    errors: int = 0
    avg_response_time: float = 0.0
    last_used: Optional[datetime] = None

@dataclass
class ModelConfig:
    """Model configuration details"""
    name: str
    provider: ModelProvider
    endpoint: str
    max_tokens: int
    temperature: float
    cost_per_1k_input: float
    cost_per_1k_output: float
    rate_limit_rpm: int
    rate_limit_tpm: int
    capabilities: List[str]

class ModelManager:
    """
    Centralized model management for RSC03 multi-agent system
    
    Features:
    - Multi-model API management
    - Cost optimization and tracking
    - Fallback and retry logic
    - Performance monitoring
    - Rate limit management
    """
    
    def __init__(self, config_path: str = None):
        self.config_path = config_path or "/home/ubuntu/environment/workbench/rsc03/configs/model_config.json"
        self.config = self._load_config()
        self.usage_stats = {}
        self.rate_limits = {}
        self.logger = self._setup_logging()
        
        # Initialize usage tracking for all models
        for model_name in self.config["model_configurations"].keys():
            self.usage_stats[model_name] = ModelUsage()
            self.rate_limits[model_name] = {
                "requests": [],
                "tokens": []
            }
    
    def _load_config(self) -> Dict[str, Any]:
        """Load model configuration from JSON file"""
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            self.logger.error(f"Model config file not found: {self.config_path}")
            return self._get_default_config()
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON in config file: {e}")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Return default configuration if config file is not available"""
        return {
            "model_assignments": {},
            "model_configurations": {},
            "fallback_strategy": {"enabled": False},
            "monitoring": {"enabled": True}
        }
    
    def _setup_logging(self) -> logging.Logger:
        """Setup logging for model manager"""
        logger = logging.getLogger("ModelManager")
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def get_model_for_agent(self, agent_id: str) -> Tuple[str, Dict[str, Any]]:
        """
        Get the appropriate model for a specific agent
        
        Args:
            agent_id: Agent identifier
            
        Returns:
            Tuple of (model_name, model_config)
        """
        if agent_id not in self.config["model_assignments"]:
            self.logger.warning(f"No model assignment found for agent: {agent_id}")
            return "gpt-3.5-turbo", self.config["model_configurations"].get("gpt-3.5-turbo", {})
        
        assignment = self.config["model_assignments"][agent_id]
        primary_model = assignment["primary_model"]
        
        # Check if primary model is available
        if self._is_model_available(primary_model):
            model_config = self.config["model_configurations"][primary_model]
            return primary_model, model_config
        
        # Try fallback model
        fallback_model = assignment.get("fallback_model")
        if fallback_model and self._is_model_available(fallback_model):
            self.logger.info(f"Using fallback model {fallback_model} for agent {agent_id}")
            model_config = self.config["model_configurations"][fallback_model]
            return fallback_model, model_config
        
        # Use system-wide fallback
        return self._get_system_fallback()
    
    def _is_model_available(self, model_name: str) -> bool:
        """
        Check if a model is available (not rate limited, has API key, etc.)
        
        Args:
            model_name: Name of the model to check
            
        Returns:
            True if model is available, False otherwise
        """
        if model_name not in self.config["model_configurations"]:
            return False
        
        model_config = self.config["model_configurations"][model_name]
        provider = model_config["provider"]
        
        # Check API key availability
        api_key = self._get_api_key(provider)
        if not api_key:
            self.logger.warning(f"No API key found for provider: {provider}")
            return False
        
        # Check rate limits
        if self._is_rate_limited(model_name):
            self.logger.warning(f"Model {model_name} is rate limited")
            return False
        
        return True
    
    def _get_api_key(self, provider: str) -> Optional[str]:
        """Get API key for a specific provider"""
        key_mapping = {
            "openai": "OPENAI_API_KEY",
            "anthropic": "ANTHROPIC_API_KEY",
            "google": "GEMINI_API_KEY",
            "deepseek": "DEEPSEEK_API_KEY"
        }
        
        env_var = key_mapping.get(provider)
        if env_var:
            return os.getenv(env_var)
        
        return None
    
    def _is_rate_limited(self, model_name: str) -> bool:
        """
        Check if model is currently rate limited
        
        Args:
            model_name: Name of the model to check
            
        Returns:
            True if rate limited, False otherwise
        """
        if model_name not in self.rate_limits:
            return False
        
        model_config = self.config["model_configurations"][model_name]
        current_time = time.time()
        
        # Clean old entries (older than 1 minute)
        cutoff_time = current_time - 60
        
        rate_limit_data = self.rate_limits[model_name]
        rate_limit_data["requests"] = [
            req_time for req_time in rate_limit_data["requests"] 
            if req_time > cutoff_time
        ]
        
        # Check request rate limit
        if len(rate_limit_data["requests"]) >= model_config["rate_limits"]["requests_per_minute"]:
            return True
        
        return False
    
    def _get_system_fallback(self) -> Tuple[str, Dict[str, Any]]:
        """Get system-wide fallback model"""
        fallback_model = "gpt-3.5-turbo"  # Most reliable fallback
        model_config = self.config["model_configurations"].get(
            fallback_model, 
            {"provider": "openai", "max_tokens": 4096}
        )
        return fallback_model, model_config
    
    def record_usage(self, model_name: str, input_tokens: int, output_tokens: int, 
                    response_time: float, success: bool = True) -> None:
        """
        Record model usage statistics
        
        Args:
            model_name: Name of the model used
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
            response_time: Response time in seconds
            success: Whether the request was successful
        """
        if model_name not in self.usage_stats:
            self.usage_stats[model_name] = ModelUsage()
        
        stats = self.usage_stats[model_name]
        stats.requests += 1
        stats.tokens_input += input_tokens
        stats.tokens_output += output_tokens
        stats.last_used = datetime.now()
        
        # Calculate cost
        if model_name in self.config["model_configurations"]:
            model_config = self.config["model_configurations"][model_name]
            input_cost = (input_tokens / 1000) * model_config["cost_per_1k_tokens"]["input"]
            output_cost = (output_tokens / 1000) * model_config["cost_per_1k_tokens"]["output"]
            stats.cost += input_cost + output_cost
        
        # Update average response time
        if stats.requests > 1:
            stats.avg_response_time = (
                (stats.avg_response_time * (stats.requests - 1) + response_time) / stats.requests
            )
        else:
            stats.avg_response_time = response_time
        
        if not success:
            stats.errors += 1
        
        # Record for rate limiting
        current_time = time.time()
        if model_name in self.rate_limits:
            self.rate_limits[model_name]["requests"].append(current_time)
    
    def get_usage_summary(self, agent_id: str = None) -> Dict[str, Any]:
        """
        Get usage summary for all models or specific agent
        
        Args:
            agent_id: Optional agent ID to filter by
            
        Returns:
            Usage summary dictionary
        """
        summary = {
            "total_requests": 0,
            "total_cost": 0.0,
            "total_tokens": 0,
            "models": {}
        }
        
        for model_name, stats in self.usage_stats.items():
            # Filter by agent if specified
            if agent_id:
                agent_assignment = self.config["model_assignments"].get(agent_id, {})
                if model_name not in [agent_assignment.get("primary_model"), 
                                    agent_assignment.get("fallback_model")]:
                    continue
            
            model_summary = {
                "requests": stats.requests,
                "tokens_input": stats.tokens_input,
                "tokens_output": stats.tokens_output,
                "total_tokens": stats.tokens_input + stats.tokens_output,
                "cost": round(stats.cost, 4),
                "errors": stats.errors,
                "error_rate": round(stats.errors / max(stats.requests, 1), 3),
                "avg_response_time": round(stats.avg_response_time, 2),
                "last_used": stats.last_used.isoformat() if stats.last_used else None
            }
            
            summary["models"][model_name] = model_summary
            summary["total_requests"] += stats.requests
            summary["total_cost"] += stats.cost
            summary["total_tokens"] += stats.tokens_input + stats.tokens_output
        
        summary["total_cost"] = round(summary["total_cost"], 4)
        
        return summary
    
    def get_cost_breakdown(self) -> Dict[str, Any]:
        """Get detailed cost breakdown by tier and agent"""
        breakdown = {
            "by_tier": {tier: 0.0 for tier in ["premium", "balanced", "efficient"]},
            "by_agent": {},
            "by_model": {},
            "total": 0.0
        }
        
        # Calculate costs by model
        for model_name, stats in self.usage_stats.items():
            breakdown["by_model"][model_name] = round(stats.cost, 4)
            breakdown["total"] += stats.cost
        
        # Calculate costs by tier
        for tier_name, tier_config in self.config["cost_tiers"].items():
            tier_cost = sum(
                self.usage_stats[model].cost 
                for model in tier_config["models"] 
                if model in self.usage_stats
            )
            breakdown["by_tier"][tier_name] = round(tier_cost, 4)
        
        # Calculate costs by agent
        for agent_id, assignment in self.config["model_assignments"].items():
            agent_cost = 0.0
            for model_name in [assignment["primary_model"], assignment.get("fallback_model")]:
                if model_name and model_name in self.usage_stats:
                    agent_cost += self.usage_stats[model_name].cost
            breakdown["by_agent"][agent_id] = round(agent_cost, 4)
        
        breakdown["total"] = round(breakdown["total"], 4)
        
        return breakdown

# Global model manager instance
model_manager = ModelManager()

def get_model_for_agent(agent_id: str) -> Tuple[str, Dict[str, Any]]:
    """Convenience function to get model for agent"""
    return model_manager.get_model_for_agent(agent_id)

def record_model_usage(model_name: str, input_tokens: int, output_tokens: int, 
                      response_time: float, success: bool = True) -> None:
    """Convenience function to record model usage"""
    model_manager.record_usage(model_name, input_tokens, output_tokens, response_time, success)

if __name__ == "__main__":
    # Example usage and testing
    manager = ModelManager()
    
    # Test model assignment
    model, config = manager.get_model_for_agent("project_orchestrator")
    print(f"Project Orchestrator model: {model}")
    
    # Test usage recording
    manager.record_usage("gpt-4", 100, 200, 2.5, True)
    
    # Get usage summary
    summary = manager.get_usage_summary()
    print(f"Usage summary: {json.dumps(summary, indent=2)}")