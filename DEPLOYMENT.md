# RSC03 Deployment Guide

## Standalone Deployment

RSC03 can be deployed as a standalone project without requiring OpenHands to be installed in a specific location.

### Prerequisites

- Python 3.8+
- Standard OpenHands installation (any location)
- RSC03 project files

### Global Installation

To make the `rc` command available system-wide:

```bash
# From the RSC03 project directory
./install_rc_global.sh
```

This will:
- Create a symlink from `/usr/local/bin/rc` to the project's `bin/rc`
- Test the installation
- Show usage instructions
- Indicate if sudo is required

### Global Uninstallation

To remove the global `rc` command:

```bash
# From the RSC03 project directory
./uninstall_rc_global.sh
```

### Architecture

```
Deployment Structure:
├── /usr/local/bin/rc                    # Global symlink (created by installer)
│   └── → /path/to/rsc03/bin/rc          # Points to project binary
├── /path/to/rsc03/                      # Project directory (any location)
│   ├── bin/rc                           # Main RC binary
│   ├── install_rc_global.sh             # Global installer
│   ├── uninstall_rc_global.sh           # Global uninstaller
│   └── ...                              # Other project files
```

### Benefits

- ✅ **Portable**: Works with any OpenHands installation location
- ✅ **Standalone**: No hardcoded paths to OpenHands directories
- ✅ **Simple**: One command installation/uninstallation
- ✅ **Clean**: Uses symlinks (no file duplication)
- ✅ **Safe**: Automatic sudo detection and confirmation prompts

### Usage After Installation

```bash
# From anywhere on the system
rc --version                    # Check version
rc --help                       # Show help
rc "your request here"          # Execute command
```

### Deployment Notes

- **One Assistant Per Server**: Designed for single RSC project per server
- **Symlink Based**: Global command is a symlink to project binary
- **Sudo Handling**: Automatically detects and requests sudo when needed
- **Path Independent**: Works regardless of where RSC03 is installed