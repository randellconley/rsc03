# RSC03 Production Setup Guide

## 🚀 Quick Start - Clone to Production

### Step 1: Run the Sync Script
```bash
cd /home/ubuntu/environment/workbench
./sync03.sh agents
```

This will:
- Clone RSC03 to `/home/ubuntu/environment/rsc03` (production directory)
- Sync the `agents` branch with all multi-model implementations
- Set up the production environment automatically

### Step 2: Verify Installation
```bash
cd /home/ubuntu/environment/rsc03
python -c "from utils.model_manager import ModelManager; print('✅ RSC03 Multi-Agent System Ready!')"
```

### Step 3: Test the System
```bash
cd /home/ubuntu/environment/rsc03
python start_team.py
```

### Step 4: Start Interactive CLI Chat
```bash
cd /home/ubuntu/environment/rsc03
python interactive_chat.py
```

This provides an interactive command-line interface where you can:
- Chat directly with any of the 8 specialized agents
- Switch between agents with `/switch <agent>`
- View usage costs and statistics
- Access structured workflows
- See chat history and agent status

## 📁 Directory Structure After Setup

```
/home/ubuntu/environment/
├── workbench/                    # Development environment
│   ├── rsc03/                   # Development version
│   └── sync03.sh                # Sync script
└── rsc03/                       # 🎯 PRODUCTION ENVIRONMENT
    ├── agents/                  # 8 specialized agents
    │   ├── project_orchestrator.py    # GPT-4
    │   ├── research_analyst.py        # Gemini Pro
    │   ├── solution_architect.py      # GPT-4
    │   ├── code_implementer.py        # DeepSeek Coder
    │   ├── quality_assurance.py       # Claude
    │   ├── technical_writer.py        # GPT-3.5-turbo
    │   ├── infrastructure_specialist.py # GPT-3.5-turbo
    │   └── security_specialist.py     # Claude
    ├── configs/                 # Configuration files
    │   ├── agent_configs.json
    │   └── model_config.json
    ├── utils/                   # Utility modules
    │   ├── __init__.py
    │   └── model_manager.py     # Multi-model management
    ├── workflows/               # Workflow definitions
    ├── examples/                # Example projects
    ├── docs/                    # Documentation
    └── start_team.py           # Main entry point
```

## 🔧 Environment Setup

### Required API Keys
Set these environment variables for full functionality:

```bash
# OpenAI (GPT-4, GPT-3.5-turbo)
export OPENAI_API_KEY="your-openai-api-key"

# Anthropic (Claude)
export ANTHROPIC_API_KEY="your-anthropic-api-key"

# Google (Gemini Pro)
export GEMINI_API_KEY="your-gemini-api-key"

# DeepSeek (DeepSeek Coder)
export DEEPSEEK_API_KEY="your-deepseek-api-key"
```

### Optional: Add to ~/.bashrc
```bash
echo 'export OPENAI_API_KEY="your-openai-api-key"' >> ~/.bashrc
echo 'export ANTHROPIC_API_KEY="your-anthropic-api-key"' >> ~/.bashrc
echo 'export GEMINI_API_KEY="your-gemini-api-key"' >> ~/.bashrc
echo 'export DEEPSEEK_API_KEY="your-deepseek-api-key"' >> ~/.bashrc
source ~/.bashrc
```

## 🎯 Using the Production System

### Basic Usage
```bash
cd /home/ubuntu/environment/rsc03

# Start the multi-agent system
python start_team.py

# Test specific agent
python -c "
from agents.project_orchestrator import ProjectOrchestrator
orchestrator = ProjectOrchestrator()
print('Project Orchestrator ready!')
"

# Check model assignments
python -c "
from utils.model_manager import get_model_for_agent
model, config = get_model_for_agent('research_analyst')
print(f'Research Analyst uses: {model}')
"
```

### Advanced Usage - Model Manager
```python
from utils.model_manager import ModelManager

# Initialize model manager
manager = ModelManager()

# Get usage statistics
summary = manager.get_usage_summary()
print(f"Total requests: {summary['total_requests']}")
print(f"Total cost: ${summary['total_cost']}")

# Get cost breakdown
breakdown = manager.get_cost_breakdown()
print("Cost by tier:", breakdown['by_tier'])
print("Cost by agent:", breakdown['by_agent'])
```

## 🔄 Ongoing Development Workflow

### Making Changes
1. **Work in development**: `/home/ubuntu/environment/workbench/rsc03`
2. **Test changes**: Verify functionality in workbench
3. **Sync to production**: Run `./sync03.sh agents`

### Sync Script Usage
```bash
# Sync current branch
cd /home/ubuntu/environment/workbench
./sync03.sh agents

# Sync different branch
./sync03.sh main
./sync03.sh feature-branch
```

## 🧠 Multi-Model Configuration

### Model Assignments
| Agent | Model | Reasoning |
|-------|-------|-----------|
| Project Orchestrator | GPT-4 | Complex coordination |
| Research Analyst | Gemini Pro | Research capabilities |
| Solution Architect | GPT-4 | System design |
| Code Implementer | DeepSeek Coder | Code generation |
| Quality Assurance | Claude | Detailed analysis |
| Technical Writer | GPT-3.5-turbo | Cost-effective docs |
| Infrastructure Specialist | GPT-3.5-turbo | Automation |
| Security Specialist | Claude | Security focus |

### Fallback Strategy
- Each agent has a fallback model configured
- Automatic failover on API errors or rate limits
- System-wide fallback to GPT-3.5-turbo

## 🔍 Troubleshooting

### Common Issues

#### 1. Import Errors
```bash
cd /home/ubuntu/environment/rsc03
export PYTHONPATH=$PYTHONPATH:$(pwd)
python -c "from utils.model_manager import ModelManager; print('OK')"
```

#### 2. API Key Issues
```bash
# Check if keys are set
echo $OPENAI_API_KEY
echo $ANTHROPIC_API_KEY

# Test model manager with available keys
python -c "
from utils.model_manager import ModelManager
manager = ModelManager()
model, config = manager.get_model_for_agent('project_orchestrator')
print(f'Using model: {model}')
"
```

#### 3. Git Issues
```bash
cd /home/ubuntu/environment/rsc03
git status
git branch -v
```

### Getting Help
- Check logs in model manager for API issues
- Review agent configurations in `configs/`
- Consult documentation in `docs/`

## 🎉 Success Indicators

You'll know the system is working when:

✅ **Sync completes successfully**: No errors from `./sync03.sh agents`
✅ **Model manager initializes**: No import errors
✅ **Agents load correctly**: All 8 agents can be imported
✅ **API connections work**: At least one model responds
✅ **Start script runs**: `python start_team.py` shows delegation sequence

## 📈 Next Steps

Once production is set up:

1. **Configure API keys** for all models
2. **Test each agent** individually
3. **Run example workflows** from `examples/`
4. **Monitor usage and costs** with model manager
5. **Customize agents** for your specific needs

---

*The RSC03 Multi-Agent System is now ready for production use with strategic multi-model AI distribution!*