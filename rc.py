#!/usr/bin/env python3
"""
RC - RSC03 Command Runner
A minimal, context-aware command interface for the RSC03 multi-agent system.
Replaces RSC02's RC command with enhanced directory context and interactive chat integration.
"""

import sys
import os
import argparse
import time
import threading
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

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
        if os.getenv('RSC03_DEBUG', 'false').lower() == 'true':
            print(f"🔑 Loaded API keys from {env_file}")
    else:
        if os.getenv('RSC03_DEBUG', 'false').lower() == 'true':
            print(f"⚠️  No .env file found at {env_file}")
        
except ImportError:
    print("⚠️  python-dotenv not installed. Install with: pip install python-dotenv")

from rc_context import DirectoryContext
from rc_planner import PlanManager


class ProcessSpinner:
    """Interactive spinner that reflects real process status and stops if stalled"""
    
    def __init__(self, message: str = "Processing"):
        self.message = message
        self.is_active = False
        self.is_stalled = False
        self.last_activity = time.time()
        self.spinner_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        self.current_char = 0
        self.thread = None
        self.stall_timeout = 30  # 30 seconds before considering stalled
        
    def __enter__(self):
        self.start()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
        
    def start(self):
        """Start the spinner"""
        self.is_active = True
        self.is_stalled = False
        self.last_activity = time.time()
        self.thread = threading.Thread(target=self._spin, daemon=True)
        self.thread.start()
        
    def stop(self, final_message: str = None):
        """Stop the spinner"""
        self.is_active = False
        if self.thread:
            self.thread.join(timeout=1)
        
        # Clear the spinner line
        print('\r' + ' ' * (len(self.message) + 10), end='\r')
        
        if final_message:
            print(final_message)
            
    def update_activity(self, new_message: str = None):
        """Call this to indicate process is still active"""
        self.last_activity = time.time()
        self.is_stalled = False
        if new_message:
            self.message = new_message
            
    def _spin(self):
        """Internal spinner loop"""
        while self.is_active:
            # Check if process has stalled
            if time.time() - self.last_activity > self.stall_timeout:
                if not self.is_stalled:
                    self.is_stalled = True
                    print(f'\r⚠️  Process appears stalled (no activity for {self.stall_timeout}s)')
                    print(f'   Last activity: {datetime.fromtimestamp(self.last_activity).strftime("%H:%M:%S")}')
                time.sleep(1)
                continue
                
            # Show spinner
            spinner_char = self.spinner_chars[self.current_char]
            status = "🔄" if not self.is_stalled else "⏸️"
            print(f'\r{status} {spinner_char} {self.message}...', end='', flush=True)
            
            self.current_char = (self.current_char + 1) % len(self.spinner_chars)
            time.sleep(0.1)


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='RC - RSC03 Multi-Agent Command Interface',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  rc "analyze this codebase"              # Execute request with directory context
  rc --chat                               # Start interactive chat with context
  rc --chat "help me with this project"  # Start chat with initial message
  rc -plan "build a web application"     # Generate plan for review
  rc -v "debug this issue"               # Verbose mode for current command
  rc -d "troubleshoot the problem"       # Debug mode for current command
        """
    )
    
    # Planning system
    parser.add_argument(
        '-plan',
        metavar='REQUEST',
        help='Generate a plan for the given request (action-type prompts)'
    )
    
    # Chat mode
    parser.add_argument(
        '--chat',
        action='store_true',
        help='Start interactive chat mode with directory context'
    )
    
    # Debug and verbose modes
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output for current command only'
    )
    
    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        help='Enable debug output for current command only'
    )
    
    # Version info
    parser.add_argument(
        '--version',
        action='version',
        version='RC (RSC03) v1.0.0 - Multi-Agent Command Interface'
    )
    
    # Main request (positional arguments)
    parser.add_argument(
        'request',
        nargs='*',
        help='The request for the RSC03 multi-agent system'
    )
    
    return parser.parse_args()


def launch_interactive_chat(context: Dict[str, Any], initial_message: str = None, verbose: bool = False, debug: bool = False):
    """Launch interactive chat with directory context"""
    try:
        # Import the interactive chat system
        from interactive_chat import InteractiveAgentChat
        
        if verbose or debug:
            print(f"🚀 Launching interactive chat with context:")
            print(f"   Directory: {context['current_dir']}")
            print(f"   Project Type: {context['project_type']}")
            print(f"   RSC03 Relation: {context['rsc03_relation']}")
            if debug:
                print(f"   Full Context: {context}")
            print("=" * 60)
        
        # Create chat instance with context
        chat = InteractiveAgentChat(directory_context=context)
        
        # Start chat with optional initial message
        if initial_message:
            print(f"💬 Starting chat with: {initial_message}")
            chat.start_chat_with_message(initial_message)
        else:
            print("💬 Starting interactive chat...")
            chat.start_chat()
            
    except ImportError as e:
        print(f"❌ Error: Could not import interactive chat system: {e}")
        print("   Make sure you're running from the RSC03 directory")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error launching interactive chat: {e}")
        sys.exit(1)


def execute_request(request: str, context: Dict[str, Any], verbose: bool = False, debug: bool = False):
    """Execute a request with context awareness"""
    
    if verbose or debug:
        print(f"🎯 Executing request: {request}")
        print(f"📍 Context: {context['current_dir']} ({context['project_type']})")
        if debug:
            print(f"🔍 Full context: {context}")
        print("=" * 60)
    
    with ProcessSpinner("Analyzing request and context") as spinner:
        time.sleep(1)  # Simulate analysis
        spinner.update_activity("Determining appropriate agents")
        
        # Simulate some processing time
        time.sleep(2)
        spinner.update_activity("Coordinating multi-agent response")
        
        # For now, this is a placeholder - will be replaced with actual agent coordination
        time.sleep(1)
        spinner.update_activity("Generating response")
        
        # Simulate final processing
        time.sleep(1)
        
    print("✅ Request processed successfully!")
    print(f"📋 Response: This is a placeholder response for: '{request}'")
    print(f"📍 Context used: {context['current_dir']} ({context['project_type']})")
    
    if verbose:
        print("\n🔍 Verbose Details:")
        print(f"   - Request length: {len(request)} characters")
        print(f"   - Project files detected: {len(context.get('files_present', []))}")
        print(f"   - Git status: {context.get('git_info', {}).get('status', 'unknown')}")
    
    if debug:
        print("\n🐛 Debug Information:")
        print(f"   - Full context: {context}")
        print(f"   - Environment variables loaded: {bool(os.getenv('OPENAI_API_KEY'))}")
        print(f"   - Current working directory: {os.getcwd()}")


def main():
    """Main entry point for RC command"""
    args = parse_arguments()
    
    # Get directory context
    try:
        context_detector = DirectoryContext()
        context = context_detector.get_context()
    except Exception as e:
        print(f"❌ Error detecting directory context: {e}")
        context = {
            'current_dir': os.getcwd(),
            'project_type': 'unknown',
            'files_present': [],
            'git_info': {},
            'rsc03_relation': 'external'
        }
    
    # Handle different modes
    if args.chat:
        # Chat mode
        if args.request:
            # Chat with initial message
            initial_message = ' '.join(args.request)
            launch_interactive_chat(context, initial_message, args.verbose, args.debug)
        else:
            # Pure chat mode
            launch_interactive_chat(context, None, args.verbose, args.debug)
            
    elif args.plan:
        # Plan generation mode
        try:
            plan_manager = PlanManager()
            with ProcessSpinner("Generating plan") as spinner:
                spinner.update_activity("Analyzing request for planning")
                plan = plan_manager.generate_plan(args.plan, context)
                spinner.update_activity("Saving plan for review")
                plan_path = plan_manager.save_plan(plan, args.plan)
                
            print("✅ Plan generated successfully!")
            print(f"📋 Plan saved to: {plan_path}")
            print("\n" + "="*60)
            print(plan)
            print("="*60)
            
            # Ask for execution confirmation
            response = input("\n🤔 Would you like to execute this plan? (y/n): ").strip().lower()
            if response in ['y', 'yes']:
                print("🚀 Executing plan...")
                plan_manager.execute_plan(plan_path, context, args.verbose, args.debug)
            else:
                print("📝 Plan saved for later execution")
                
        except Exception as e:
            print(f"❌ Error in plan generation: {e}")
            if args.debug:
                import traceback
                traceback.print_exc()
            sys.exit(1)
            
    elif args.request:
        # Standard request execution
        request = ' '.join(args.request)
        execute_request(request, context, args.verbose, args.debug)
        
    else:
        # No arguments provided
        print("❌ Error: No command provided.")
        print("\nUsage examples:")
        print("  rc \"analyze this codebase\"              # Execute request")
        print("  rc chat                                 # Start interactive chat")
        print("  rc chat \"help me with this project\"    # Start chat with message")
        print("  rc -plan \"build a web application\"     # Generate plan")
        print("  rc -v \"debug this issue\"               # Verbose mode")
        print("  rc -d \"troubleshoot the problem\"       # Debug mode")
        print("\nUse 'rc --help' for more information.")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 RC command interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)