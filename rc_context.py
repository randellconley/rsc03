#!/usr/bin/env python3
"""
RC Context Detection System
Provides directory and project context awareness for the RC command.
"""

import os
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Optional


class DirectoryContext:
    """Detects and provides context about current directory and project"""
    
    def __init__(self):
        self.current_dir = Path.cwd()
        self.project_root = self._find_project_root()
        
    def get_context(self) -> Dict[str, Any]:
        """Get comprehensive context about current directory and project"""
        return {
            'current_dir': str(self.current_dir),
            'project_root': str(self.project_root) if self.project_root else None,
            'project_type': self.detect_project_type(),
            'files_present': self.get_key_files(),
            'git_info': self.get_git_info(),
            'rsc03_relation': self.detect_rsc03_relation(),
            'directory_summary': self.get_directory_summary(),
            'context_hints': self.generate_context_hints()
        }
    
    def _find_project_root(self) -> Optional[Path]:
        """Find the root of the current project by looking for common indicators"""
        current = self.current_dir
        
        # Look for common project root indicators
        root_indicators = [
            '.git',
            'package.json',
            'pyproject.toml',
            'requirements.txt',
            'Cargo.toml',
            'go.mod',
            'pom.xml',
            'build.gradle',
            'Makefile',
            'README.md'
        ]
        
        while current != current.parent:  # Stop at filesystem root
            for indicator in root_indicators:
                if (current / indicator).exists():
                    return current
            current = current.parent
            
        return None
    
    def detect_project_type(self) -> str:
        """Detect project type based on files present"""
        # Check current directory first, then project root
        check_dirs = [self.current_dir]
        if self.project_root and self.project_root != self.current_dir:
            check_dirs.append(self.project_root)
        
        for check_dir in check_dirs:
            # Python projects
            if any((check_dir / f).exists() for f in ['requirements.txt', 'pyproject.toml', 'setup.py', 'Pipfile']):
                if (check_dir / 'manage.py').exists():
                    return 'django'
                elif (check_dir / 'app.py').exists() or (check_dir / 'main.py').exists():
                    return 'python-app'
                elif any((check_dir / f).exists() for f in ['notebook.ipynb', 'analysis.py']):
                    return 'data-science'
                return 'python'
            
            # Node.js projects
            if (check_dir / 'package.json').exists():
                if (check_dir / 'next.config.js').exists():
                    return 'nextjs'
                elif (check_dir / 'angular.json').exists():
                    return 'angular'
                elif (check_dir / 'vue.config.js').exists():
                    return 'vue'
                elif (check_dir / 'src' / 'App.js').exists() or (check_dir / 'src' / 'App.tsx').exists():
                    return 'react'
                return 'nodejs'
            
            # Web projects
            if (check_dir / 'index.html').exists():
                if any((check_dir / f).exists() for f in ['style.css', 'styles.css', 'main.css']):
                    return 'web-static'
                return 'html'
            
            # Other project types
            if (check_dir / 'Cargo.toml').exists():
                return 'rust'
            if (check_dir / 'go.mod').exists():
                return 'go'
            if (check_dir / 'pom.xml').exists():
                return 'java-maven'
            if (check_dir / 'build.gradle').exists():
                return 'java-gradle'
            if (check_dir / 'Dockerfile').exists():
                return 'docker'
            
        return 'unknown'
    
    def get_key_files(self) -> List[str]:
        """Get list of key files in current directory"""
        key_extensions = {'.py', '.js', '.ts', '.jsx', '.tsx', '.html', '.css', '.md', '.json', '.yml', '.yaml'}
        key_filenames = {
            'README.md', 'package.json', 'requirements.txt', 'pyproject.toml', 
            'Dockerfile', 'docker-compose.yml', '.env', '.env.example',
            'Makefile', 'setup.py', 'main.py', 'app.py', 'index.html', 'index.js'
        }
        
        files = []
        try:
            for item in self.current_dir.iterdir():
                if item.is_file():
                    if item.name in key_filenames or item.suffix in key_extensions:
                        files.append(item.name)
        except PermissionError:
            pass
            
        return sorted(files)[:20]  # Limit to first 20 files
    
    def get_git_info(self) -> Dict[str, Any]:
        """Get git repository information if available"""
        git_info = {
            'is_repo': False,
            'branch': None,
            'status': None,
            'remote': None,
            'has_changes': False
        }
        
        try:
            # Check if we're in a git repository
            result = subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'], 
                                  capture_output=True, text=True, cwd=self.current_dir)
            if result.returncode == 0:
                git_info['is_repo'] = True
                
                # Get current branch
                result = subprocess.run(['git', 'branch', '--show-current'], 
                                      capture_output=True, text=True, cwd=self.current_dir)
                if result.returncode == 0:
                    git_info['branch'] = result.stdout.strip()
                
                # Get status
                result = subprocess.run(['git', 'status', '--porcelain'], 
                                      capture_output=True, text=True, cwd=self.current_dir)
                if result.returncode == 0:
                    if result.stdout.strip():
                        git_info['status'] = 'dirty'
                        git_info['has_changes'] = True
                    else:
                        git_info['status'] = 'clean'
                
                # Get remote origin
                result = subprocess.run(['git', 'remote', 'get-url', 'origin'], 
                                      capture_output=True, text=True, cwd=self.current_dir)
                if result.returncode == 0:
                    git_info['remote'] = result.stdout.strip()
                    
        except (subprocess.SubprocessError, FileNotFoundError):
            pass
            
        return git_info
    
    def detect_rsc03_relation(self) -> str:
        """Detect relationship to RSC03 project"""
        current_str = str(self.current_dir)
        
        # Check if we're in RSC03 development environment
        if '/workbench/rsc03' in current_str:
            return 'development'
        
        # Check if we're in RSC03 production environment
        if current_str.startswith('/home/ubuntu/environment/rsc03'):
            return 'production'
        
        # Check if we're in the broader workbench
        if '/workbench' in current_str:
            return 'workbench'
        
        # Check if we're in any RSC project
        if '/rsc0' in current_str:
            return 'rsc-project'
        
        return 'external'
    
    def get_directory_summary(self) -> Dict[str, Any]:
        """Get summary of directory contents"""
        summary = {
            'total_files': 0,
            'total_dirs': 0,
            'file_types': {},
            'size_mb': 0
        }
        
        try:
            for item in self.current_dir.iterdir():
                if item.is_file():
                    summary['total_files'] += 1
                    ext = item.suffix.lower()
                    summary['file_types'][ext] = summary['file_types'].get(ext, 0) + 1
                    try:
                        summary['size_mb'] += item.stat().st_size
                    except (OSError, PermissionError):
                        pass
                elif item.is_dir() and not item.name.startswith('.'):
                    summary['total_dirs'] += 1
                    
            summary['size_mb'] = round(summary['size_mb'] / (1024 * 1024), 2)
            
        except PermissionError:
            pass
            
        return summary
    
    def generate_context_hints(self) -> List[str]:
        """Generate helpful context hints for the AI agents"""
        hints = []
        
        # Project type hints
        project_type = self.detect_project_type()
        if project_type == 'python':
            hints.append("This appears to be a Python project - I can help with code analysis, debugging, and development")
        elif project_type == 'nodejs':
            hints.append("This appears to be a Node.js project - I can help with JavaScript/TypeScript development")
        elif project_type == 'web-static':
            hints.append("This appears to be a static web project - I can help with HTML, CSS, and frontend development")
        elif project_type == 'unknown':
            hints.append("Project type unclear - I'll analyze the context to provide appropriate assistance")
        
        # Git hints
        git_info = self.get_git_info()
        if git_info['is_repo']:
            if git_info['has_changes']:
                hints.append("Git repository with uncommitted changes - I can help review or commit changes")
            else:
                hints.append("Clean git repository - ready for new development work")
        
        # RSC03 relation hints
        rsc03_relation = self.detect_rsc03_relation()
        if rsc03_relation == 'development':
            hints.append("Working in RSC03 development environment - I can help with RSC03 development")
        elif rsc03_relation == 'production':
            hints.append("Working in RSC03 production environment - I'll be careful with changes")
        elif rsc03_relation == 'external':
            hints.append("Working in external project - I'll provide general assistance")
        
        # File-based hints
        files = self.get_key_files()
        if 'README.md' in files:
            hints.append("README.md present - I can analyze project documentation")
        if '.env' in files or '.env.example' in files:
            hints.append("Environment configuration detected - I can help with setup and configuration")
        if 'Dockerfile' in files:
            hints.append("Docker configuration present - I can help with containerization")
        
        return hints
    
    def format_context_summary(self) -> str:
        """Format context information for display"""
        context = self.get_context()
        
        summary = f"""
📍 Directory Context Summary:
   Current: {context['current_dir']}
   Project Type: {context['project_type']}
   RSC03 Relation: {context['rsc03_relation']}
   
📁 Directory Contents:
   Files: {context['directory_summary']['total_files']} ({context['directory_summary']['size_mb']} MB)
   Directories: {context['directory_summary']['total_dirs']}
   Key Files: {', '.join(context['files_present'][:5])}{'...' if len(context['files_present']) > 5 else ''}
"""
        
        if context['git_info']['is_repo']:
            summary += f"""
🔄 Git Information:
   Branch: {context['git_info']['branch']}
   Status: {context['git_info']['status']}
   Has Changes: {context['git_info']['has_changes']}
"""
        
        if context['context_hints']:
            summary += f"""
💡 Context Hints:
   • {chr(10).join(f'  • {hint}' for hint in context['context_hints'][:3])}
"""
        
        return summary.strip()


# Convenience function for quick context access
def get_current_context() -> Dict[str, Any]:
    """Get context for current directory"""
    return DirectoryContext().get_context()


if __name__ == "__main__":
    # Test the context detection
    context_detector = DirectoryContext()
    context = context_detector.get_context()
    
    print("🔍 Directory Context Detection Test")
    print("=" * 50)
    print(context_detector.format_context_summary())
    print("\n🔧 Full Context Data:")
    import json
    print(json.dumps(context, indent=2))