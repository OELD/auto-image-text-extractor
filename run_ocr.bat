@echo off
if "%~1"=="" (
    echo Usage: run_ocr.bat [input_folder_path]
    pause
    exit /b 1
)
python src\main.py "%~1"
pause
