# Step 1
- On terminal window:
cd "D:\TransferFromDellLaptop\C_Drive\Projects\ai-learning-journey"
# Use your REAL NAME (not username)
git config --global user.name "Your Full Name"
# Use the EMAIL associated with your GitHub account
git config --global user.email "your-github-email@example.com"

# Step2: Create a github repository
Go to github.com and sign in
Click the "+" button → "New repository"
Repository name: ai-learning-journey
Description: My 8-week journey learning AI, chatbots, and building AI agents
Make it Public (so you can showcase your progress!)
DO NOT initialize with README (we already have files)
Click "Create repository"

# Step 3: Connect local to Github
cd "D:\TransferFromDellLaptop\C_Drive\Projects\ai-learning-journey"
git add .
git commit -m "Initial commit: Setup AI learning journey with 8-week plan"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ai-learning-journey.git
git push -u origin main

Replace YOUR-USERNAME with your actual GitHub username

# Step 4:
Daily routine will be:
# After making changes
git add .
git commit -m "Week 1: Completed Python environment setup"
git push

- Use branches for experiments
# Create branch for new features
git checkout -b week3/rule-based-chatbot
# Work on your chatbot...
git add .
git commit -m "Add greeting functionality to chatbot"
git checkout main
git merge week3/rule-based-chatbot

