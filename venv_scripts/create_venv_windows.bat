@echo off
REM Check if Poetry is installed
poetry -V >nul 2>&1
IF ERRORLEVEL 1 (
    echo Poetry could not be found, installing...
    powershell -Command "Invoke-WebRequest -Uri https://install.python-poetry.org/windows-installer.py -UseBasicParsing | python -"
)

REM Configure Poetry to create virtual environments inside the project's root directory
poetry config virtualenvs.in-project true

REM Change directory to the new project
cd ..

REM Install dependencies (if any)
poetry install

echo Setup complete. Virtual environment is ready and dependencies are installed.