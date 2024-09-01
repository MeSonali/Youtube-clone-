#!/bin/bash
############################################
# AUTHOR : FAREED SAYED
# DATE : 01 SEPTEMBER 2024 
# TO EXECUTE PROPER GITHUB 
############################################
@echo off
setlocal

:: Prompt for commit message
set /p commit_message="Enter commit message: "

:: Check if the user provided a commit message
if "%commit_message%"=="" (
    echo Commit message cannot be empty. Exiting.
    exit /b 1
)

:: Add changes to staging
git add .

:: Commit changes with user-provided message
git commit -m "%commit_message%"

:: Pull latest changes from origin main
git pull origin fareed

:: Add changes to staging again (in case there were updates from pull)
git add .

:: Commit changes again with user-provided message
git commit -m "%commit_message%"

:: Push changes to origin branch named fareed
git push origin fareed

endlocal

