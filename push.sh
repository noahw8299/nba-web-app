#!/bin/bash

# Add all of the modified files to the staging area
git add .

# Ask the user for the commit message
echo "Enter a commit message: "
read message

# Commit the changes with the message
git commit -m "$message"

# Push the code to the remote repository
git push origin main
