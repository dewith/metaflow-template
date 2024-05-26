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

.PHONY: env install clean
