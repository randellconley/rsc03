"""
Code Implementer Agent for RSC03 OpenHands Multi-Agent System

This agent specializes in full-stack software development and implementation,
working within the OpenHands multi-agent framework to deliver high-quality code.

Role: Senior Software Developer
Goal: Implement solutions, write high-quality code, and integrate components
"""

from typing import Dict, Any, List
import json


class CodeImplementerAgent:
    """
    Code Implementer Agent using OpenHands capabilities.
    
    This agent specializes in writing clean, efficient, and well-documented code
    across multiple programming languages and frameworks, following industry
    best practices and security standards.
    """
    
    def __init__(self):
        self.agent_name = "code_implementer"
        self.role = "Senior Software Developer"
        self.model = "deepseek-coder"
        self.api_key = os.getenv('DEEPSEEK_API_KEY')
        self.specializations = [
            "full_stack_development",
            "python_development",
            "javascript_development",
            "api_development",
            "database_integration",
            "frontend_frameworks",
            "backend_frameworks",
            "code_optimization",
            "security_implementation"
        ]
        
        # Technology expertise
        self.technology_stack = {
            "backend": ["Python", "FastAPI", "Django", "Flask", "Node.js", "Express"],
            "frontend": ["React", "Vue.js", "Angular", "HTML5", "CSS3", "JavaScript", "TypeScript"],
            "databases": ["PostgreSQL", "MySQL", "SQLite", "MongoDB", "Redis"],
            "tools": ["Git", "Docker", "pytest", "Jest", "Webpack", "Vite"],
            "cloud": ["AWS", "Google Cloud", "Azure", "Heroku", "Vercel"]
        }
        
        # Code quality standards
        self.quality_standards = [
            "Clean code principles",
            "SOLID design patterns", 
            "Comprehensive error handling",
            "Security best practices",
            "Performance optimization",
            "Comprehensive testing",
            "Clear documentation",
            "Code maintainability"
        ]
    
    def get_system_prompt(self) -> str:
        """Get the specialized system prompt for this agent"""
        return f"""You are a {self.role} in an OpenHands multi-agent software development team.

ROLE & RESPONSIBILITIES:
- Implement high-quality, production-ready code
- Follow industry best practices and security standards
- Write clean, maintainable, and well-documented code
- Integrate multiple components and systems
- Optimize code for performance and scalability
- Implement comprehensive error handling and validation
- Create and maintain automated tests

TECHNOLOGY EXPERTISE:
{json.dumps(self.technology_stack, indent=2)}

CODE QUALITY STANDARDS:
{chr(10).join(f"- {standard}" for standard in self.quality_standards)}

IMPLEMENTATION APPROACH:
1. Analyze requirements and technical specifications thoroughly
2. Design clean, modular code architecture
3. Implement core functionality with proper error handling
4. Add comprehensive input validation and security measures
5. Write unit tests and integration tests
6. Document code with clear comments and docstrings
7. Optimize for performance and maintainability
8. Provide deployment and setup instructions

CODING BEST PRACTICES:
- Use meaningful variable and function names
- Follow language-specific style guides (PEP 8 for Python, etc.)
- Implement proper separation of concerns
- Use design patterns appropriately
- Handle edge cases and error conditions
- Write self-documenting code with clear comments
- Ensure code is testable and modular

SECURITY CONSIDERATIONS:
- Input validation and sanitization
- SQL injection prevention
- XSS protection
- Authentication and authorization
- Secure data handling
- Environment variable usage for secrets
- HTTPS and secure communication

When you receive implementation tasks, focus on delivering production-ready code that is secure, performant, and maintainable."""

    def get_implementation_templates(self) -> Dict[str, Dict[str, Any]]:
        """Get implementation templates for common project types"""
        
        return {
            "fastapi_backend": {
                "description": "FastAPI backend with authentication",
                "files": {
                    "main.py": "FastAPI application entry point",
                    "models.py": "Database models and schemas",
                    "auth.py": "Authentication and authorization",
                    "database.py": "Database connection and configuration",
                    "routers/": "API route handlers",
                    "tests/": "Unit and integration tests",
                    "requirements.txt": "Python dependencies"
                },
                "key_features": [
                    "JWT authentication",
                    "Password hashing",
                    "Database integration",
                    "API documentation",
                    "Error handling",
                    "Input validation",
                    "CORS configuration"
                ]
            },
            "react_frontend": {
                "description": "React frontend application",
                "files": {
                    "src/App.js": "Main application component",
                    "src/components/": "Reusable UI components",
                    "src/pages/": "Page components",
                    "src/hooks/": "Custom React hooks",
                    "src/services/": "API service functions",
                    "src/utils/": "Utility functions",
                    "src/styles/": "CSS and styling",
                    "package.json": "Node.js dependencies"
                },
                "key_features": [
                    "Component-based architecture",
                    "State management",
                    "API integration",
                    "Responsive design",
                    "Form validation",
                    "Error boundaries",
                    "Performance optimization"
                ]
            },
            "full_stack_app": {
                "description": "Complete full-stack application",
                "structure": {
                    "backend/": "FastAPI backend implementation",
                    "frontend/": "React frontend implementation", 
                    "database/": "Database schemas and migrations",
                    "tests/": "End-to-end and integration tests",
                    "docker/": "Docker configuration files",
                    "docs/": "Technical documentation"
                },
                "integration_points": [
                    "API communication",
                    "Authentication flow",
                    "Database operations",
                    "File uploads",
                    "Real-time features",
                    "Error handling"
                ]
            }
        }
    
    def get_code_examples(self) -> Dict[str, str]:
        """Get code examples for common implementation patterns"""
        
        return {
            "fastapi_auth": '''
# FastAPI Authentication Example
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta

app = FastAPI()
security = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=24)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )

@app.post("/login")
async def login(username: str, password: str):
    # Verify user credentials (implement your logic)
    if verify_user(username, password):
        token = create_access_token({"sub": username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
            ''',
            
            "react_component": '''
// React Component Example
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserProfile = ({ userId }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchUser = async () => {
            try {
                setLoading(true);
                const response = await axios.get(`/api/users/${userId}`);
                setUser(response.data);
            } catch (err) {
                setError(err.response?.data?.message || 'Failed to fetch user');
            } finally {
                setLoading(false);
            }
        };

        if (userId) {
            fetchUser();
        }
    }, [userId]);

    if (loading) return <div className="loading">Loading...</div>;
    if (error) return <div className="error">Error: {error}</div>;
    if (!user) return <div className="no-data">User not found</div>;

    return (
        <div className="user-profile">
            <h2>{user.name}</h2>
            <p>Email: {user.email}</p>
            <p>Joined: {new Date(user.created_at).toLocaleDateString()}</p>
        </div>
    );
};

export default UserProfile;
            ''',
            
            "database_model": '''
# SQLAlchemy Database Model Example
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from passlib.context import CryptContext

Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def set_password(self, password: str):
        self.hashed_password = pwd_context.hash(password)
    
    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.hashed_password)
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
            '''
        }
    
    def get_testing_examples(self) -> Dict[str, str]:
        """Get testing examples for different types of code"""
        
        return {
            "pytest_example": '''
# pytest Example for FastAPI
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users/",
        json={"username": "testuser", "email": "test@example.com", "password": "testpass123"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_login():
    # First create a user
    client.post("/users/", json={"username": "testuser", "email": "test@example.com", "password": "testpass123"})
    
    # Then test login
    response = client.post("/login", json={"username": "testuser", "password": "testpass123"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_protected_route():
    # Login to get token
    login_response = client.post("/login", json={"username": "testuser", "password": "testpass123"})
    token = login_response.json()["access_token"]
    
    # Use token to access protected route
    response = client.get("/protected", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
            ''',
            
            "jest_example": '''
// Jest Example for React
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import axios from 'axios';
import UserProfile from './UserProfile';

jest.mock('axios');
const mockedAxios = axios as jest.Mocked<typeof axios>;

describe('UserProfile', () => {
    beforeEach(() => {
        mockedAxios.get.mockClear();
    });

    test('renders loading state initially', () => {
        render(<UserProfile userId="1" />);
        expect(screen.getByText('Loading...')).toBeInTheDocument();
    });

    test('renders user data after successful fetch', async () => {
        const userData = {
            id: 1,
            name: 'John Doe',
            email: 'john@example.com',
            created_at: '2023-01-01T00:00:00Z'
        };

        mockedAxios.get.mockResolvedValueOnce({ data: userData });

        render(<UserProfile userId="1" />);

        await waitFor(() => {
            expect(screen.getByText('John Doe')).toBeInTheDocument();
            expect(screen.getByText('Email: john@example.com')).toBeInTheDocument();
        });
    });

    test('renders error state on fetch failure', async () => {
        mockedAxios.get.mockRejectedValueOnce({
            response: { data: { message: 'User not found' } }
        });

        render(<UserProfile userId="1" />);

        await waitFor(() => {
            expect(screen.getByText('Error: User not found')).toBeInTheDocument();
        });
    });
});
            '''
        }


def get_implementer_prompt_template() -> str:
    """Get the complete prompt template for the Code Implementer agent"""
    
    return """You are a Senior Software Developer in an OpenHands multi-agent software development team.

CORE RESPONSIBILITIES:
1. Implement high-quality, production-ready code
2. Follow industry best practices and security standards  
3. Write clean, maintainable, and well-documented code
4. Create comprehensive tests for all implementations
5. Optimize code for performance and scalability
6. Integrate multiple components and systems effectively

TECHNOLOGY EXPERTISE:
- Backend: Python (FastAPI, Django, Flask), Node.js, Express
- Frontend: React, Vue.js, Angular, HTML5, CSS3, JavaScript, TypeScript
- Databases: PostgreSQL, MySQL, SQLite, MongoDB, Redis
- Tools: Git, Docker, pytest, Jest, Webpack, Vite
- Cloud: AWS, Google Cloud, Azure, Heroku, Vercel

CODE QUALITY STANDARDS:
- Clean code principles and SOLID design patterns
- Comprehensive error handling and input validation
- Security best practices (authentication, authorization, data protection)
- Performance optimization and scalability considerations
- Comprehensive testing (unit, integration, end-to-end)
- Clear documentation and self-documenting code
- Maintainable and modular architecture

IMPLEMENTATION APPROACH:
1. Analyze requirements and technical specifications thoroughly
2. Design clean, modular code architecture
3. Implement core functionality with proper error handling
4. Add comprehensive input validation and security measures
5. Write unit tests and integration tests
6. Document code with clear comments and docstrings
7. Optimize for performance and maintainability
8. Provide deployment and setup instructions

SECURITY CONSIDERATIONS:
- Input validation and sanitization
- SQL injection and XSS prevention
- Secure authentication and authorization
- Proper secret management (environment variables)
- HTTPS and secure communication protocols
- Data encryption and secure storage

When you receive implementation tasks, deliver production-ready code that is secure, performant, maintainable, and thoroughly tested. Always include setup instructions and documentation."""


if __name__ == "__main__":
    # Example usage and testing
    implementer = CodeImplementerAgent()
    
    print("Code Implementer Agent")
    print("=" * 50)
    print(f"Role: {implementer.role}")
    print(f"Specializations: {implementer.specializations}")
    
    print("\nTechnology Stack:")
    print("-" * 30)
    for category, technologies in implementer.technology_stack.items():
        print(f"{category.title()}: {', '.join(technologies)}")
    
    print("\nImplementation Templates:")
    print("-" * 30)
    templates = implementer.get_implementation_templates()
    for template_name, template_info in templates.items():
        print(f"{template_name}: {template_info['description']}")
    
    print("\nSystem Prompt:")
    print("-" * 30)
    print(implementer.get_system_prompt())