"""
Configuration settings for the Kingdom Foods Flask application.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Base configuration class."""
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'kingdomfoods_dev_key')
    
    # Flask-Mail configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587  # Keep at 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')

    # Update the CONTACT_EMAIL line to use your Gmail address for testing:
    CONTACT_EMAIL = os.environ.get('MAIL_USERNAME')  # For testing, use same as MAIL_USERNAME
    
    # Contact email recipient
    CONTACT_EMAIL = 'phamtuan301104@gmail.com'  # Email address info@kf-asia.com
    
    # Website details
    SITE_NAME = 'Kingdom Foods'
    SITE_DESCRIPTION = 'Authentic food products from Laos, Vietnam, and Thailand'
    
    # Default language
    DEFAULT_LANGUAGE = 'en'  # 'en' for English, 'vi' for Vietnamese
    
    # File upload configuration (for future use)
    UPLOAD_FOLDER = 'static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # For debugging - disable in production
    DEBUG_TB_INTERCEPT_REDIRECTS = False

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    """Testing configuration."""
    DEBUG = False
    TESTING = True
    WTF_CSRF_ENABLED = False  # Disable CSRF protection in tests

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False
    
    # In production, ensure SECRET_KEY is set in environment variables
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # Add any production-specific settings here
    
    # Security headers
    SECURITY_HEADERS = {
        'Content-Security-Policy': "default-src 'self'; script-src 'self' https://cdnjs.cloudflare.com; style-src 'self' https://cdnjs.cloudflare.com 'unsafe-inline'; font-src 'self' https://cdnjs.cloudflare.com; img-src 'self' data:",
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'SAMEORIGIN',
        'X-XSS-Protection': '1; mode=block',
    }

# Dictionary of available configurations
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def get_config():
    """Get the correct configuration based on environment."""
    config_name = os.environ.get('FLASK_ENV', 'default')
    return config.get(config_name, config['default'])