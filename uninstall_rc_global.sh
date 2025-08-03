#!/bin/bash
# RC Global Uninstallation Script
# Removes the global symlink to the RSC03 RC command

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
GLOBAL_RC_PATH="/usr/local/bin/rc"

echo -e "${BLUE}🗑️  RSC03 Global RC Uninstallation${NC}"
echo "===================================="
echo ""

# Check if global RC exists
if [ ! -L "$GLOBAL_RC_PATH" ] && [ ! -f "$GLOBAL_RC_PATH" ]; then
    echo -e "${YELLOW}⚠️  No global RC installation found at $GLOBAL_RC_PATH${NC}"
    echo "   Nothing to uninstall"
    exit 0
fi

# Check if we need sudo
if [ -w "/usr/local/bin" ]; then
    SUDO_NEEDED=false
    echo -e "${GREEN}✅ Write access to /usr/local/bin detected${NC}"
else
    SUDO_NEEDED=true
    echo -e "${YELLOW}⚠️  Sudo required for /usr/local/bin access${NC}"
fi

# Show what will be removed
echo -e "${BLUE}🔍 Found global RC installation:${NC}"
ls -la "$GLOBAL_RC_PATH"
echo ""

# Confirm removal
echo -e "${YELLOW}❓ Remove global RC command? (y/N)${NC}"
read -r response
if [[ ! "$response" =~ ^[Yy]$ ]]; then
    echo -e "${BLUE}ℹ️  Uninstallation cancelled${NC}"
    exit 0
fi

# Remove global RC
echo -e "${BLUE}🗑️  Removing global RC command...${NC}"

if [ "$SUDO_NEEDED" = true ]; then
    echo -e "${YELLOW}   (Using sudo)${NC}"
    sudo rm -f "$GLOBAL_RC_PATH"
else
    rm -f "$GLOBAL_RC_PATH"
fi

# Verify removal
if [ ! -f "$GLOBAL_RC_PATH" ]; then
    echo -e "${GREEN}✅ Global RC command removed successfully${NC}"
    echo ""
    echo -e "${GREEN}🎉 UNINSTALLATION COMPLETE!${NC}"
    echo ""
    echo -e "${BLUE}Note:${NC} The RSC03 project files remain unchanged"
    echo "      Only the global symlink was removed"
else
    echo -e "${RED}❌ Error: Failed to remove global RC command${NC}"
    exit 1
fi