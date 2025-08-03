#!/usr/bin/env python3
"""
RSC03 Installation Setup Script
Setuptools configuration for global RC command installation
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Read requirements
requirements = []
requirements_file = this_directory / "requirements.txt"
if requirements_file.exists():
    requirements = requirements_file.read_text().strip().split('\n')
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

setup(
    name="rsc03-rc",
    version="1.0.0",
    description="RC - RSC03 Multi-Agent Command Interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="RSC03 Team",
    author_email="rsc03@example.com",
    url="https://github.com/randellconley/rsc03",
    packages=find_packages(),
    py_modules=[
        "rc",
        "rc_context", 
        "rc_planner",
        "interactive_chat"
    ],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'rc=rc:main',
        ],
    },
    scripts=['bin/rc'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Tools",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    package_data={
        '': ['*.md', '*.txt', '*.json', '*.yaml', '*.yml'],
    },
    zip_safe=False,
)