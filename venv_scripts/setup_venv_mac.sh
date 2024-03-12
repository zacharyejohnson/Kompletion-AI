
#!/bin/bash
# Check if Poetry is installed
if ! command -v poetry &> /dev/null
then
    echo "Poetry could not be found, installing..."
    curl -sSL https://install.python-poetry.org | python3 -
fi

# Configure Poetry to create virtual environments inside the project's root directory
poetry config virtualenvs.in-project true


# Change directory to the new project
cd ..

# Install dependencies (if any)
poetry install --no-root

echo "Setup complete. Virtual environment is ready and dependencies are installed."
