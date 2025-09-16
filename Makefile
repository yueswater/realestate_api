# Makefile for realestate_crawler

.PHONY: run clean format lint check help

# Run FastAPI server with live reload
run:
	uvicorn app.main:app --reload --app-dir src

# Remove Python __pycache__ directories
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +

# Auto-format code: remove unused imports and sort imports
format:
	autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src
	isort src

# Lint code with flake8
lint:
	flake8 src

# Format and lint
check: format lint

# Show all available commands
help:
	@echo "Available commands:"
	@echo "  make run     - Start FastAPI server with reload"
	@echo "  make clean   - Remove __pycache__ directories"
	@echo "  make format  - Run autoflake and isort to auto-format code"
	@echo "  make lint    - Lint code using flake8"
	@echo "  make check   - Run both format and lint checks"
