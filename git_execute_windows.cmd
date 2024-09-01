#!/bin/bash
############################################
# AUTHOR : FAREED SAYED
# DATE : 01 SEPTEMBER 2024 
# TO EXECUTE PROPER GITHUB 
############################################

# Prompt for commit message
echo "Enter commit message:"
read commit_message

# Add changes to staging
git add .

# Commit changes with user-provided message
git commit -m "$commit_message"

# Pull latest changes from origin main
git pull origin main

# Add changes to staging again (in case there were updates from pull)
git add .

# Commit changes again with user-provided message
git commit -m "$commit_message"

# Push changes to origin branch named fareed
git push origin fareed
