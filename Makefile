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

.PHONY: help install migrate migrate-apply migrate-reset superuser load-fixtures run shell test clean format format-check reset status migrations-status
