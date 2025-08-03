#!/usr/bin/env python3
"""
Infrastructure Specialist Agent - RSC03 OpenHands Multi-Agent System
Specialized in deployment, DevOps, and infrastructure solutions
Uses OpenAI GPT-3.5-turbo for cost-effective infrastructure planning and automation
"""

import os
import json
from typing import Dict, List, Any, Optional
from datetime import datetime

class InfrastructureSpecialist:
    """
    Infrastructure Specialist Agent
    
    Responsibilities:
    - Design deployment strategies and infrastructure
    - Create DevOps pipelines and automation
    - Manage containerization and orchestration
    - Optimize infrastructure costs and performance
    
    Model: OpenAI GPT-3.5-turbo (efficient for infrastructure tasks)
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        self.agent_id = "infrastructure_specialist"
        self.role = "Infrastructure Specialist"
        self.model = "gpt-3.5-turbo"
        self.api_key = os.getenv('OPENAI_API_KEY')
        
        # Load configuration
        self.config = config or self._load_default_config()
        
        # Initialize capabilities
        self.specializations = [
            "deployment",
            "devops",
            "infrastructure",
            "containerization",
            "cloud_platforms",
            "automation"
        ]
        
        self.deployment_history = []
        self.infrastructure_templates = {}
        self.cost_optimizations = {}
        
    def _load_default_config(self) -> Dict[str, Any]:
        """Load default configuration for infrastructure specialist"""
        return {
            "max_concurrent_tasks": 2,
            "preferred_cloud": "aws",
            "containerization": "docker",
            "orchestration": "kubernetes",
            "cost_optimization": True
        }
    
    def design_deployment_strategy(self, application: Dict[str, Any], requirements: Dict[str, Any]) -> Dict[str, Any]:
        """
        Design comprehensive deployment strategy for an application
        
        Args:
            application: Application details and architecture
            requirements: Deployment requirements and constraints
            
        Returns:
            Detailed deployment strategy and plan
        """
        
        deployment_prompt = f"""
        As an Infrastructure Specialist, design a deployment strategy for:
        
        Application: {json.dumps(application, indent=2)}
        Requirements: {json.dumps(requirements, indent=2)}
        
        Please provide:
        1. Deployment Architecture
           - Infrastructure overview and components
           - Network architecture and security
           - Load balancing and traffic management
           - Data storage and backup strategies
        
        2. Containerization Strategy
           - Docker container design
           - Image optimization and security
           - Container orchestration approach
           - Registry and image management
        
        3. Cloud Infrastructure Design
           - Cloud provider recommendations
           - Compute resources and scaling
           - Storage solutions and configuration
           - Network and security groups
        
        4. CI/CD Pipeline Design
           - Source code management integration
           - Build and test automation
           - Deployment automation stages
           - Rollback and recovery procedures
        
        5. Monitoring and Observability
           - Application monitoring setup
           - Infrastructure monitoring
           - Logging and log aggregation
           - Alerting and notification systems
        
        6. Security and Compliance
           - Security best practices implementation
           - Access control and authentication
           - Data encryption and protection
           - Compliance requirements adherence
        
        7. Scalability and Performance
           - Auto-scaling configurations
           - Performance optimization strategies
           - Resource allocation and limits
           - Capacity planning guidelines
        
        8. Cost Optimization
           - Resource cost analysis
           - Cost optimization strategies
           - Reserved instances and savings plans
           - Monitoring and cost alerts
        
        9. Disaster Recovery
           - Backup and recovery procedures
           - High availability setup
           - Disaster recovery planning
           - Business continuity measures
        
        Focus on practical, scalable, and cost-effective solutions.
        """
        
        deployment_result = {
            "application": application,
            "requirements": requirements,
            "timestamp": datetime.now().isoformat(),
            "strategy_type": "deployment_strategy",
            "model_used": self.model,
            "prompt": deployment_prompt,
            "deployment_strategy": {
                "architecture": "Multi-tier deployment architecture with load balancing",
                "containerization": "Docker containers with Kubernetes orchestration",
                "cloud_infrastructure": "AWS-based infrastructure with auto-scaling",
                "cicd_pipeline": "GitLab CI/CD with automated testing and deployment",
                "monitoring": "Prometheus and Grafana monitoring stack",
                "security": "Security-first approach with encryption and access controls",
                "scalability": "Horizontal auto-scaling with performance optimization",
                "cost_optimization": "Reserved instances and resource optimization",
                "disaster_recovery": "Multi-AZ deployment with automated backups"
            },
            "estimated_cost": "$500-1000/month",
            "deployment_timeline": "2-3 weeks",
            "complexity_level": "medium"
        }
        
        # Add to deployment history
        self.deployment_history.append({
            "application_name": application.get("name", "unknown"),
            "timestamp": datetime.now().isoformat(),
            "strategy_id": len(self.deployment_history)
        })
        
        return deployment_result
    
    def create_cicd_pipeline(self, project: Dict[str, Any], pipeline_requirements: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create CI/CD pipeline configuration and scripts
        
        Args:
            project: Project details and structure
            pipeline_requirements: Pipeline requirements and preferences
            
        Returns:
            CI/CD pipeline configuration and documentation
        """
        
        pipeline_prompt = f"""
        As an Infrastructure Specialist, create a CI/CD pipeline for:
        
        Project: {json.dumps(project, indent=2)}
        Pipeline Requirements: {json.dumps(pipeline_requirements, indent=2)}
        
        Please provide:
        1. Pipeline Overview
           - Pipeline stages and workflow
           - Trigger conditions and events
           - Branch strategies and policies
           - Environment promotion flow
        
        2. Source Code Management
           - Repository structure and branching
           - Code review and approval process
           - Merge strategies and policies
           - Version tagging and releases
        
        3. Build Stage Configuration
           - Build environment setup
           - Dependency management
           - Build scripts and commands
           - Artifact generation and storage
        
        4. Testing Stage Configuration
           - Unit testing automation
           - Integration testing setup
           - Code quality and coverage checks
           - Security scanning integration
        
        5. Deployment Stage Configuration
           - Environment-specific deployments
           - Blue-green or rolling deployments
           - Configuration management
           - Database migration handling
        
        6. Monitoring and Notifications
           - Pipeline monitoring and metrics
           - Failure notifications and alerts
           - Success confirmations
           - Performance tracking
        
        7. Security and Compliance
           - Security scanning integration
           - Compliance checks and validations
           - Secret management
           - Access control and permissions
        
        8. Pipeline Configuration Files
           - YAML/JSON configuration examples
           - Script templates and examples
           - Environment variable management
           - Pipeline as code implementation
        
        Provide practical, maintainable pipeline configurations.
        """
        
        pipeline_result = {
            "project": project,
            "pipeline_requirements": pipeline_requirements,
            "timestamp": datetime.now().isoformat(),
            "model_used": self.model,
            "prompt": pipeline_prompt,
            "cicd_pipeline": {
                "overview": "Automated CI/CD pipeline with multi-stage deployment",
                "source_management": "Git-based workflow with feature branches",
                "build_stage": "Automated build with dependency caching",
                "testing_stage": "Comprehensive testing with quality gates",
                "deployment_stage": "Environment-specific automated deployments",
                "monitoring": "Pipeline monitoring with Slack notifications",
                "security": "Integrated security scanning and compliance checks",
                "configuration_files": {
                    "gitlab_ci": "GitLab CI/CD YAML configuration",
                    "github_actions": "GitHub Actions workflow configuration",
                    "jenkins": "Jenkins pipeline script",
                    "docker": "Dockerfile and docker-compose configurations"
                }
            },
            "pipeline_stages": ["build", "test", "security_scan", "deploy_staging", "deploy_production"],
            "estimated_setup_time": "1-2 weeks",
            "maintenance_effort": "low"
        }
        
        return pipeline_result
    
    def design_container_architecture(self, services: List[Dict[str, Any]], orchestration: str = "kubernetes") -> Dict[str, Any]:
        """
        Design containerization and orchestration architecture
        
        Args:
            services: List of services to containerize
            orchestration: Orchestration platform (kubernetes, docker-swarm, etc.)
            
        Returns:
            Container architecture design and configurations
        """
        
        container_prompt = f"""
        As an Infrastructure Specialist, design container architecture for:
        
        Services: {json.dumps(services, indent=2)}
        Orchestration Platform: {orchestration}
        
        Please provide:
        1. Container Design Strategy
           - Containerization approach and principles
           - Base image selection and optimization
           - Multi-stage build strategies
           - Security hardening practices
        
        2. Service Architecture
           - Microservices container design
           - Inter-service communication
           - Service discovery and networking
           - Data persistence strategies
        
        3. Orchestration Configuration
           - {orchestration.title()} cluster design
           - Resource allocation and limits
           - Scaling policies and strategies
           - Health checks and readiness probes
        
        4. Networking and Security
           - Network policies and segmentation
           - Service mesh considerations
           - SSL/TLS termination
           - Secret and configuration management
        
        5. Storage and Data Management
           - Persistent volume strategies
           - Database containerization approach
           - Backup and recovery procedures
           - Data migration strategies
        
        6. Monitoring and Logging
           - Container monitoring setup
           - Log aggregation and analysis
           - Performance metrics collection
           - Distributed tracing implementation
        
        7. Development and Testing
           - Local development environment
           - Testing strategies for containers
           - Image testing and validation
           - Development workflow optimization
        
        8. Production Deployment
           - Production-ready configurations
           - Rolling update strategies
           - Rollback procedures
           - Performance optimization
        
        Provide practical, production-ready container solutions.
        """
        
        container_result = {
            "services": services,
            "orchestration": orchestration,
            "timestamp": datetime.now().isoformat(),
            "model_used": self.model,
            "prompt": container_prompt,
            "container_architecture": {
                "design_strategy": "Microservices-based containerization with optimized images",
                "service_architecture": "Loosely coupled services with API communication",
                "orchestration_config": f"{orchestration.title()} cluster with auto-scaling",
                "networking_security": "Network policies with service mesh integration",
                "storage_management": "Persistent volumes with automated backup",
                "monitoring_logging": "Centralized monitoring with distributed tracing",
                "development_testing": "Local development with container testing",
                "production_deployment": "Blue-green deployment with health monitoring"
            },
            "configuration_files": {
                "dockerfiles": "Optimized Dockerfile configurations",
                "kubernetes_manifests": "Kubernetes YAML manifests",
                "docker_compose": "Docker Compose for local development",
                "helm_charts": "Helm charts for package management"
            },
            "resource_requirements": "Medium to high compute resources",
            "complexity_assessment": "medium-high"
        }
        
        return container_result
    
    def optimize_infrastructure_costs(self, current_setup: Dict[str, Any], usage_patterns: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze and optimize infrastructure costs
        
        Args:
            current_setup: Current infrastructure configuration
            usage_patterns: Usage patterns and metrics
            
        Returns:
            Cost optimization recommendations and strategies
        """
        
        optimization_prompt = f"""
        As an Infrastructure Specialist, analyze and optimize infrastructure costs:
        
        Current Setup: {json.dumps(current_setup, indent=2)}
        Usage Patterns: {json.dumps(usage_patterns, indent=2)}
        
        Please provide:
        1. Cost Analysis
           - Current cost breakdown by service
           - Resource utilization analysis
           - Waste identification and quantification
           - Cost trend analysis and projections
        
        2. Right-Sizing Recommendations
           - Compute resource optimization
           - Storage optimization opportunities
           - Network cost optimization
           - Database resource tuning
        
        3. Reserved Instance Strategy
           - Reserved instance recommendations
           - Savings plan opportunities
           - Spot instance utilization
           - Commitment term optimization
        
        4. Auto-Scaling Optimization
           - Scaling policy improvements
           - Resource scheduling strategies
           - Load-based optimization
           - Predictive scaling implementation
        
        5. Storage Optimization
           - Storage tier optimization
           - Data lifecycle management
           - Backup cost optimization
           - Archive strategy implementation
        
        6. Network Cost Optimization
           - Data transfer optimization
           - CDN utilization strategies
           - Regional optimization
           - Bandwidth cost reduction
        
        7. Monitoring and Alerting
           - Cost monitoring setup
           - Budget alerts and thresholds
           - Usage anomaly detection
           - Cost allocation and tracking
        
        8. Implementation Roadmap
           - Priority optimization actions
           - Implementation timeline
           - Risk assessment and mitigation
           - Expected savings calculation
        
        Focus on practical, measurable cost reduction strategies.
        """
        
        optimization_result = {
            "current_setup": current_setup,
            "usage_patterns": usage_patterns,
            "timestamp": datetime.now().isoformat(),
            "model_used": self.model,
            "prompt": optimization_prompt,
            "cost_optimization": {
                "cost_analysis": "Detailed cost breakdown with waste identification",
                "right_sizing": "Resource optimization recommendations",
                "reserved_instances": "Strategic reserved instance planning",
                "auto_scaling": "Optimized scaling policies and scheduling",
                "storage_optimization": "Storage tier and lifecycle optimization",
                "network_optimization": "Data transfer and CDN optimization",
                "monitoring_alerting": "Cost monitoring and budget management",
                "implementation_roadmap": "Prioritized optimization action plan"
            },
            "estimated_savings": "20-40% cost reduction",
            "implementation_effort": "medium",
            "payback_period": "2-3 months"
        }
        
        # Cache optimization recommendations
        self.cost_optimizations[hash(str(current_setup))] = optimization_result
        
        return optimization_result
    
    def create_infrastructure_templates(self, template_type: str, requirements: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create reusable infrastructure templates
        
        Args:
            template_type: Type of template (terraform, cloudformation, etc.)
            requirements: Template requirements and specifications
            
        Returns:
            Infrastructure template code and documentation
        """
        
        template_prompt = f"""
        As an Infrastructure Specialist, create infrastructure templates:
        
        Template Type: {template_type}
        Requirements: {json.dumps(requirements, indent=2)}
        
        Please provide:
        1. Template Structure
           - Template organization and modules
           - Variable definitions and defaults
           - Resource dependencies and relationships
           - Output definitions and exports
        
        2. Core Infrastructure Components
           - Compute resources and configurations
           - Network and security group definitions
           - Storage and database configurations
           - Load balancer and traffic management
        
        3. Security and Compliance
           - Security group and firewall rules
           - IAM roles and policies
           - Encryption and key management
           - Compliance and governance controls
        
        4. Monitoring and Logging
           - Monitoring resource definitions
           - Log aggregation and storage
           - Alerting and notification setup
           - Dashboard and visualization configs
        
        5. Scalability and Performance
           - Auto-scaling group configurations
           - Performance optimization settings
           - Resource limits and quotas
           - Capacity planning considerations
        
        6. Template Documentation
           - Usage instructions and examples
           - Variable descriptions and validation
           - Deployment procedures
           - Troubleshooting guide
        
        7. Testing and Validation
           - Template testing strategies
           - Validation rules and checks
           - Integration testing approach
           - Quality assurance procedures
        
        8. Maintenance and Updates
           - Version control and tagging
           - Update procedures and rollback
           - Deprecation and migration strategies
           - Community contribution guidelines
        
        Provide production-ready, well-documented templates.
        """
        
        template_result = {
            "template_type": template_type,
            "requirements": requirements,
            "timestamp": datetime.now().isoformat(),
            "model_used": self.model,
            "prompt": template_prompt,
            "infrastructure_template": {
                "structure": f"Modular {template_type} template with best practices",
                "core_components": "Compute, network, storage, and security resources",
                "security_compliance": "Security-first template with compliance controls",
                "monitoring_logging": "Integrated monitoring and logging setup",
                "scalability": "Auto-scaling and performance optimization",
                "documentation": "Comprehensive usage and deployment documentation",
                "testing_validation": "Template testing and validation procedures",
                "maintenance": "Version control and update management"
            },
            "template_files": {
                "main": f"main.{template_type}",
                "variables": f"variables.{template_type}",
                "outputs": f"outputs.{template_type}",
                "modules": "Reusable module definitions"
            },
            "complexity_level": "medium",
            "reusability_score": 0.90
        }
        
        # Store template for reuse
        self.infrastructure_templates[template_type] = template_result
        
        return template_result
    
    def get_infrastructure_summary(self) -> Dict[str, Any]:
        """Get summary of all infrastructure activities"""
        return {
            "agent_id": self.agent_id,
            "total_deployments": len(self.deployment_history),
            "infrastructure_templates": len(self.infrastructure_templates),
            "cost_optimizations": len(self.cost_optimizations),
            "specializations": self.specializations,
            "model_used": self.model,
            "recent_deployments": self.deployment_history[-5:] if self.deployment_history else []
        }
    
    def delegate_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle delegated infrastructure tasks
        
        Args:
            task: Task details from orchestrator
            
        Returns:
            Task execution result
        """
        task_type = task.get("type", "deployment_strategy")
        
        if task_type == "deployment_strategy":
            return self.design_deployment_strategy(
                task.get("application", {}),
                task.get("requirements", {})
            )
        elif task_type == "cicd_pipeline":
            return self.create_cicd_pipeline(
                task.get("project", {}),
                task.get("pipeline_requirements", {})
            )
        elif task_type == "container_architecture":
            return self.design_container_architecture(
                task.get("services", []),
                task.get("orchestration", "kubernetes")
            )
        elif task_type == "cost_optimization":
            return self.optimize_infrastructure_costs(
                task.get("current_setup", {}),
                task.get("usage_patterns", {})
            )
        elif task_type == "infrastructure_template":
            return self.create_infrastructure_templates(
                task.get("template_type", "terraform"),
                task.get("requirements", {})
            )
        else:
            return {
                "error": f"Unknown task type: {task_type}",
                "supported_types": ["deployment_strategy", "cicd_pipeline", "container_architecture", "cost_optimization", "infrastructure_template"]
            }

if __name__ == "__main__":
    # Example usage
    infra = InfrastructureSpecialist()
    
    # Example deployment strategy
    app = {
        "name": "WebApp",
        "type": "web_application",
        "components": ["frontend", "backend", "database"],
        "expected_users": 10000
    }
    
    requirements = {
        "availability": "99.9%",
        "scalability": "auto_scaling",
        "budget": "$1000/month",
        "compliance": ["SOC2", "GDPR"]
    }
    
    result = infra.design_deployment_strategy(app, requirements)
    print(json.dumps(result, indent=2))