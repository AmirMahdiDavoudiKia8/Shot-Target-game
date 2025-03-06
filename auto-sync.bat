cd "C:\path\to\MyProject"
git add .
git commit -m "Auto-update - %date% %time%" || exit /b
git push origin main