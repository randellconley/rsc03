#!/usr/bin/env python3
"""
RSC03 Interactive Multi-Agent Chat Interface

This provides an interactive chat interface similar to OpenHands
where you can directly communicate with the specialized agents.
"""

import sys
import json
import asyncio
from pathlib import Path
from typing import Dict, List, Optional
import readline  # For better input handling

# Add the current directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from utils.model_manager import ModelManager, get_model_for_agent
from workflows.multi_agent_workflow import MultiAgentWorkflowManager, AgentRole


class InteractiveAgentChat:
    """Interactive chat interface for RSC03 multi-agent system"""
    
    def __init__(self):
        self.model_manager = ModelManager()
        self.workflow_manager = MultiAgentWorkflowManager()
        self.current_agent = None
        self.chat_history = []
        self.available_agents = {
            'orchestrator': 'Project Orchestrator - Overall project coordination',
            'research': 'Research Analyst - Information gathering and analysis',
            'architect': 'Solution Architect - System design and architecture',
            'coder': 'Code Implementer - Code generation and implementation',
            'qa': 'Quality Assurance - Testing and quality control',
            'writer': 'Technical Writer - Documentation and communication',
            'infra': 'Infrastructure Specialist - DevOps and deployment',
            'security': 'Security Specialist - Security analysis and hardening'
        }
        
    def display_welcome(self):
        """Display welcome message and available commands"""
        print("\n" + "="*70)
        print("🤖 RSC03 INTERACTIVE MULTI-AGENT CLI CHAT")
        print("="*70)
        print("Welcome to the RSC03 Multi-Agent System!")
        print("Chat directly with 8 specialized AI agents using optimal models.")
        print("\n📋 Available Commands:")
        print("  /agents     - List all available agents with model info")
        print("  /switch     - Switch to a different agent")
        print("  /status     - Show current agent and model info")
        print("  /history    - Show recent chat history")
        print("  /clear      - Clear chat history")
        print("  /workflow   - Start a structured workflow")
        print("  /costs      - Show usage and cost summary")
        print("  /models     - Show all model assignments")
        print("  /save       - Save chat session to file")
        print("  /help       - Show this help message")
        print("  /quit       - Exit the chat")
        print("\n🎯 Quick Start:")
        print("  Type '/switch orchestrator' to start with the Project Orchestrator")
        print("  Type '/agents' to see all available specialists")
        print("  Type '/models' to see the multi-model distribution")
        print("="*70)
        
    def display_agents(self):
        """Display available agents"""
        print("\n🤖 Available Agents:")
        print("-" * 70)
        for key, description in self.available_agents.items():
            model, config = get_model_for_agent(self._get_agent_class_name(key))
            status = "✅" if self.current_agent == key else "⚪"
            cost_tier = config.get('cost_tier', 'unknown')
            print(f"  {status} /{key:<12} - {description}")
            print(f"     {'':14} Model: {model} | Cost: {cost_tier}")
        print("-" * 70)
        print("💡 Use '/switch <agent>' to select an agent (e.g., '/switch orchestrator')")
        
    def display_models(self):
        """Display all model assignments"""
        print("\n🧠 Multi-Model Distribution:")
        print("-" * 70)
        
        model_groups = {}
        for key, description in self.available_agents.items():
            agent_class_name = self._get_agent_class_name(key)
            model, config = get_model_for_agent(agent_class_name)
            
            if model not in model_groups:
                model_groups[model] = []
            model_groups[model].append({
                'key': key,
                'description': description,
                'cost_tier': config.get('cost_tier', 'unknown')
            })
        
        for model, agents in model_groups.items():
            print(f"\n🔹 {model}:")
            for agent in agents:
                print(f"    • {agent['description']} ({agent['cost_tier']})")
        
        print("-" * 70)
        print("💡 This distribution optimizes cost and performance for each agent's role")
        
    def save_session(self):
        """Save chat session to file"""
        if not self.chat_history:
            print("❌ No chat history to save.")
            return
            
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"rsc03_chat_session_{timestamp}.txt"
        
        try:
            with open(filename, 'w') as f:
                f.write("RSC03 Multi-Agent Chat Session\n")
                f.write("=" * 50 + "\n")
                f.write(f"Saved: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total Messages: {len(self.chat_history)}\n\n")
                
                for i, entry in enumerate(self.chat_history, 1):
                    agent = entry.get('agent', 'unknown')
                    user_msg = entry.get('user_message', '')
                    agent_msg = entry.get('agent_response', '')
                    
                    f.write(f"--- Message {i} ---\n")
                    f.write(f"Agent: {self.available_agents.get(agent, agent)}\n")
                    f.write(f"User: {user_msg}\n")
                    f.write(f"Response: {agent_msg}\n\n")
                    
            print(f"✅ Chat session saved to: {filename}")
            
        except Exception as e:
            print(f"❌ Error saving session: {e}")
        
    def _get_agent_class_name(self, agent_key: str) -> str:
        """Convert agent key to class name"""
        mapping = {
            'orchestrator': 'project_orchestrator',
            'research': 'research_analyst',
            'architect': 'solution_architect',
            'coder': 'code_implementer',
            'qa': 'quality_assurance',
            'writer': 'technical_writer',
            'infra': 'infrastructure_specialist',
            'security': 'security_specialist'
        }
        return mapping.get(agent_key, agent_key)
        
    def switch_agent(self, agent_key: str):
        """Switch to a different agent"""
        if agent_key not in self.available_agents:
            print(f"❌ Unknown agent: {agent_key}")
            print("Available agents:", ", ".join(self.available_agents.keys()))
            return False
            
        self.current_agent = agent_key
        agent_class_name = self._get_agent_class_name(agent_key)
        model, config = get_model_for_agent(agent_class_name)
        
        print(f"\n🔄 Switched to: {self.available_agents[agent_key]}")
        print(f"🧠 Using Model: {model}")
        print(f"💰 Cost Tier: {config.get('cost_tier', 'unknown')}")
        print(f"📝 You can now chat directly with this agent!")
        print("-" * 50)
        return True
        
    def display_status(self):
        """Display current status"""
        if not self.current_agent:
            print("\n❌ No agent selected. Use '/switch <agent>' to select one.")
            return
            
        agent_class_name = self._get_agent_class_name(self.current_agent)
        model, config = get_model_for_agent(agent_class_name)
        
        print(f"\n📊 Current Status:")
        print(f"  🤖 Active Agent: {self.available_agents[self.current_agent]}")
        print(f"  🧠 Model: {model}")
        print(f"  💰 Cost Tier: {config.get('cost_tier', 'unknown')}")
        print(f"  📈 Chat Messages: {len(self.chat_history)}")
        
    def display_costs(self):
        """Display usage and cost summary"""
        try:
            summary = self.model_manager.get_usage_summary()
            breakdown = self.model_manager.get_cost_breakdown()
            
            print(f"\n💰 Usage & Cost Summary:")
            print(f"  📊 Total Requests: {summary.get('total_requests', 0)}")
            print(f"  💵 Total Cost: ${summary.get('total_cost', 0.0):.4f}")
            print(f"  📈 Average Cost/Request: ${summary.get('avg_cost_per_request', 0.0):.4f}")
            
            if breakdown.get('by_tier'):
                print(f"\n📊 Cost by Tier:")
                for tier, cost in breakdown['by_tier'].items():
                    print(f"    {tier}: ${cost:.4f}")
                    
        except Exception as e:
            print(f"❌ Error getting cost summary: {e}")
            
    def display_history(self):
        """Display chat history"""
        if not self.chat_history:
            print("\n📝 No chat history yet.")
            return
            
        print(f"\n📝 Chat History ({len(self.chat_history)} messages):")
        print("-" * 50)
        for i, entry in enumerate(self.chat_history[-10:], 1):  # Show last 10
            agent = entry.get('agent', 'unknown')
            message = entry.get('message', '')[:100] + ('...' if len(entry.get('message', '')) > 100 else '')
            print(f"  {i}. [{agent}] {message}")
        print("-" * 50)
        
    def simulate_agent_response(self, message: str) -> str:
        """
        Simulate agent response (placeholder for actual AI integration)
        In a real implementation, this would call the actual AI models
        """
        if not self.current_agent:
            return "❌ No agent selected. Use '/switch <agent>' first."
            
        agent_name = self.available_agents[self.current_agent]
        agent_class_name = self._get_agent_class_name(self.current_agent)
        model, _ = get_model_for_agent(agent_class_name)
        
        # Simulate different agent personalities/responses
        responses = {
            'orchestrator': f"🎯 As the Project Orchestrator using {model}, I'll coordinate this request: {message[:50]}... Let me delegate this to the appropriate specialists.",
            'research': f"🔍 Research Analyst here using {model}. I'll analyze this topic: {message[:50]}... Let me gather comprehensive information.",
            'architect': f"🏗️ Solution Architect with {model} reporting. For your request: {message[:50]}... I'll design a robust system architecture.",
            'coder': f"💻 Code Implementer using {model}. I'll implement: {message[:50]}... Let me write efficient, clean code.",
            'qa': f"🔍 QA Specialist with {model}. I'll test: {message[:50]}... Let me ensure quality and reliability.",
            'writer': f"📝 Technical Writer using {model}. I'll document: {message[:50]}... Let me create clear documentation.",
            'infra': f"⚙️ Infrastructure Specialist with {model}. For deployment: {message[:50]}... I'll set up robust infrastructure.",
            'security': f"🔒 Security Specialist using {model}. Security analysis of: {message[:50]}... Let me identify and mitigate risks."
        }
        
        return responses.get(self.current_agent, f"🤖 Agent response using {model}: {message}")
        
    def start_workflow(self):
        """Start a structured workflow"""
        print("\n🔄 Available Workflows:")
        print("  1. Web Application Development")
        print("  2. API Development")
        print("  3. Data Analysis Project")
        print("  4. Security Audit")
        print("  5. Custom Workflow")
        
        choice = input("\nSelect workflow (1-5): ").strip()
        
        if choice == "1":
            workflow = self.workflow_manager.get_workflow_template("web_application")
            if workflow:
                print(f"\n🚀 Starting: {workflow.project_name}")
                print(f"⏱️ Timeline: {workflow.estimated_timeline}")
                delegations = self.workflow_manager.get_delegation_sequence(workflow)
                print(f"📋 Tasks: {len(delegations)} delegation steps")
                for i, delegation in enumerate(delegations[:3], 1):
                    print(f"  {i}. {delegation.agent_role.value} - {delegation.task_description[:60]}...")
            else:
                print("❌ Workflow template not found")
        else:
            print("🚧 Other workflows coming soon!")
            
    def run(self):
        """Main chat loop"""
        self.display_welcome()
        
        while True:
            try:
                # Show current agent in prompt
                agent_prompt = f"[{self.current_agent}]" if self.current_agent else "[no agent]"
                user_input = input(f"\n{agent_prompt} > ").strip()
                
                if not user_input:
                    continue
                    
                # Handle commands
                if user_input.startswith('/'):
                    command_parts = user_input[1:].split()
                    command = command_parts[0].lower()
                    
                    if command == 'quit' or command == 'exit':
                        print("\n👋 Goodbye! Thanks for using RSC03 Multi-Agent System!")
                        break
                        
                    elif command == 'help':
                        self.display_welcome()
                        
                    elif command == 'agents':
                        self.display_agents()
                        
                    elif command == 'switch':
                        if len(command_parts) > 1:
                            self.switch_agent(command_parts[1])
                        else:
                            print("Usage: /switch <agent_name>")
                            self.display_agents()
                            
                    elif command == 'status':
                        self.display_status()
                        
                    elif command == 'history':
                        self.display_history()
                        
                    elif command == 'clear':
                        self.chat_history.clear()
                        print("✅ Chat history cleared.")
                        
                    elif command == 'workflow':
                        self.start_workflow()
                        
                    elif command == 'costs':
                        self.display_costs()
                        
                    elif command == 'models':
                        self.display_models()
                        
                    elif command == 'save':
                        self.save_session()
                        
                    else:
                        print(f"❌ Unknown command: /{command}")
                        print("Type '/help' for available commands.")
                        
                else:
                    # Handle regular chat message
                    if not self.current_agent:
                        print("❌ Please select an agent first using '/switch <agent>'")
                        print("Type '/agents' to see available agents.")
                        continue
                        
                    # Simulate agent response
                    response = self.simulate_agent_response(user_input)
                    print(f"\n🤖 {response}")
                    
                    # Add to history
                    self.chat_history.append({
                        'agent': self.current_agent,
                        'user_message': user_input,
                        'agent_response': response,
                        'timestamp': str(Path(__file__).stat().st_mtime)  # Simple timestamp
                    })
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye! Thanks for using RSC03 Multi-Agent System!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                print("Type '/help' for available commands.")


def main():
    """Main entry point"""
    try:
        chat = InteractiveAgentChat()
        chat.run()
    except Exception as e:
        print(f"❌ Failed to start interactive chat: {e}")
        print("Make sure all dependencies are installed and configured.")
        sys.exit(1)


if __name__ == "__main__":
    main()