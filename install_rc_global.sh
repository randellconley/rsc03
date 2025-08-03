#!/bin/bash
# RC Global Installation Script
# Creates a global symlink to the RSC03 RC command for system-wide access

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RC_BINARY="$PROJECT_DIR/bin/rc"
GLOBAL_RC_PATH="/usr/local/bin/rc"

echo -e "${BLUE}🚀 RSC03 Global RC Installation${NC}"
echo "=================================="
echo ""

# Check if RC binary exists
if [ ! -f "$RC_BINARY" ]; then
    echo -e "${RED}❌ Error: RC binary not found at $RC_BINARY${NC}"
    echo "   Make sure you're running this from the RSC03 project directory"
    exit 1
fi

# Check if RC binary is executable
if [ ! -x "$RC_BINARY" ]; then
    echo -e "${YELLOW}⚠️  Making RC binary executable...${NC}"
    chmod +x "$RC_BINARY"
fi

# Test RC binary works
echo -e "${BLUE}🔍 Testing RC binary...${NC}"
if ! "$RC_BINARY" --version >/dev/null 2>&1; then
    echo -e "${RED}❌ Error: RC binary is not working properly${NC}"
    echo "   Please check the RSC03 installation"
    exit 1
fi

echo -e "${GREEN}✅ RC binary test passed${NC}"
echo ""

# Check if we need sudo
if [ -w "/usr/local/bin" ]; then
    SUDO_NEEDED=false
    echo -e "${GREEN}✅ Write access to /usr/local/bin detected${NC}"
else
    SUDO_NEEDED=true
    echo -e "${YELLOW}⚠️  Sudo required for /usr/local/bin access${NC}"
fi

# Remove existing global RC if it exists
if [ -L "$GLOBAL_RC_PATH" ] || [ -f "$GLOBAL_RC_PATH" ]; then
    echo -e "${YELLOW}⚠️  Existing RC command found at $GLOBAL_RC_PATH${NC}"
    echo "   Removing existing installation..."
    
    if [ "$SUDO_NEEDED" = true ]; then
        sudo rm -f "$GLOBAL_RC_PATH"
    else
        rm -f "$GLOBAL_RC_PATH"
    fi
    
    echo -e "${GREEN}✅ Existing RC command removed${NC}"
fi

# Create symlink
echo -e "${BLUE}🔗 Creating global symlink...${NC}"
echo "   From: $GLOBAL_RC_PATH"
echo "   To:   $RC_BINARY"

if [ "$SUDO_NEEDED" = true ]; then
    echo -e "${YELLOW}   (Using sudo)${NC}"
    sudo ln -s "$RC_BINARY" "$GLOBAL_RC_PATH"
else
    ln -s "$RC_BINARY" "$GLOBAL_RC_PATH"
fi

# Verify installation
echo ""
echo -e "${BLUE}🔍 Verifying installation...${NC}"

if [ -L "$GLOBAL_RC_PATH" ] && [ -x "$GLOBAL_RC_PATH" ]; then
    echo -e "${GREEN}✅ Global RC symlink created successfully${NC}"
    
    # Test global command
    if rc --version >/dev/null 2>&1; then
        echo -e "${GREEN}✅ Global RC command working${NC}"
        echo ""
        echo -e "${GREEN}🎉 INSTALLATION COMPLETE!${NC}"
        echo ""
        echo -e "${BLUE}Usage:${NC}"
        echo "   rc --version                    # Check version"
        echo "   rc --help                       # Show help"
        echo "   rc \"your request here\"          # Execute command"
        echo ""
        echo -e "${BLUE}Installation Details:${NC}"
        echo "   Global Command: $GLOBAL_RC_PATH"
        echo "   Project Binary: $RC_BINARY"
        echo "   Sudo Required: $SUDO_NEEDED"
        echo ""
        
        # Show version
        echo -e "${BLUE}Installed Version:${NC}"
        rc --version
        
    else
        echo -e "${RED}❌ Error: Global RC command not working${NC}"
        echo "   The symlink was created but the command is not accessible"
        echo "   Check your PATH environment variable"
        exit 1
    fi
else
    echo -e "${RED}❌ Error: Failed to create global symlink${NC}"
    exit 1
fi