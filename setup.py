#!/usr/bin/env python3
"""
RSC03 Setup Script - OpenHands Multi-Agent System

This script initializes the RSC03 OpenHands multi-agent system,
validates the environment, and prepares the system for operation.
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, Any


def validate_openhands_environment() -> bool:
    """Validate that we're running in an OpenHands environment"""
    
    print("Validating OpenHands environment...")
    
    # Check for OpenHands-specific environment variables or files
    openhands_indicators = [
        "OPENHANDS_WORKSPACE",
        "OPENHANDS_AGENT_ID", 
        "OPENHANDS_SESSION_ID"
    ]
    
    found_indicators = []
    for indicator in openhands_indicators:
        if os.getenv(indicator):
            found_indicators.append(indicator)
    
    # Check for OpenHands directory structure
    workbench_path = Path("/home/ubuntu/environment/workbench")
    openhands_path = workbench_path / ".openhands"
    
    if openhands_path.exists():
        print("  ✓ OpenHands directory structure detected")
        found_indicators.append("openhands_directory")
    
    if found_indicators:
        print(f"  ✓ OpenHands environment validated: {', '.join(found_indicators)}")
        return True
    else:
        print("  ⚠ OpenHands environment not clearly detected, but proceeding...")
        return True  # Allow setup to continue


def create_directory_structure():
    """Create the required directory structure for RSC03"""
    
    base_path = Path(__file__).parent
    
    directories = [
        "agents",
        "workflows", 
        "configs",
        "examples",
        "docs",
        "logs",
        "workspace"  # Shared workspace for agent collaboration
    ]
    
    print("Creating directory structure...")
    for directory in directories:
        dir_path = base_path / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {directory}")


def create_agent_configurations():
    """Create configuration files for all agents"""
    
    base_path = Path(__file__).parent
    configs_dir = base_path / "configs"
    
    # Agent configurations based on RSC02 agent types
    agent_configs = {
        "project_orchestrator": {
            "role": "Project Orchestrator & Technical Lead",
            "goal": "Define project scope, break down requirements, coordinate team efforts, and ensure deliverable quality",
            "llm_model": "gpt-4",  # High reasoning capability needed
            "specializations": ["project_management", "coordination", "planning", "quality_assurance"],
            "delegation_capability": True,
            "coordination_role": True,
            "max_concurrent_tasks": 5,
            "workflow_stages": ["analysis", "review"]
        },
        "research_analyst": {
            "role": "Technical Research Specialist", 
            "goal": "Research technologies, analyze existing codebases, and provide technical recommendations",
            "llm_model": "gpt-4",  # Good research and analysis capability
            "specializations": ["technology_research", "code_analysis", "best_practices", "emerging_technologies"],
            "delegation_capability": False,
            "coordination_role": False,
            "max_concurrent_tasks": 3,
            "workflow_stages": ["analysis"]
        },
        "solution_architect": {
            "role": "Solution Architect & Designer",
            "goal": "Design technical solutions, create system architecture, and define implementation strategies", 
            "llm_model": "gpt-4",  # Complex architectural reasoning needed
            "specializations": ["system_design", "architecture", "technical_specifications", "scalability"],
            "delegation_capability": False,
            "coordination_role": False,
            "max_concurrent_tasks": 2,
            "workflow_stages": ["architecture"]
        },
        "code_implementer": {
            "role": "Senior Software Developer",
            "goal": "Implement solutions, write high-quality code, and integrate components",
            "llm_model": "gpt-4",  # Strong coding capability needed
            "specializations": ["full_stack_development", "coding", "integration", "debugging"],
            "delegation_capability": False,
            "coordination_role": False,
            "max_concurrent_tasks": 3,
            "workflow_stages": ["implementation"]
        },
        "quality_assurance": {
            "role": "Quality Assurance Engineer",
            "goal": "Review code quality, test solutions, and ensure reliability",
            "llm_model": "gpt-4",  # Attention to detail needed
            "specializations": ["testing", "quality_validation", "code_review", "bug_detection"],
            "delegation_capability": False,
            "coordination_role": False,
            "max_concurrent_tasks": 2,
            "workflow_stages": ["testing", "review"]
        },
        "technical_writer": {
            "role": "Technical Documentation Specialist",
            "goal": "Create comprehensive documentation, user guides, and technical specifications",
            "llm_model": "gpt-3.5-turbo",  # Cost-effective for text generation
            "specializations": ["documentation", "technical_writing", "user_guides", "api_docs"],
            "delegation_capability": False,
            "coordination_role": False,
            "max_concurrent_tasks": 2,
            "workflow_stages": ["documentation"]
        },
        "infrastructure_specialist": {
            "role": "Infrastructure Specialist",
            "goal": "Design deployment, DevOps, and infrastructure solutions",
            "llm_model": "gpt-3.5-turbo",  # Cost-effective for operational tasks
            "specializations": ["deployment", "devops", "infrastructure", "containerization"],
            "delegation_capability": False,
            "coordination_role": False,
            "max_concurrent_tasks": 2,
            "workflow_stages": ["deployment"]
        },
        "security_specialist": {
            "role": "Security Architecture Specialist",
            "goal": "Design secure, robust authentication and authorization systems",
            "llm_model": "gpt-4",  # Security requires high reasoning
            "specializations": ["security_architecture", "authentication", "authorization", "compliance"],
            "delegation_capability": False,
            "coordination_role": False,
            "max_concurrent_tasks": 2,
            "workflow_stages": ["architecture", "review"]
        }
    }
    
    # Save agent configurations
    config_file = configs_dir / "agent_configs.json"
    with open(config_file, 'w') as f:
        json.dump(agent_configs, f, indent=2)
    
    print(f"  ✓ Created agent configurations: {config_file}")
    
    # Create workflow configuration
    workflow_config = {
        "default_workflow": "web_application",
        "available_workflows": ["web_application", "api_service", "custom"],
        "delegation_timeout": 300,  # 5 minutes
        "max_delegation_depth": 3,
        "parallel_execution": True,
        "quality_gates": {
            "code_review_required": True,
            "testing_required": True,
            "documentation_required": True
        }
    }
    
    workflow_config_file = configs_dir / "workflow_config.json"
    with open(workflow_config_file, 'w') as f:
        json.dump(workflow_config, f, indent=2)
    
    print(f"  ✓ Created workflow configuration: {workflow_config_file}")


def create_example_project():
    """Create an example project to demonstrate the system"""
    
    base_path = Path(__file__).parent
    examples_dir = base_path / "examples"
    
    example_project = {
        "project_id": "example_web_app",
        "project_name": "Example Web Application",
        "project_type": "web_application",
        "description": "A simple web application with user authentication to demonstrate the multi-agent system",
        "requirements": [
            "User registration and login system",
            "Secure password handling with hashing",
            "JWT-based authentication",
            "Responsive web interface with React",
            "FastAPI backend with PostgreSQL database",
            "Comprehensive test coverage",
            "API documentation",
            "Deployment configuration"
        ],
        "success_criteria": [
            "Users can register and login successfully",
            "All API endpoints are secure and functional",
            "Frontend is responsive and user-friendly",
            "Test coverage is above 80%",
            "Complete documentation is available",
            "Application can be deployed successfully"
        ],
        "constraints": {
            "timeline": "2-3 weeks",
            "budget": "medium",
            "team_size": "8 agents",
            "technology_stack": {
                "backend": "FastAPI",
                "frontend": "React", 
                "database": "PostgreSQL",
                "deployment": "Docker"
            }
        }
    }
    
    example_file = examples_dir / "example_web_app.json"
    with open(example_file, 'w') as f:
        json.dump(example_project, f, indent=2)
    
    print(f"  ✓ Created example project: {example_file}")


def create_startup_script():
    """Create a startup script for the multi-agent system"""
    
    base_path = Path(__file__).parent
    
    startup_script = '''#!/usr/bin/env python3
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
'''
    
    startup_file = base_path / "start_team.py"
    with open(startup_file, 'w') as f:
        f.write(startup_script)
    
    # Make it executable
    startup_file.chmod(0o755)
    
    print(f"  ✓ Created startup script: {startup_file}")


def create_documentation():
    """Create basic documentation files"""
    
    base_path = Path(__file__).parent
    docs_dir = base_path / "docs"
    
    # Agent delegation guide
    delegation_guide = '''# OpenHands Agent Delegation Guide for RSC03

## Overview

RSC03 uses OpenHands' `agent_delegate` functionality to create a collaborative
multi-agent software development team. Each agent is specialized for specific
roles and can delegate tasks to other agents.

## Agent Roles

### Project Orchestrator
- **Role**: Main coordinator and technical lead
- **Capabilities**: Task decomposition, team coordination, quality assurance
- **Delegation**: Can delegate to all other agents
- **LLM**: GPT-4 (high reasoning needed)

### Research Analyst  
- **Role**: Technology research and analysis
- **Capabilities**: Research, code analysis, best practices
- **Delegation**: None (specialist role)
- **LLM**: GPT-4 (research and analysis)

### Solution Architect
- **Role**: System design and architecture
- **Capabilities**: Architecture design, technical specifications
- **Delegation**: None (specialist role)
- **LLM**: GPT-4 (complex reasoning)

### Code Implementer
- **Role**: Full-stack development
- **Capabilities**: Coding, integration, debugging
- **Delegation**: None (specialist role)
- **LLM**: GPT-4 (strong coding capability)

### Quality Assurance
- **Role**: Testing and quality validation
- **Capabilities**: Testing, code review, bug detection
- **Delegation**: None (specialist role)
- **LLM**: GPT-4 (attention to detail)

### Technical Writer
- **Role**: Documentation specialist
- **Capabilities**: Documentation, user guides, API docs
- **Delegation**: None (specialist role)
- **LLM**: GPT-3.5-turbo (cost-effective)

### Infrastructure Specialist
- **Role**: Deployment and DevOps
- **Capabilities**: Deployment, infrastructure, containerization
- **Delegation**: None (specialist role)
- **LLM**: GPT-3.5-turbo (operational tasks)

### Security Specialist
- **Role**: Security architecture
- **Capabilities**: Security design, authentication, authorization
- **Delegation**: None (specialist role)
- **LLM**: GPT-4 (security reasoning)

## Delegation Pattern

```python
# Basic delegation syntax
result = agent_delegate(
    agent="target_agent_name",
    task="Specific task description",
    context={
        "key": "value",
        "requirements": [...],
        "constraints": {...}
    }
)
```

## Example Workflow

1. **User Request** → Project Orchestrator
2. **Project Orchestrator** analyzes and delegates:
   - Research → Research Analyst
   - Architecture → Solution Architect  
   - Security → Security Specialist
3. **Implementation Phase**:
   - Backend → Code Implementer
   - Frontend → Code Implementer
4. **Quality Phase**:
   - Testing → Quality Assurance
   - Documentation → Technical Writer
5. **Deployment Phase**:
   - Infrastructure → Infrastructure Specialist

## Cost Optimization

- **GPT-4**: Used for complex reasoning (orchestrator, architect, security, QA, implementer)
- **GPT-3.5-turbo**: Used for routine tasks (documentation, infrastructure)
- **Estimated Savings**: 40-60% compared to using GPT-4 for all agents

## Benefits

- **Specialization**: Each agent optimized for specific tasks
- **Parallel Processing**: Multiple agents can work simultaneously
- **Quality**: Specialized expertise leads to better outcomes
- **Cost Efficiency**: Right model for the right task
- **Scalability**: Easy to add new specialized agents
'''
    
    delegation_guide_file = docs_dir / "delegation_guide.md"
    with open(delegation_guide_file, 'w') as f:
        f.write(delegation_guide)
    
    print(f"  ✓ Created delegation guide: {delegation_guide_file}")


def main():
    """Main setup function"""
    
    print("RSC03 OpenHands Multi-Agent System Setup")
    print("=" * 50)
    
    try:
        # Validate OpenHands environment
        openhands_valid = validate_openhands_environment()
        print()
        
        # Create directory structure
        create_directory_structure()
        print()
        
        # Create configuration files
        print("Creating configuration files...")
        create_agent_configurations()
        print()
        
        # Create example project
        print("Creating example files...")
        create_example_project()
        print()
        
        # Create startup script
        print("Creating startup script...")
        create_startup_script()
        print()
        
        # Create documentation
        print("Creating documentation...")
        create_documentation()
        print()
        
        # Summary
        print("Setup Summary")
        print("-" * 30)
        print("✓ Directory structure created")
        print("✓ Agent configurations created (8 specialized agents)")
        print("✓ Workflow configurations created")
        print("✓ Example project created")
        print("✓ Startup script created")
        print("✓ Documentation created")
        print()
        
        print("🎉 RSC03 OpenHands Multi-Agent System setup completed!")
        print()
        print("Key Features:")
        print("- Pure OpenHands implementation (no external dependencies)")
        print("- 8 specialized agents with role-based optimization")
        print("- Agent delegation using OpenHands' agent_delegate")
        print("- Cost-optimized LLM usage (GPT-4 + GPT-3.5-turbo)")
        print("- Workflow templates for common project types")
        print()
        print("Next Steps:")
        print("1. Configure LLM API keys in your OpenHands environment")
        print("2. Run: python start_team.py 'Your project description'")
        print("3. Explore the example project in examples/")
        print("4. Read the delegation guide in docs/")
        
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()