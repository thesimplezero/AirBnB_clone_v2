#!/bin/bash

# 0. Ask the user for an absolute path to the GitHub repository
read -p "Enter the absolute path to the GitHub repository: " repo_path

cd "$repo_path" || { echo "Error: Invalid repository path"; exit 1; }

# 1a. Check the state of the Git repo and perform necessary actions
git status

# 1b. Git pull and merge
echo "Pulling changes from remote repository..."
git pull --no-commit

# Check for merge conflicts
conflicts=$(git diff --name-only --diff-filter=U)

if [ -n "$conflicts" ]; then
  echo "Merge conflicts detected. Please resolve the conflicts in the following files:"
  echo "$conflicts"
  echo "After resolving the conflicts, stage the changes and run 'git commit'."
  exit 1
fi

# 2. Git add and commit
echo "Staging all changes..."
git add .

# Ask the user for a unique commit message for each file
echo "Enter a unique commit message for each file:"

for file in $(git diff --cached --name-only); do
  read -p "Commit message for $file: " commit_message
  git commit -m "$commit_message" -- "$file"
done

# 3. Add a timer that pushes the files after 10 seconds
echo "Pushing changes to the remote repository in 10 seconds..."
sleep 10
git push

echo "Changes have been pushed successfully."
