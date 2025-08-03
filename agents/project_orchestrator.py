"""
Project Orchestrator Agent for RSC03 OpenHands Multi-Agent System

This agent serves as the main coordinator for software development projects,
using OpenHands' agent_delegate functionality to coordinate with specialist agents.

Role: Project Orchestrator & Technical Lead
Goal: Define project scope, break down requirements, coordinate team efforts, and ensure deliverable quality
"""

from typing import Dict, Any, List
import json


class ProjectOrchestratorAgent:
    """
    Project Orchestrator Agent using OpenHands delegation patterns.
    
    This agent acts as the technical lead and project manager, receiving high-level
    requirements and coordinating specialist agents to deliver complete solutions.
    """
    
    def __init__(self):
        self.agent_name = "project_orchestrator"
        self.role = "Project Orchestrator & Technical Lead"
        self.specializations = [
            "project_management",
            "requirement_analysis", 
            "task_decomposition",
            "team_coordination",
            "quality_assurance"
        ]
        
        # Available specialist agents for delegation
        self.available_agents = {
            "research_analyst": "Technology research and code analysis",
            "solution_architect": "System design and architecture planning", 
            "code_implementer": "Full-stack development and implementation",
            "quality_assurance": "Testing, code review, and quality validation",
            "technical_writer": "Documentation and user guides",
            "infrastructure_specialist": "Deployment and system operations",
            "security_specialist": "Security architecture and implementation"
        }
    
    def get_system_prompt(self) -> str:
        """Get the specialized system prompt for this agent"""
        return f"""You are a {self.role} in an OpenHands multi-agent software development team.

ROLE & RESPONSIBILITIES:
- Analyze project requirements and break them down into manageable tasks
- Coordinate with specialist agents using agent_delegate actions
- Ensure project quality and deliverable standards
- Manage project timeline and dependencies
- Provide technical leadership and decision-making

AVAILABLE SPECIALIST AGENTS:
{json.dumps(self.available_agents, indent=2)}

DELEGATION PATTERN:
Use agent_delegate(agent="agent_name", task="specific_task", context={{...}}) to delegate tasks to specialists.

WORKFLOW APPROACH:
1. Analyze the user's requirements thoroughly
2. Break down complex projects into specific tasks
3. Delegate tasks to appropriate specialist agents
4. Coordinate between agents and manage dependencies
5. Review and integrate results from all agents
6. Ensure final deliverable meets requirements

COMMUNICATION STYLE:
- Clear, technical, and professional
- Focus on actionable tasks and specific requirements
- Provide context and background for delegated tasks
- Coordinate timing and dependencies between agents

You excel at translating business requirements into technical specifications and managing complex development workflows."""

    def analyze_project_requirements(self, user_request: str) -> Dict[str, Any]:
        """
        Analyze user requirements and create project breakdown
        
        Args:
            user_request: The user's project request
            
        Returns:
            Project analysis with task breakdown and delegation plan
        """
        
        # This would be implemented as part of the OpenHands agent's reasoning
        # The actual implementation would use the agent's LLM capabilities
        
        analysis_template = {
            "project_type": "web_application",  # Determined from request
            "complexity": "medium",  # Assessed complexity
            "estimated_timeline": "2-3 weeks",
            "required_specialists": [
                "solution_architect",
                "code_implementer", 
                "quality_assurance",
                "technical_writer"
            ],
            "task_breakdown": [
                {
                    "task_id": "architecture_design",
                    "description": "Design system architecture and technical specifications",
                    "assigned_agent": "solution_architect",
                    "priority": "high",
                    "dependencies": []
                },
                {
                    "task_id": "backend_implementation",
                    "description": "Implement backend API and database",
                    "assigned_agent": "code_implementer",
                    "priority": "high", 
                    "dependencies": ["architecture_design"]
                },
                {
                    "task_id": "frontend_implementation",
                    "description": "Implement user interface and frontend",
                    "assigned_agent": "code_implementer",
                    "priority": "high",
                    "dependencies": ["architecture_design"]
                },
                {
                    "task_id": "quality_validation",
                    "description": "Test implementation and validate quality",
                    "assigned_agent": "quality_assurance",
                    "priority": "medium",
                    "dependencies": ["backend_implementation", "frontend_implementation"]
                },
                {
                    "task_id": "documentation",
                    "description": "Create technical documentation and user guides",
                    "assigned_agent": "technical_writer",
                    "priority": "low",
                    "dependencies": ["quality_validation"]
                }
            ]
        }
        
        return analysis_template
    
    def create_delegation_context(self, task: Dict[str, Any], project_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create context for agent delegation
        
        Args:
            task: Specific task to delegate
            project_context: Overall project context
            
        Returns:
            Context dictionary for delegation
        """
        
        return {
            "task_id": task["task_id"],
            "task_description": task["description"],
            "project_type": project_context.get("project_type"),
            "project_requirements": project_context.get("requirements", []),
            "dependencies": task.get("dependencies", []),
            "priority": task.get("priority", "medium"),
            "expected_deliverables": task.get("deliverables", []),
            "constraints": project_context.get("constraints", {}),
            "timeline": project_context.get("timeline")
        }
    
    def get_example_delegations(self) -> List[Dict[str, Any]]:
        """Get example delegation patterns for different project types"""
        
        return [
            {
                "project_type": "web_application",
                "delegations": [
                    {
                        "agent": "solution_architect",
                        "task": "Design web application architecture with user authentication",
                        "context": {
                            "requirements": ["user registration", "login system", "secure sessions"],
                            "technology_preferences": ["Python", "FastAPI", "React"],
                            "scalability_needs": "medium"
                        }
                    },
                    {
                        "agent": "code_implementer", 
                        "task": "Implement FastAPI backend with authentication system",
                        "context": {
                            "architecture_plan": "from_solution_architect",
                            "database_schema": "from_solution_architect",
                            "api_specifications": "from_solution_architect"
                        }
                    }
                ]
            },
            {
                "project_type": "api_service",
                "delegations": [
                    {
                        "agent": "research_analyst",
                        "task": "Research best practices for RESTful API design",
                        "context": {
                            "domain": "user_management",
                            "performance_requirements": "high",
                            "security_requirements": "enterprise"
                        }
                    },
                    {
                        "agent": "security_specialist",
                        "task": "Design API security architecture",
                        "context": {
                            "authentication_method": "JWT",
                            "authorization_model": "RBAC",
                            "compliance_requirements": ["GDPR", "SOC2"]
                        }
                    }
                ]
            }
        ]


def get_orchestrator_prompt_template() -> str:
    """Get the complete prompt template for the Project Orchestrator agent"""
    
    return """You are a Project Orchestrator & Technical Lead in an OpenHands multi-agent software development team.

CORE RESPONSIBILITIES:
1. Analyze user requirements and break them into manageable tasks
2. Coordinate specialist agents using agent_delegate actions  
3. Manage project timeline, dependencies, and quality standards
4. Provide technical leadership and architectural guidance
5. Ensure deliverables meet user requirements and quality standards

AVAILABLE SPECIALIST AGENTS:
- research_analyst: Technology research and code analysis
- solution_architect: System design and architecture planning
- code_implementer: Full-stack development and implementation  
- quality_assurance: Testing, code review, and quality validation
- technical_writer: Documentation and user guides
- infrastructure_specialist: Deployment and system operations
- security_specialist: Security architecture and implementation

DELEGATION WORKFLOW:
1. Analyze the user's request thoroughly
2. Break down complex requirements into specific, actionable tasks
3. Determine which specialist agents are needed
4. Use agent_delegate(agent="agent_name", task="specific_task", context={...}) for each task
5. Coordinate timing and dependencies between delegated tasks
6. Review and integrate results from all agents
7. Ensure final deliverable is complete and meets requirements

DELEGATION BEST PRACTICES:
- Provide clear, specific task descriptions
- Include relevant context and background information
- Specify expected deliverables and success criteria
- Indicate dependencies and timing requirements
- Use appropriate specialist for each task type

COMMUNICATION STYLE:
- Professional and technical
- Clear and actionable instructions
- Comprehensive context for delegated tasks
- Focus on deliverable quality and user satisfaction

When you receive a user request, start by analyzing the requirements, then create a project plan with specific tasks to delegate to appropriate specialist agents."""


if __name__ == "__main__":
    # Example usage and testing
    orchestrator = ProjectOrchestratorAgent()
    
    print("Project Orchestrator Agent")
    print("=" * 50)
    print(f"Role: {orchestrator.role}")
    print(f"Specializations: {orchestrator.specializations}")
    print(f"Available Agents: {list(orchestrator.available_agents.keys())}")
    
    print("\nSystem Prompt:")
    print("-" * 30)
    print(orchestrator.get_system_prompt())
    
    print("\nExample Delegations:")
    print("-" * 30)
    examples = orchestrator.get_example_delegations()
    for example in examples:
        print(f"Project Type: {example['project_type']}")
        for delegation in example['delegations']:
            print(f"  → {delegation['agent']}: {delegation['task']}")
        print()