# 🚀 GitHub Repo Specialist

A specialized terminal-based tool built in Python to discover the latest and most relevant repositories on GitHub. This tool helps you hunt for high-quality code in specialized categories.

## ✨ Features

- **Secure Authentication**: Uses GitHub Personal Access Tokens (PAT) for reliable API access
- **Smart Category Filters**: Instant search for AI, Cybersecurity, Darkweb, Databases, and Networking
- **Real-Time Data**: Fetches the most recently updated repositories to ensure you find active projects via the GitHub Search API
- **Terminal-to-Browser**: Open any repository link in your default browser directly from the terminal

## 🛠️ Installation & Setup

### 1. Prepare the Environment
Run these commands in your terminal to set up the project:

```powershell
# Create project folder
mkdir repo-specialist && cd repo-specialist

# Set up virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install requests
