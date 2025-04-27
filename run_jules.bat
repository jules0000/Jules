@echo off
echo Jules Language Runner
echo ===================
echo.

REM Get directory of batch file
cd /d "%~dp0"

if "%~1"=="" (
    echo No file specified. Enter interactive mode.
    python jules.py
) else (
    echo Running: %~1
    python jules.py "%~1"
)

echo.
pause 