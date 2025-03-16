class Config:
	SECRET_KEY = 'your-secret-key' # to create, run: openssl rand -base64 24

class DevelopmentConfig(Config):
	DEBUG = True
	ENV = 'development'