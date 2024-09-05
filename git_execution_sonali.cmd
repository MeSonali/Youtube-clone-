@echo off
setlocal

:: Prompt for commit message
set /p commit_message="Enter commit message: "
if "%commit_message%"=="" (
    echo Commit message cannot be empty. Exiting.
    exit /b 1
)

git checkout sonali || git checkout -b sonali
git add .
git commit -m "%commit_message%"
git pull origin main 
git add . 
git commit -m "%commit_message%"
git push origin sonali

