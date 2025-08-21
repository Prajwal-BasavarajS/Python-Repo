import requests
import time
import csv
from urllib.parse import urlparse, parse_qs
import os

# --- SECURITY WARNING ---
# Never hardcode your token. Use environment variables instead.
# Set an environment variable named 'GITHUB_TOKEN' with your PAT.
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# If the environment variable is not set, stop the script.
if not GITHUB_TOKEN:
    raise ValueError("GitHub token not found. Please set the 'GITHUB_TOKEN' environment variable.")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Changed filename for the new batch of data
csv_file = 'github_individuals_3000_batch3.csv'
# Added 'total_public_repos' to the fieldnames
fieldnames = ['full_repository_name', 'repository', 'owner', 'email', 'description', 'pull_requests', 'stars', 'forks', 'commits', 'total_public_repos']

# Updated date ranges to fetch a different set of repositories (from 2019-2020)
date_ranges = [
    ('2020-01-01', '2020-06-30'),
    ('2020-07-01', '2020-12-31'),
    ('2019-01-01', '2019-06-30'),
    ('2019-07-01', '2019-12-31')
]

def get_total_count_from_link_header(response):
    """
    Extracts the total number of items (like commits or PRs) from the 'Link' header
    by finding the page number of the 'last' link.
    """
    link_header = response.headers.get('Link')
    if not link_header:
        # If no 'Link' header, the number of items is on the first page
        try:
            return len(response.json())
        except (requests.exceptions.JSONDecodeError, AttributeError):
            return 0


    # Find the URL for the last page
    last_link = [link for link in link_header.split(',') if 'rel="last"' in link]
    if not last_link:
        # If there's a link header but no 'last' page, it means there's only one page
        try:
            return len(response.json())
        except (requests.exceptions.JSONDecodeError, AttributeError):
            return 0
        
    try:
        # Parse the URL to get the page number
        last_url = last_link[0].split(';')[0].strip().strip('<>')
        parsed_url = urlparse(last_url)
        query_params = parse_qs(parsed_url.query)
        # The total count is the page number of the last page, assuming per_page=1
        # This is a common trick for getting total counts efficiently.
        return int(query_params.get('page', [1])[0])
    except (IndexError, ValueError) as e:
        print(f"Could not parse last page number from link: {last_link}. Error: {e}")
        # Fallback to counting items on the current page
        try:
            return len(response.json())
        except (requests.exceptions.JSONDecodeError, AttributeError):
            return 0


with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    total_repos_saved = 0
    processed_repos = set() # Use a set to avoid duplicating repositories

    # Outer loop to break out of both inner loops when the limit is reached
    for start_date, end_date in date_ranges:
        if total_repos_saved >= 10:
            break
            
        for page in range(1, 11):  # GitHub allows up to 10 pages for a search (1000 results)
            if total_repos_saved >= 10:
                break

            print(f"Fetching page {page} for repositories created between {start_date} and {end_date}...")
            params = {
                'q': f'stars:>10 created:{start_date}..{end_date}',
                'sort': 'stars',
                'order': 'desc',
                'per_page': 100,
                'page': page
            }

            try:
                response = requests.get('https://api.github.com/search/repositories', headers=headers, params=params)
                response.raise_for_status() # This will raise an exception for 4xx or 5xx status codes
            except requests.exceptions.RequestException as e:
                print(f"Error fetching repositories: {e}")
                # You might hit a rate limit, so wait before continuing
                time.sleep(60) 
                continue

            repositories = response.json().get('items', [])
            if not repositories:
                # No more repositories in this date range
                break

            for repo in repositories:
                if total_repos_saved >= 10:
                    break

                full_name = repo['full_name']
                
                # Skip if we've already processed this repo
                if full_name in processed_repos:
                    continue

                # Skip if the owner is an Organization, we only want individual users
                if repo['owner']['type'] != 'User':
                    continue

                # --- Extracting Data ---
                owner, repository_name = full_name.split('/')
                description = repo.get('description', 'N/A') # Get the repository description
                stars = repo['stargazers_count']
                forks = repo['forks_count']

                # --- Get total public repositories for the owner ---
                total_public_repos = 'N/A' # Default value
                try:
                    user_url = f"https://api.github.com/users/{owner}"
                    user_resp = requests.get(user_url, headers=headers)
                    user_resp.raise_for_status()
                    user_data = user_resp.json()
                    total_public_repos = user_data.get('public_repos', 'N/A')
                except requests.exceptions.RequestException as e:
                    print(f"Could not fetch user data for {owner}: {e}")


                # Get total commits
                try:
                    commits_url = repo['commits_url'].replace('{/sha}', '')
                    # Set per_page=1 to make the request fast, we only need the header
                    commits_resp = requests.get(commits_url, headers=headers, params={'per_page': 1})
                    commits_resp.raise_for_status()
                    
                    # Get the email from the latest commit if available
                    latest_commit = commits_resp.json()
                    if latest_commit:
                        email = latest_commit[0]['commit']['author'].get('email', 'N/A')
                    else:
                        email = 'N/A'
                    
                    # Get total commit count from header
                    commits = get_total_count_from_link_header(commits_resp)
                except requests.exceptions.RequestException:
                    email = 'N/A'
                    commits = 0

                # Get total pull requests
                try:
                    pr_url = repo['pulls_url'].replace('{/number}', '')
                    pr_resp = requests.get(pr_url, headers=headers, params={'state': 'all', 'per_page': 1})
                    pr_resp.raise_for_status()
                    pull_requests = get_total_count_from_link_header(pr_resp)
                except requests.exceptions.RequestException:
                    pull_requests = 0

                # --- Save to CSV ---
                writer.writerow({
                    'full_repository_name': full_name,
                    'repository': repository_name,
                    'owner': owner,
                    'email': email,
                    'description': description,
                    'pull_requests': pull_requests,
                    'stars': stars,
                    'forks': forks,
                    'commits': commits,
                    'total_public_repos': total_public_repos
                })

                processed_repos.add(full_name)
                total_repos_saved += 1
                print(f"({total_repos_saved}/3000) Saved: {full_name} (Owner has {total_public_repos} public repos)")
                
                # Be respectful of the API rate limit
                time.sleep(1) 

            # Wait a moment before fetching the next page
            time.sleep(1)

print(f"\nData collection complete. Total individual user repositories collected: {total_repos_saved}")