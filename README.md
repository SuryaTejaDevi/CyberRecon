# CyberRecon - Automated Google & GitHub Dorking Tool

## Overview
CyberRecon is an automated reconnaissance tool designed for ethical hacking and bug bounty hunting. It performs Google Dorking and GitHub Dorking to uncover sensitive information, misconfigurations, and data leaks.

### Features
- **Google Dorking:** Searches for exposed files like `.env`, `.log`, `.json`, and more.
- **GitHub Dorking:** Searches GitHub repositories for sensitive data like credentials, private keys, and configuration files.
- **Output:** Results are saved in `.txt`, `.json`, and `.md` formats.

### Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/CyberRecon.git
    cd CyberRecon
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set environment variables for the APIs:
    - **SERPAPI_KEY**: Get an API key from [SerpAPI](https://serpapi.com/).
    - **GITHUB_TOKEN**: Generate a personal access token from [GitHub](https://github.com/settings/tokens).

    ```bash
    export SERPAPI_KEY="your_serpapi_key"
    export GITHUB_TOKEN="your_github_token"
    ```

4. Run the script:
    ```bash
    python cyberrecon.py
    ```

### Disclaimer
This tool is intended for ethical use only. Ensure you have authorization to scan the targets and are following all relevant laws and guidelines.
