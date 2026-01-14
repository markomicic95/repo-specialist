import requests
import getpass
import webbrowser # Added this to let you open links easily

def get_github_token():
    print("\n--- GITHUB AUTHENTICATION ---")
    print("1. Go to: https://github.com/settings/tokens")
    print("2. Click 'Generate new token' (classic)")
    print("3. Give it a name and check 'public_repo'")
    print("-" * 30)
    token = getpass.getpass("Paste Token (Characters will be hidden): ").strip()
    return token

# Broadened queries to ensure results exist
CATEGORIES = {
    "1": ("AI & Machine Learning", "machine-learning OR artificial-intelligence OR python-ai"),
    "2": ("Cybersecurity", "cybersecurity OR hacking-tool OR pentesting"),
    "3": ("Darkweb", "tor-network OR darkweb OR onion-services"),
    "4": ("Databases", "database OR mysql OR mongodb OR postgresql"),
    "5": ("Networking", "networking OR tcp-ip OR network-security")
}

def fetch_repos(query, token):
    # Using 'q' for general keywords + sorting by most recently updated
    url = f"https://api.github.com/search/repositories"
    params = {
        'q': query,
        'sort': 'updated',
        'order': 'desc',
        'per_page': 10
    }
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json().get('items', [])
        else:
            print(f"DEBUG: Status {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Connection Error: {e}")
        return None

def main():
    token = get_github_token()
    
    while True:
        print("\n📂 --- GITHUB REPO SPECIALIST --- 📂")
        for key, (name, _) in CATEGORIES.items():
            print(f"[{key}] {name}")
        print("[S] Custom Search")
        print("[Q] Quit")

        choice = input("\nSelect an option: ").strip().upper()
        
        if choice == "Q": break
        
        query = ""
        if choice == "S":
            query = input("Enter keyword: ")
        elif choice in CATEGORIES:
            query = CATEGORIES[choice][1]
        else:
            continue

        print(f"\nSearching for the latest '{query}' repos...")
        repos = fetch_repos(query, token)
        
        if repos:
            for i, repo in enumerate(repos, 1):
                print(f"{i}. ⭐ {repo['stargazers_count']} | {repo['full_name']}")
                print(f"   📝 {repo['description'][:100] if repo['description'] else 'No description'}...")
                print(f"   🔗 {repo['html_url']}\n")
            
            # Interactive Step: Open in browser
            action = input("Type a number (1-10) to open in browser, or 'M' for menu: ")
            if action.isdigit() and 1 <= int(action) <= len(repos):
                webbrowser.open(repos[int(action)-1]['html_url'])
        else:
            print("❌ No results. Try checking your internet or using a simpler keyword.")

if __name__ == "__main__":
    main()