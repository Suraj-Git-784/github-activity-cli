import requests
import sys


def fetch_github_activity(username):

    url = f"https://api.github.com/users/{username}/events"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            activities = response.json()
            if not activities:
                print("No recent activity is found")

            else:
                display_activity(activities)
        else:
            print(f"Error: Unable to fetch data for {username}. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def display_activity(activities):
    for activity in activities:
        event_type = activities["type"]
        repo_name = activities["repo"]["name"]

        if event_type == "PushEvent":
            commit_count = len(activity['payload']['commits'])
            print(f"Pushed {commit_count} commit(s) to {repo_name}")
        elif event_type == 'IssueEvent' and activity['payload']['action'] == 'opened':
            print(f"Opened a new issue in {repo_name}")
        elif event_type == 'StarEvent':
            print(f"Starred {repo_name}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <Github username>")
        sys.exit(1)

    username = sys.argv[1]
    fetch_github_activity(username)

if __name__ == "__main__":
    main()
