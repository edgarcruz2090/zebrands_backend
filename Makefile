# Django Development Makefile
# Usage: make <command>

# Variables
PYTHON = python
MANAGE = python manage.py
PROJECT_DIR = zebrands

# Default target
help:
	@echo "Available commands:"
	@echo "  help              - Show this help message"
	@echo "  install           - Install dependencies"
	@echo "  migrate           - Create migrations"
	@echo "  migrate-apply     - Apply migrations"
	@echo "  migrate-reset     - Reset database and apply migrations"
	@echo "  superuser         - Create superuser"
	@echo "  load-fixtures     - Load sample data fixtures"
	@echo "  run               - Run development server"
	@echo "  shell             - Open Django shell"
	@echo "  test              - Run tests"
	@echo "  clean             - Clean Python cache files"
	@echo "  format            - Format code with Black"
	@echo "  format-check      - Check code formatting without changing"
	@echo "  reset             - Full reset: clean, migrate, load fixtures"
	@echo "  docker-build      - Build Docker image"
	@echo "  docker-build-nc   - Build Docker image without cache"
	@echo "  docker-start      - Start Docker container in background"
	@echo "  docker-stop       - Stop Docker container"
	@echo "  docker-rebuild    - Rebuild and start Docker container"
	@echo "  docker-bash       - Access Docker container bash"
	@echo "  docker-shell      - Access Django shell in Docker"
	@echo "  docker-superuser  - Create superuser in Docker"
	@echo "  docker-loaddata   - Load fixtures in Docker container"

# Install dependencies
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Create migrations
migrate:
	@echo "Creating migrations..."
	cd $(PROJECT_DIR) && $(MANAGE) makemigrations

# Apply migrations
migrate-apply:
	@echo "Applying migrations..."
	cd $(PROJECT_DIR) && $(MANAGE) migrate

# Reset database and apply migrations
migrate-reset:
	@echo "Resetting database..."
	cd $(PROJECT_DIR) && rm -f db.sqlite3
	cd $(PROJECT_DIR) && $(MANAGE) migrate

# Create superuser
superuser:
	@echo "Creating superuser..."
	cd $(PROJECT_DIR) && $(MANAGE) createsuperuser

# Load fixtures
load-fixtures:
	@echo "Loading fixtures..."
	cd $(PROJECT_DIR) && $(MANAGE) loaddata fixtures/sample_data.json

# Run development server
run:
	@echo "Starting development server..."
	cd $(PROJECT_DIR) && $(MANAGE) runserver 8001

# Open Django shell
shell:
	@echo "Opening Django shell..."
	cd $(PROJECT_DIR) && $(MANAGE) shell

# Run tests
test:
	@echo "Running tests..."
	cd $(PROJECT_DIR) && $(MANAGE) test apps

# Clean Python cache files
clean:
	@echo "Cleaning cache files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +

# Format code with Black
format:
	@echo "Formatting code with Black..."
	cd $(PROJECT_DIR) && black .

# Check code formatting without changing
format-check:
	@echo "Checking code formatting with Black..."
	cd $(PROJECT_DIR) && black --check .

# Full reset: clean, migrate, load fixtures
reset: clean migrate-reset load-fixtures
	@echo "Full reset completed!"

# Check Django status
status:
	@echo "Checking Django status..."
	cd $(PROJECT_DIR) && $(MANAGE) check

# Show migrations status
migrations-status:
	@echo "Showing migrations status..."
	cd $(PROJECT_DIR) && $(MANAGE) showmigrations

# Docker commands
docker-build:
	@echo "Building Docker image..."
	docker compose -f docker-compose.yml build

docker-build-nc:
	@echo "Building Docker image without cache..."
	docker compose -f docker-compose.yml build --no-cache

docker-start:
	@echo "Starting Docker container in background..."
	docker compose -f docker-compose.yml up -d

docker-stop:
	@echo "Stopping Docker container..."
	docker compose -f docker-compose.yml stop

docker-rebuild:
	@echo "Rebuilding and starting Docker container..."
	docker compose -f docker-compose.yml up -d --build

docker-bash:
	@echo "Accessing Docker container bash..."
	docker compose -f docker-compose.yml exec app bash

docker-shell:
	@echo "Accessing Django shell in Docker..."
	docker compose -f docker-compose.yml exec app bash -c "cd zebrands && python manage.py shell"

docker-superuser:
	@echo "Creating superuser in Docker..."
	docker compose -f docker-compose.yml exec app bash -c "cd zebrands && python manage.py createsuperuser"

docker-loaddata:
	@echo "Loading fixtures in Docker container..."
	docker compose -f docker-compose.yml exec app bash -c "cd zebrands && python manage.py loaddata fixtures/sample_data.json"

.PHONY: help install migrate migrate-apply migrate-reset superuser load-fixtures run shell test clean format format-check reset status migrations-status docker-build docker-build-nc docker-start docker-stop docker-rebuild docker-bash docker-shell docker-superuser docker-loaddata
