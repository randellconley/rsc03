"""
Multi-Agent Workflow System for RSC03 OpenHands

This module defines the workflow patterns and coordination logic for
OpenHands multi-agent collaboration using agent_delegate functionality.
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum
import json


class WorkflowStage(Enum):
    """Workflow stages for multi-agent projects"""
    ANALYSIS = "analysis"
    ARCHITECTURE = "architecture" 
    IMPLEMENTATION = "implementation"
    TESTING = "testing"
    DOCUMENTATION = "documentation"
    DEPLOYMENT = "deployment"
    REVIEW = "review"


class AgentRole(Enum):
    """Available agent roles in the system"""
    PROJECT_ORCHESTRATOR = "project_orchestrator"
    RESEARCH_ANALYST = "research_analyst"
    SOLUTION_ARCHITECT = "solution_architect"
    CODE_IMPLEMENTER = "code_implementer"
    QUALITY_ASSURANCE = "quality_assurance"
    TECHNICAL_WRITER = "technical_writer"
    INFRASTRUCTURE_SPECIALIST = "infrastructure_specialist"
    SECURITY_SPECIALIST = "security_specialist"


@dataclass
class WorkflowTask:
    """Represents a task in the multi-agent workflow"""
    task_id: str
    description: str
    assigned_agent: AgentRole
    stage: WorkflowStage
    priority: str  # "high", "medium", "low"
    dependencies: List[str]  # List of task_ids this task depends on
    estimated_duration: str
    deliverables: List[str]
    context: Dict[str, Any]


@dataclass
class ProjectWorkflow:
    """Represents a complete multi-agent project workflow"""
    project_id: str
    project_name: str
    project_type: str
    description: str
    requirements: List[str]
    tasks: List[WorkflowTask]
    estimated_timeline: str
    success_criteria: List[str]


class MultiAgentWorkflowManager:
    """
    Manages multi-agent workflows and coordination patterns for OpenHands.
    
    This class provides workflow templates and coordination logic for
    different types of software development projects.
    """
    
    def __init__(self):
        self.workflow_templates = self._initialize_workflow_templates()
        self.agent_capabilities = self._initialize_agent_capabilities()
    
    def _initialize_workflow_templates(self) -> Dict[str, ProjectWorkflow]:
        """Initialize predefined workflow templates"""
        
        templates = {}
        
        # Web Application Workflow
        templates["web_application"] = ProjectWorkflow(
            project_id="web_app_template",
            project_name="Web Application Development",
            project_type="web_application",
            description="Complete web application with frontend, backend, and database",
            requirements=[
                "User authentication system",
                "Responsive web interface", 
                "RESTful API backend",
                "Database integration",
                "Security implementation",
                "Comprehensive testing",
                "Technical documentation"
            ],
            tasks=[
                WorkflowTask(
                    task_id="requirements_analysis",
                    description="Analyze project requirements and research technologies",
                    assigned_agent=AgentRole.RESEARCH_ANALYST,
                    stage=WorkflowStage.ANALYSIS,
                    priority="high",
                    dependencies=[],
                    estimated_duration="1-2 days",
                    deliverables=["Requirements analysis report", "Technology recommendations"],
                    context={"analysis_depth": "comprehensive", "focus_areas": ["security", "scalability"]}
                ),
                WorkflowTask(
                    task_id="system_architecture",
                    description="Design system architecture and technical specifications",
                    assigned_agent=AgentRole.SOLUTION_ARCHITECT,
                    stage=WorkflowStage.ARCHITECTURE,
                    priority="high",
                    dependencies=["requirements_analysis"],
                    estimated_duration="2-3 days",
                    deliverables=["System architecture diagram", "Database schema", "API specifications"],
                    context={"architecture_style": "microservices", "scalability_target": "medium"}
                ),
                WorkflowTask(
                    task_id="security_design",
                    description="Design security architecture and authentication system",
                    assigned_agent=AgentRole.SECURITY_SPECIALIST,
                    stage=WorkflowStage.ARCHITECTURE,
                    priority="high",
                    dependencies=["system_architecture"],
                    estimated_duration="1-2 days",
                    deliverables=["Security architecture", "Authentication flow", "Security checklist"],
                    context={"auth_method": "JWT", "security_level": "high"}
                ),
                WorkflowTask(
                    task_id="backend_implementation",
                    description="Implement backend API and database integration",
                    assigned_agent=AgentRole.CODE_IMPLEMENTER,
                    stage=WorkflowStage.IMPLEMENTATION,
                    priority="high",
                    dependencies=["system_architecture", "security_design"],
                    estimated_duration="5-7 days",
                    deliverables=["Backend API code", "Database models", "Authentication system"],
                    context={"framework": "FastAPI", "database": "PostgreSQL", "testing_required": True}
                ),
                WorkflowTask(
                    task_id="frontend_implementation",
                    description="Implement user interface and frontend application",
                    assigned_agent=AgentRole.CODE_IMPLEMENTER,
                    stage=WorkflowStage.IMPLEMENTATION,
                    priority="high",
                    dependencies=["system_architecture", "backend_implementation"],
                    estimated_duration="5-7 days",
                    deliverables=["Frontend application", "UI components", "Integration with backend"],
                    context={"framework": "React", "styling": "CSS3", "responsive": True}
                ),
                WorkflowTask(
                    task_id="quality_assurance",
                    description="Test implementation and validate quality standards",
                    assigned_agent=AgentRole.QUALITY_ASSURANCE,
                    stage=WorkflowStage.TESTING,
                    priority="medium",
                    dependencies=["backend_implementation", "frontend_implementation"],
                    estimated_duration="3-4 days",
                    deliverables=["Test suite", "Quality report", "Bug fixes"],
                    context={"test_types": ["unit", "integration", "e2e"], "coverage_target": "80%"}
                ),
                WorkflowTask(
                    task_id="deployment_setup",
                    description="Set up deployment infrastructure and CI/CD",
                    assigned_agent=AgentRole.INFRASTRUCTURE_SPECIALIST,
                    stage=WorkflowStage.DEPLOYMENT,
                    priority="medium",
                    dependencies=["quality_assurance"],
                    estimated_duration="2-3 days",
                    deliverables=["Deployment configuration", "CI/CD pipeline", "Infrastructure setup"],
                    context={"platform": "cloud", "containerization": "Docker", "automation": True}
                ),
                WorkflowTask(
                    task_id="documentation",
                    description="Create comprehensive technical documentation",
                    assigned_agent=AgentRole.TECHNICAL_WRITER,
                    stage=WorkflowStage.DOCUMENTATION,
                    priority="low",
                    dependencies=["deployment_setup"],
                    estimated_duration="2-3 days",
                    deliverables=["API documentation", "User guide", "Developer documentation"],
                    context={"documentation_types": ["api", "user", "developer"], "format": "markdown"}
                )
            ],
            estimated_timeline="3-4 weeks",
            success_criteria=[
                "Fully functional web application",
                "Secure authentication system",
                "Comprehensive test coverage",
                "Production-ready deployment",
                "Complete documentation"
            ]
        )
        
        # API Service Workflow
        templates["api_service"] = ProjectWorkflow(
            project_id="api_service_template",
            project_name="API Service Development",
            project_type="api_service",
            description="RESTful API service with comprehensive functionality",
            requirements=[
                "RESTful API design",
                "Database integration",
                "Authentication and authorization",
                "API documentation",
                "Performance optimization",
                "Security implementation"
            ],
            tasks=[
                WorkflowTask(
                    task_id="api_research",
                    description="Research API best practices and design patterns",
                    assigned_agent=AgentRole.RESEARCH_ANALYST,
                    stage=WorkflowStage.ANALYSIS,
                    priority="high",
                    dependencies=[],
                    estimated_duration="1 day",
                    deliverables=["API design guidelines", "Best practices report"],
                    context={"api_type": "REST", "domain": "general"}
                ),
                WorkflowTask(
                    task_id="api_architecture",
                    description="Design API architecture and specifications",
                    assigned_agent=AgentRole.SOLUTION_ARCHITECT,
                    stage=WorkflowStage.ARCHITECTURE,
                    priority="high",
                    dependencies=["api_research"],
                    estimated_duration="2 days",
                    deliverables=["API specifications", "Database design", "Architecture diagram"],
                    context={"api_standard": "OpenAPI", "versioning": "semantic"}
                ),
                WorkflowTask(
                    task_id="api_implementation",
                    description="Implement API endpoints and business logic",
                    assigned_agent=AgentRole.CODE_IMPLEMENTER,
                    stage=WorkflowStage.IMPLEMENTATION,
                    priority="high",
                    dependencies=["api_architecture"],
                    estimated_duration="4-5 days",
                    deliverables=["API implementation", "Database integration", "Error handling"],
                    context={"framework": "FastAPI", "database": "PostgreSQL", "validation": "Pydantic"}
                ),
                WorkflowTask(
                    task_id="api_testing",
                    description="Create comprehensive API tests",
                    assigned_agent=AgentRole.QUALITY_ASSURANCE,
                    stage=WorkflowStage.TESTING,
                    priority="high",
                    dependencies=["api_implementation"],
                    estimated_duration="2-3 days",
                    deliverables=["API test suite", "Performance tests", "Security tests"],
                    context={"test_framework": "pytest", "load_testing": True}
                ),
                WorkflowTask(
                    task_id="api_documentation",
                    description="Create API documentation and guides",
                    assigned_agent=AgentRole.TECHNICAL_WRITER,
                    stage=WorkflowStage.DOCUMENTATION,
                    priority="medium",
                    dependencies=["api_testing"],
                    estimated_duration="1-2 days",
                    deliverables=["API documentation", "Integration guide", "Examples"],
                    context={"doc_format": "OpenAPI", "examples": True}
                )
            ],
            estimated_timeline="2-3 weeks",
            success_criteria=[
                "Fully functional API service",
                "Comprehensive test coverage",
                "Complete API documentation",
                "Performance benchmarks met"
            ]
        )
        
        return templates
    
    def _initialize_agent_capabilities(self) -> Dict[AgentRole, Dict[str, Any]]:
        """Initialize agent capabilities and specializations"""
        
        return {
            AgentRole.PROJECT_ORCHESTRATOR: {
                "specializations": ["project_management", "coordination", "planning"],
                "workflow_stages": [WorkflowStage.ANALYSIS, WorkflowStage.REVIEW],
                "delegation_capability": True,
                "coordination_role": True
            },
            AgentRole.RESEARCH_ANALYST: {
                "specializations": ["technology_research", "code_analysis", "best_practices"],
                "workflow_stages": [WorkflowStage.ANALYSIS],
                "delegation_capability": False,
                "coordination_role": False
            },
            AgentRole.SOLUTION_ARCHITECT: {
                "specializations": ["system_design", "architecture", "technical_specifications"],
                "workflow_stages": [WorkflowStage.ARCHITECTURE],
                "delegation_capability": False,
                "coordination_role": False
            },
            AgentRole.CODE_IMPLEMENTER: {
                "specializations": ["full_stack_development", "coding", "integration"],
                "workflow_stages": [WorkflowStage.IMPLEMENTATION],
                "delegation_capability": False,
                "coordination_role": False
            },
            AgentRole.QUALITY_ASSURANCE: {
                "specializations": ["testing", "quality_validation", "code_review"],
                "workflow_stages": [WorkflowStage.TESTING, WorkflowStage.REVIEW],
                "delegation_capability": False,
                "coordination_role": False
            },
            AgentRole.TECHNICAL_WRITER: {
                "specializations": ["documentation", "technical_writing", "user_guides"],
                "workflow_stages": [WorkflowStage.DOCUMENTATION],
                "delegation_capability": False,
                "coordination_role": False
            },
            AgentRole.INFRASTRUCTURE_SPECIALIST: {
                "specializations": ["deployment", "devops", "infrastructure"],
                "workflow_stages": [WorkflowStage.DEPLOYMENT],
                "delegation_capability": False,
                "coordination_role": False
            },
            AgentRole.SECURITY_SPECIALIST: {
                "specializations": ["security_architecture", "authentication", "authorization"],
                "workflow_stages": [WorkflowStage.ARCHITECTURE, WorkflowStage.REVIEW],
                "delegation_capability": False,
                "coordination_role": False
            }
        }
    
    def get_workflow_template(self, project_type: str) -> Optional[ProjectWorkflow]:
        """Get a workflow template for a specific project type"""
        return self.workflow_templates.get(project_type)
    
    def create_custom_workflow(self, project_requirements: Dict[str, Any]) -> ProjectWorkflow:
        """Create a custom workflow based on project requirements"""
        
        project_type = project_requirements.get("type", "custom")
        
        # Start with a base template if available
        if project_type in self.workflow_templates:
            base_workflow = self.workflow_templates[project_type]
            # Customize based on specific requirements
            return self._customize_workflow(base_workflow, project_requirements)
        else:
            # Create from scratch
            return self._create_workflow_from_scratch(project_requirements)
    
    def _customize_workflow(self, base_workflow: ProjectWorkflow, requirements: Dict[str, Any]) -> ProjectWorkflow:
        """Customize an existing workflow template"""
        
        # Create a copy of the base workflow
        customized_workflow = ProjectWorkflow(
            project_id=requirements.get("project_id", "custom_project"),
            project_name=requirements.get("name", base_workflow.project_name),
            project_type=base_workflow.project_type,
            description=requirements.get("description", base_workflow.description),
            requirements=requirements.get("requirements", base_workflow.requirements),
            tasks=base_workflow.tasks.copy(),  # Will be modified
            estimated_timeline=base_workflow.estimated_timeline,
            success_criteria=requirements.get("success_criteria", base_workflow.success_criteria)
        )
        
        # Customize tasks based on requirements
        if "exclude_stages" in requirements:
            excluded_stages = [WorkflowStage(stage) for stage in requirements["exclude_stages"]]
            customized_workflow.tasks = [
                task for task in customized_workflow.tasks 
                if task.stage not in excluded_stages
            ]
        
        if "additional_requirements" in requirements:
            # Add additional tasks based on new requirements
            additional_tasks = self._generate_tasks_for_requirements(
                requirements["additional_requirements"]
            )
            customized_workflow.tasks.extend(additional_tasks)
        
        return customized_workflow
    
    def _create_workflow_from_scratch(self, requirements: Dict[str, Any]) -> ProjectWorkflow:
        """Create a completely custom workflow from requirements"""
        
        # This would implement logic to analyze requirements and generate appropriate tasks
        # For now, return a basic workflow structure
        
        return ProjectWorkflow(
            project_id=requirements.get("project_id", "custom_project"),
            project_name=requirements.get("name", "Custom Project"),
            project_type="custom",
            description=requirements.get("description", "Custom project workflow"),
            requirements=requirements.get("requirements", []),
            tasks=[],  # Would be generated based on requirements analysis
            estimated_timeline="TBD",
            success_criteria=requirements.get("success_criteria", [])
        )
    
    def _generate_tasks_for_requirements(self, requirements: List[str]) -> List[WorkflowTask]:
        """Generate workflow tasks based on specific requirements"""
        
        tasks = []
        task_counter = 1
        
        for requirement in requirements:
            req_lower = requirement.lower()
            
            if "security" in req_lower:
                tasks.append(WorkflowTask(
                    task_id=f"security_task_{task_counter}",
                    description=f"Implement security requirement: {requirement}",
                    assigned_agent=AgentRole.SECURITY_SPECIALIST,
                    stage=WorkflowStage.ARCHITECTURE,
                    priority="high",
                    dependencies=[],
                    estimated_duration="1-2 days",
                    deliverables=["Security implementation"],
                    context={"requirement": requirement}
                ))
            elif "documentation" in req_lower:
                tasks.append(WorkflowTask(
                    task_id=f"doc_task_{task_counter}",
                    description=f"Create documentation: {requirement}",
                    assigned_agent=AgentRole.TECHNICAL_WRITER,
                    stage=WorkflowStage.DOCUMENTATION,
                    priority="medium",
                    dependencies=[],
                    estimated_duration="1 day",
                    deliverables=["Documentation"],
                    context={"requirement": requirement}
                ))
            # Add more requirement-to-task mappings as needed
            
            task_counter += 1
        
        return tasks
    
    def get_delegation_sequence(self, workflow: ProjectWorkflow) -> List[Dict[str, Any]]:
        """Generate the sequence of agent delegations for a workflow"""
        
        delegations = []
        
        # Sort tasks by dependencies and priority
        sorted_tasks = self._sort_tasks_by_dependencies(workflow.tasks)
        
        for task in sorted_tasks:
            delegation = {
                "agent": task.assigned_agent.value,
                "task": task.description,
                "context": {
                    "task_id": task.task_id,
                    "stage": task.stage.value,
                    "priority": task.priority,
                    "dependencies": task.dependencies,
                    "deliverables": task.deliverables,
                    "estimated_duration": task.estimated_duration,
                    **task.context
                }
            }
            delegations.append(delegation)
        
        return delegations
    
    def _sort_tasks_by_dependencies(self, tasks: List[WorkflowTask]) -> List[WorkflowTask]:
        """Sort tasks based on their dependencies"""
        
        # Simple topological sort implementation
        sorted_tasks = []
        remaining_tasks = tasks.copy()
        
        while remaining_tasks:
            # Find tasks with no unresolved dependencies
            ready_tasks = [
                task for task in remaining_tasks
                if all(dep_id in [t.task_id for t in sorted_tasks] for dep_id in task.dependencies)
            ]
            
            if not ready_tasks:
                # If no tasks are ready, there might be circular dependencies
                # Add remaining tasks anyway (could be improved with better cycle detection)
                ready_tasks = remaining_tasks
            
            # Sort ready tasks by priority
            priority_order = {"high": 0, "medium": 1, "low": 2}
            ready_tasks.sort(key=lambda t: priority_order.get(t.priority, 3))
            
            # Add the first ready task to sorted list
            next_task = ready_tasks[0]
            sorted_tasks.append(next_task)
            remaining_tasks.remove(next_task)
        
        return sorted_tasks


if __name__ == "__main__":
    # Example usage and testing
    workflow_manager = MultiAgentWorkflowManager()
    
    print("Multi-Agent Workflow Manager")
    print("=" * 50)
    
    # Get web application workflow
    web_app_workflow = workflow_manager.get_workflow_template("web_application")
    if web_app_workflow:
        print(f"Web Application Workflow: {web_app_workflow.project_name}")
        print(f"Tasks: {len(web_app_workflow.tasks)}")
        print(f"Timeline: {web_app_workflow.estimated_timeline}")
        
        print("\nTask Sequence:")
        for i, task in enumerate(web_app_workflow.tasks, 1):
            print(f"{i}. {task.description} ({task.assigned_agent.value})")
        
        print("\nDelegation Sequence:")
        delegations = workflow_manager.get_delegation_sequence(web_app_workflow)
        for i, delegation in enumerate(delegations, 1):
            print(f"{i}. {delegation['agent']}: {delegation['task']}")
    
    print("\nAvailable Templates:")
    for template_name in workflow_manager.workflow_templates.keys():
        print(f"- {template_name}")