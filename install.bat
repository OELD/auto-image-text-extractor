@echo off
echo Installing required Python packages...
pip install -r requirements.txt

echo.
echo Checking for Tesseract OCR...
where tesseract >nul 2>&1
if errorlevel 1 (
    echo Tesseract not found. Installing via winget...
    winget install --id=UB Mannheim.Tesseract-OCR -e --source winget
) else (
    echo Tesseract is already installed.
)
pause
