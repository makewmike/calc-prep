#!/bin/bash
# Run this once after cloning or creating the repo locally.
# Replace the email below with your GitHub-verified email.

GITHUB_EMAIL="make.w.mike@gmail.com"
GITHUB_NAME="makewmike"

git init
git config user.email "$GITHUB_EMAIL"
git config user.name "$GITHUB_NAME"
git add .
git commit -m "init: calc-prep repo structure and calc-coach skill"
git branch -M main

echo ""
echo "✅ Repo initialized."
echo "Next: create a new public repo on GitHub named 'calc-prep', then run:"
echo "  git remote add origin https://github.com/makewmike/calc-prep.git"
echo "  git push -u origin main"
