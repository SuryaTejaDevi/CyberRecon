import urllib.parse
import os
from datetime import datetime
from rich.console import Console

console = Console()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    console.print("\n[bold cyan]🐙 GitHub Dorking Tool 🐙[/bold cyan]")
    print("=" * 60)

def save_results(data):
    file_path = os.path.abspath("github_results.txt")
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(data + "\n")
        console.print(f"[+] Results saved to: {file_path}\n", style="green")
    except Exception as e:
        console.print(f"[!] Failed to save results: {e}", style="bold red")

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

def main():
    clear_screen()
    banner()
    keyword = input("Enter target keyword or domain (e.g., example.com): ").strip()
    print()
    github_dorking(keyword)
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
