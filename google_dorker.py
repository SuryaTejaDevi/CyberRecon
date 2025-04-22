import urllib.parse
import os
from datetime import datetime
from rich.console import Console

console = Console()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    console.print("\n[bold cyan]🔍 Google Dorking Tool 🔍[/bold cyan]")
    print("=" * 60)

def save_results(data):
    file_path = os.path.abspath("google_results.txt")
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(data + "\n")
        console.print(f"[+] Results saved to: {file_path}\n", style="green")
    except Exception as e:
        console.print(f"[!] Failed to save results: {e}", style="bold red")

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

def main():
    clear_screen()
    banner()
    domain = input("Enter the target domain (e.g., example.com): ").strip()
    print()
    google_dorking(domain)
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
