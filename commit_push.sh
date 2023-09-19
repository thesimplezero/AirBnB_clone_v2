#!/bin/bash

# Function to add, commit, and push a file
function git_add_commit_push {
    local file_path=$1
    local commit_message=$2

    # Check if there are changes to commit
    if [[ -n $(git status -s "$file_path") ]]; then
        # Add the file
        git add "$file_path"
        echo "Added: $file_path"

        # Commit the changes with the provided message
        git commit -m "$commit_message"
        echo "Committed: $file_path - Message: $commit_message"

        # Push to the remote repository
        git push origin main
        echo "Pushed: $file_path"
    else
        echo "No changes to commit for: $file_path"
    fi
}

# Main function
function main {
    # Check if the repository is initialized and connected to a remote
    if [[ -n $(git remote -v) ]]; then
        # Scan files in the current directory and its subdirectories (excluding .git and the script itself)
        find . -type f -not -name "${0##*/}" -not -path "./.git/*" | while read -r file_path; do
            echo "Processing: $file_path"
            read -p "Enter a commit message for '$file_path': " commit_message
            git_add_commit_push "$file_path" "$commit_message"
            sleep 2
        done
    else
        echo "Git repository not initialized or not connected to a remote."
    fi
}

# Run the main function and capture errors
main 2>&1 | while IFS= read -r line; do
    echo "Error: $line"
done
