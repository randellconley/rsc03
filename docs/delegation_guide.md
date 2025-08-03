# OpenHands Agent Delegation Guide for RSC03

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
