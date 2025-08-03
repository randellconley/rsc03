#!/usr/bin/env python3
"""
RSC03 Multi-Agent Team Startup Script

This script demonstrates how to start the OpenHands multi-agent system
and coordinate agents using delegation patterns.
"""

import sys
import json
from pathlib import Path

# Add the current directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    
    # Look for .env file in project root
    project_root = Path(__file__).parent
    env_file = project_root / '.env'
    
    if env_file.exists():
        load_dotenv(env_file)
        print(f"🔑 Loaded API keys from {env_file}")
    else:
        print(f"⚠️  No .env file found. Create one from .env.example for API keys")
        
except ImportError:
    print("⚠️  python-dotenv not installed. Install with: pip install python-dotenv")

from workflows.multi_agent_workflow import MultiAgentWorkflowManager, AgentRole


def start_multi_agent_team(project_request: str):
    """
    Start the multi-agent team with a project request.
    
    This function demonstrates the OpenHands delegation pattern
    for coordinating multiple specialized agents.
    """
    
    print("RSC03 OpenHands Multi-Agent System")
    print("=" * 50)
    print(f"Project Request: {project_request}")
    print()
    
    # Initialize workflow manager
    workflow_manager = MultiAgentWorkflowManager()
    
    # For demonstration, use web application workflow
    workflow = workflow_manager.get_workflow_template("web_application")
    
    if not workflow:
        print("❌ No workflow template found")
        return
    
    print(f"Selected Workflow: {workflow.project_name}")
    print(f"Estimated Timeline: {workflow.estimated_timeline}")
    print(f"Number of Tasks: {len(workflow.tasks)}")
    print()
    
    # Generate delegation sequence
    delegations = workflow_manager.get_delegation_sequence(workflow)
    
    print("Delegation Sequence:")
    print("-" * 30)
    
    for i, delegation in enumerate(delegations, 1):
        print(f"{i}. {delegation['agent'].replace('_', ' ').title()}")
        print(f"   Task: {delegation['task']}")
        print(f"   Stage: {delegation['context']['stage']}")
        print(f"   Priority: {delegation['context']['priority']}")
        print()
    
    print("OpenHands Delegation Pattern:")
    print("-" * 30)
    print("# In actual OpenHands implementation, you would use:")
    print()
    
    for delegation in delegations[:3]:  # Show first 3 as examples
        agent_name = delegation['agent']
        task_desc = delegation['task']
        context = delegation['context']
        
        print(f"# Delegate to {agent_name}")
        print(f"result = agent_delegate(")
        print(f"    agent='{agent_name}',")
        print(f"    task='{task_desc}',")
        print(f"    context={json.dumps(context, indent=8)[1:-1]}")  # Format context nicely
        print(f")")
        print()
    
    print("This demonstrates how RSC03 uses OpenHands' agent_delegate")
    print("functionality to coordinate specialized agents in a")
    print("collaborative software development workflow.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        project_request = " ".join(sys.argv[1:])
    else:
        project_request = "Build a web application with user authentication"
    
    start_multi_agent_team(project_request)
