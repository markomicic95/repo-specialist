\# 🚀 GitHub Repo Specialist



A powerful terminal-based tool built in Python to discover the latest and most relevant repositories on GitHub. Whether you are looking for AI models, cybersecurity tools, or networking protocols, this specialist finds them and opens them for you.



---



\## 🛠️ Features

\* \*\*Live Authentication\*\*: Securely connect via GitHub Personal Access Token.

\* \*\*Smart Categories\*\*: Quick-access filters for AI, Cybersecurity, Darkweb, Databases, and Networking.

\* \*\*Real-Time Results\*\*: Fetches the most recently updated repositories (Active projects only!).

\* \*\*Browser Integration\*\*: Type a number to open the repository directly in your web browser.



---



\## ⚙️ Setup \& Installation



\### 1. Prepare the Environment

Ensure you have Python installed, then run:

```powershell

\# Create project folder

mkdir repo-specialist \&\& cd repo-specialist



\# Set up virtual environment

python -m venv venv

.\\venv\\Scripts\\Activate.ps1



\# Install dependencies

pip install requests





\### 2. Authentication

When you start the script, it will guide you to generate a GitHub Token. This ensures you aren't blocked by API rate limits.



---



\## 🚀 How to Use



Follow these steps to start hunting for repositories directly from your terminal:



\### 1. Launch the Tool

Run the script using the Python interpreter:

```powershell

python hunt.py





\### 2. Choose a Category

Once the menu appears, select a pre-defined category by typing its number, or press 'S' to perform a custom keyword search.



\### 3. Explore Results

The tool will display the top 10 results. For each repository, you will see:



Star Count: Popularity metric.



Short Description: What the project actually does.



Direct URL: The link to the source code.



\### 4. Open \& Learn

Type the number (1-10) of the repository you want to explore. The tool will automatically open the link in your default web browser.

