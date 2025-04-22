import urllib.parse
import os
from datetime import datetime
from rich.console import Console

console = Console()

# Clear the terminal screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ASCII Banner
def banner():
    console.print("\n   (            )             )\ )                      ", style="bold cyan")
    console.print("   )\  (     ( /(    (   (   (()/(   (                  ", style="bold cyan")
    console.print("  (((_) )\ )  )\())  ))\  )(   /(_)) ))\  (   (    (     ", style="bold cyan")
    console.print("  )\___(()/( ((_)\  /((_)(()\ (_))  /((_) )\  )\   )\ )  ", style="bold cyan")
    console.print(" ((/ __|)(_))| |(_)(_))   ((_)| _ \(_))  ((_)((_) _(_/(  ", style="bold cyan")
    console.print("  | (__| || || '_ \/ -_) | '_||   // -_)/ _|/ _ \| ' \)) ", style="bold cyan")
    console.print("   \___|\_, ||_.__/\___| |_|  |_|_\\___|\__|\___/|_||_|  ", style="bold cyan")
    console.print("        |__/                                              ", style="bold cyan")
    print("=" * 60)

# Save results to a file
def save_results(data):
    file_path = os.path.abspath("results.txt")
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(data + "\n")
        console.print(f"[+] Results saved to: {file_path}\n", style="green")
    except Exception as e:
        console.print(f"[!] Failed to save results: {e}", style="bold red")

# Get current time
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Google Dorking function
def google_dorking(domain):
    timestamp = get_timestamp()
    queries = [
        f'inurl:admin site:{domain}',
        f'intitle:"index of" site:{domain}',
        f'filetype:pdf site:{domain}',
        f'inurl:login site:{domain}',
        f'site:{domain} ext:sql | ext:log | ext:conf'
    ]

    results = f"\n[*] Google Dorking Results for {domain}: [{timestamp}]\n"
    for query in queries:
        url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
        result_line = f"    [>] Open manually: {url}"
        print(result_line)
        results += result_line + "\n"

    save_results(results)
    return results

# GitHub Dorking function
def github_dorking(keyword):
    timestamp = get_timestamp()
    queries = [
        f'filename:.env {keyword}',
        f'filename:credentials.json {keyword}',
        f'filename:id_rsa {keyword}',
        f'filename:.git-credentials {keyword}',
        f'"aws_access_key_id" {keyword}',
        f'"DB_PASSWORD" {keyword}'
    ]

    results = f"\n[*] GitHub Dorking Results for {keyword}: [{timestamp}]\n"
    for query in queries:
        url = f"https://github.com/search?q={urllib.parse.quote(query)}&type=code"
        result_line = f"    [>] Open manually: {url}"
        print(result_line)
        results += result_line + "\n"

    save_results(results)
    return results

# Main menu
def main():
    while True:
        clear_screen()
        banner()
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("1. Google Dorking")
        print("2. GitHub Dorking")
        print("3. Both")
        print("4. Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == '1':
            domain = input("Enter the target domain (e.g., example.com): ").strip()
            print()
            google_dorking(domain)
        elif choice == '2':
            keyword = input("Enter target keyword or domain (e.g., amazon.com): ").strip()
            print()
            github_dorking(keyword)
        elif choice == '3':
            target = input("Enter target domain or keyword (e.g., example.com): ").strip()
            print("\n[*] Starting Google Dorking...\n")
            google_dorking(target)
            print("\n[*] Starting GitHub Dorking...\n")
            github_dorking(target)
        elif choice == '4':
            print("\nExiting... Stay safe, hacker!\n")
            break
        else:
            print("\n[!] Invalid option. Try again.")

        input("\nPress Enter to continue...")

# Run the tool
if __name__ == "__main__":
    main()
