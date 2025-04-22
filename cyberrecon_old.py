import argparse
import os
import requests

# Function to load dorks from a given file path
def load_dorks(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: Dork list not found: {file_path}")
        exit(1)

# Function to run GitHub dorking
def github_dorking(token, dorks):
    print("Running GitHub dorking...")
    headers = {
        'Authorization': f'token {token}'
    }

    # Placeholder for your GitHub dorking code
    for dork in dorks:
        search_query = dork.strip()
        url = f"https://api.github.com/search/code?q={search_query}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"Found {len(response.json()['items'])} results for dork: {search_query}")
        else:
            print(f"Error searching GitHub with dork: {search_query}. Status Code: {response.status_code}")
    print("GitHub dorking completed.")

# Main function to parse arguments and run the appropriate tasks
def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="CyberRecon: Automated GitHub & Google Dorking Tool")
    parser.add_argument('--github', action='store_true', help="Run GitHub Dorking")
    parser.add_argument('--google', action='store_true', help="Run Google Dorking")
    parser.add_argument('--token', type=str, help="GitHub Personal Access Token", required=False)
    args = parser.parse_args()

    # Absolute path to the github_dorks.txt file
    github_dorks_path = "/home/kali/CyberRecon/CyberRecon/data/github_dorks.txt"
    
    # Load the GitHub dorks from the file
    dorks = load_dorks(github_dorks_path)

    # If the --github flag is set, run GitHub dorking
    if args.github:
        if args.token:
            print("GitHub token provided, proceeding with dorking...")
            github_dorking(args.token, dorks)
        else:
            print("Error: GitHub token is required for GitHub dorking.")
            exit(1)

    # Add similar logic here for Google Dorking if you need it
    if args.google:
        print("Google dorking functionality will go here.")
        # Google dorking logic will be implemented later

if __name__ == "__main__":
    main()
