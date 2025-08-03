#!/usr/bin/env python3
"""
RSC03 Environment Setup Script
Helps users set up their .env file and dependencies
"""

import os
import sys
from pathlib import Path


def check_dependencies():
    """Check if required dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    missing_deps = []
    
    try:
        import dotenv
        print("  ✅ python-dotenv")
    except ImportError:
        missing_deps.append("python-dotenv")
        print("  ❌ python-dotenv")
    
    # Check for optional dependencies
    optional_deps = {
        'openai': 'OpenAI API client',
        'anthropic': 'Anthropic API client', 
        'google-generativeai': 'Google AI API client'
    }
    
    for dep, desc in optional_deps.items():
        try:
            __import__(dep.replace('-', '_'))
            print(f"  ✅ {dep} ({desc})")
        except ImportError:
            print(f"  ⚠️  {dep} ({desc}) - optional")
    
    if missing_deps:
        print(f"\n📦 Install missing dependencies:")
        print(f"pip install {' '.join(missing_deps)}")
        return False
    
    return True


def setup_env_file():
    """Help user set up .env file"""
    env_file = Path('.env')
    example_file = Path('.env.example')
    
    if env_file.exists():
        print(f"✅ .env file already exists at {env_file}")
        
        # Check if it has the required keys
        with open(env_file, 'r') as f:
            content = f.read()
            
        required_keys = ['OPENAI_API_KEY', 'ANTHROPIC_API_KEY', 'GEMINI_API_KEY', 'DEEPSEEK_API_KEY']
        missing_keys = []
        
        for key in required_keys:
            if key not in content or f"{key}=your-" in content:
                missing_keys.append(key)
        
        if missing_keys:
            print(f"⚠️  Missing or placeholder API keys: {', '.join(missing_keys)}")
            print(f"   Edit {env_file} to add your actual API keys")
        else:
            print("✅ All API keys appear to be configured")
            
        return True
    
    if not example_file.exists():
        print(f"❌ .env.example file not found")
        return False
    
    print(f"📝 Creating .env file from {example_file}...")
    
    # Copy example to .env
    with open(example_file, 'r') as f:
        content = f.read()
    
    with open(env_file, 'w') as f:
        f.write(content)
    
    print(f"✅ Created {env_file}")
    print(f"📝 Please edit {env_file} and add your actual API keys")
    
    return True


def test_model_manager():
    """Test if model manager can be imported and initialized"""
    print("\n🧪 Testing model manager...")
    
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from utils.model_manager import ModelManager, get_model_for_agent
        
        # Test initialization
        manager = ModelManager()
        print("  ✅ ModelManager initialized")
        
        # Test agent model assignment
        model, config = get_model_for_agent('project_orchestrator')
        print(f"  ✅ Agent model assignment working: {model}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def show_next_steps():
    """Show user what to do next"""
    print("\n" + "="*60)
    print("🎉 RSC03 SETUP COMPLETE!")
    print("="*60)
    
    print("\n📋 Next Steps:")
    print("1. Edit .env file with your actual API keys:")
    print("   nano .env")
    
    print("\n2. Test the system:")
    print("   python start_team.py")
    
    print("\n3. Start interactive chat:")
    print("   python interactive_chat.py")
    
    print("\n4. Available API keys to configure:")
    print("   • OPENAI_API_KEY     - For GPT-4, GPT-3.5-turbo")
    print("   • ANTHROPIC_API_KEY  - For Claude models")
    print("   • GEMINI_API_KEY     - For Gemini Pro")
    print("   • DEEPSEEK_API_KEY   - For DeepSeek Coder")
    
    print("\n💡 You can start with just one API key and add others later")
    print("   The system will use fallback models if some keys are missing")
    
    print("\n🔗 Get API keys from:")
    print("   • OpenAI: https://platform.openai.com/api-keys")
    print("   • Anthropic: https://console.anthropic.com/")
    print("   • Google AI: https://makersuite.google.com/app/apikey")
    print("   • DeepSeek: https://platform.deepseek.com/api_keys")


def main():
    """Main setup function"""
    print("🚀 RSC03 Multi-Agent System Setup")
    print("="*50)
    
    # Check current directory
    if not Path('utils/model_manager.py').exists():
        print("❌ Please run this script from the RSC03 project root directory")
        print("   The directory should contain utils/model_manager.py")
        sys.exit(1)
    
    print(f"📍 Project directory: {Path.cwd()}")
    
    # Check dependencies
    deps_ok = check_dependencies()
    
    # Setup .env file
    env_ok = setup_env_file()
    
    # Test model manager if dependencies are OK
    if deps_ok and env_ok:
        test_ok = test_model_manager()
    else:
        test_ok = False
    
    # Show results
    print("\n" + "="*50)
    print("📊 SETUP SUMMARY:")
    print("="*50)
    print(f"Dependencies: {'✅' if deps_ok else '❌'}")
    print(f"Environment:  {'✅' if env_ok else '❌'}")
    print(f"Model Manager: {'✅' if test_ok else '❌'}")
    
    if deps_ok and env_ok:
        show_next_steps()
    else:
        print("\n❌ Setup incomplete. Please resolve the issues above.")
        if not deps_ok:
            print("   Install missing dependencies first")
        if not env_ok:
            print("   Set up .env file")


if __name__ == "__main__":
    main()