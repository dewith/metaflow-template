# Variables
VENV_DIR = .env
REQ_FILE = requirements.txt

# Create virtual environment
env:
	python3 -m venv $(VENV_DIR)

# Activate virtual environment and install requirements
install: env
	. $(VENV_DIR)/bin/activate && pip install -r $(REQ_FILE)

# Clean virtual environment
clean:
	rm -rf $(VENV_DIR)

# Activate virtual environment and install pre-commit
hooks:
	. $(VENV_DIR)/bin/activate && pre-commit install

# Activate virtual environment and update pre-commit hooks
pre-commit: hooks
	. $(VENV_DIR)/bin/activate && pre-commit autoupdate

.PHONY: env install clean hooks pre-commit
