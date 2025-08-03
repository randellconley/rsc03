#!/usr/bin/env python3
"""
RC Command Global Installation Script
Sets up the RC command for global system access
"""

import os
import sys
import shutil
from pathlib import Path

def install_rc_globally():
    """Install RC command globally"""
    
    print("🚀 Installing RC Command Globally")
    print("=" * 50)
    
    # Get current RSC03 directory
    rsc03_dir = Path(__file__).parent.absolute()
    rc_script = rsc03_dir / "bin" / "rc"
    
    if not rc_script.exists():
        print(f"❌ RC script not found: {rc_script}")
        return False
    
    # Find a suitable global bin directory (prefer user-local)
    global_bin_dirs = [
        Path(os.path.expanduser("~/.local/bin")),
        Path("/home/ubuntu/.local/bin"),
        Path("/usr/local/bin")
    ]
    
    target_dir = None
    for bin_dir in global_bin_dirs:
        if bin_dir.exists() or bin_dir.parent.exists():
            target_dir = bin_dir
            break
    
    if not target_dir:
        print("❌ Could not find suitable global bin directory")
        return False
    
    # Create target directory if it doesn't exist
    target_dir.mkdir(parents=True, exist_ok=True)
    target_rc = target_dir / "rc"
    
    print(f"📍 RSC03 Directory: {rsc03_dir}")
    print(f"📍 Target Directory: {target_dir}")
    
    # Create a wrapper script that points to the RSC03 RC command
    wrapper_script = f'''#!/usr/bin/env python3
"""
RC - RSC03 Multi-Agent Command Interface (Global Wrapper)
This script provides global access to the RSC03 RC command
"""

import sys
import os
from pathlib import Path

# RSC03 installation directory
RSC03_DIR = Path("{rsc03_dir}")
RC_SCRIPT = RSC03_DIR / "bin" / "rc"

if not RC_SCRIPT.exists():
    print(f"❌ Error: RSC03 RC command not found at {{RC_SCRIPT}}")
    print(f"   Make sure RSC03 is properly installed at {{RSC03_DIR}}")
    sys.exit(1)

# Execute the RC command
import subprocess
try:
    result = subprocess.run([sys.executable, str(RC_SCRIPT)] + sys.argv[1:], 
                          cwd=str(RSC03_DIR))
    sys.exit(result.returncode)
except Exception as e:
    print(f"❌ Error executing RC command: {{e}}")
    sys.exit(1)
'''
    
    try:
        # Write the wrapper script
        with open(target_rc, 'w') as f:
            f.write(wrapper_script)
        
        # Make it executable
        target_rc.chmod(0o755)
        
        print(f"✅ RC command installed: {target_rc}")
        
        # Check if target directory is in PATH
        path_env = os.environ.get('PATH', '')
        if str(target_dir) not in path_env:
            print(f"⚠️  Warning: {target_dir} is not in your PATH")
            print(f"   Add this to your shell profile (.bashrc, .zshrc, etc.):")
            print(f"   export PATH=\"{target_dir}:$PATH\"")
        else:
            print(f"✅ {target_dir} is in your PATH")
        
        return True
        
    except Exception as e:
        print(f"❌ Error installing RC command: {e}")
        return False

def test_installation():
    """Test the RC command installation"""
    
    print("\n🧪 Testing RC Command Installation")
    print("=" * 50)
    
    try:
        import subprocess
        result = subprocess.run(['rc', '--version'], 
                              capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            print("✅ RC command is working!")
            print(f"   Output: {result.stdout.strip()}")
            return True
        else:
            print("❌ RC command test failed")
            print(f"   Error: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("❌ RC command not found in PATH")
        print("   Make sure the installation directory is in your PATH")
        return False
    except Exception as e:
        print(f"❌ Error testing RC command: {e}")
        return False

def main():
    """Main installation process"""
    
    print("RSC03 RC Command Global Installation")
    print("=" * 60)
    print("This will install the RC command globally on your system")
    print("so you can use 'rc' from any directory.")
    print()
    
    # Install the command
    if install_rc_globally():
        print("\n🎉 Installation completed successfully!")
        
        # Test the installation
        if test_installation():
            print("\n✅ RC command is ready to use!")
            print("\nTry these commands:")
            print("  rc --help                    # Show help")
            print("  rc --chat                    # Start interactive chat")
            print("  rc \"analyze this project\"    # Execute a request")
            print("  rc -plan \"build an API\"      # Generate a plan")
        else:
            print("\n⚠️  Installation completed but testing failed")
            print("   You may need to restart your shell or update your PATH")
    else:
        print("\n❌ Installation failed")
        sys.exit(1)

if __name__ == "__main__":
    main()