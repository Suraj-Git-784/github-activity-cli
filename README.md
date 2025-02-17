GitHub Activity CLI
Description
This is a simple Command Line Interface (CLI) application that fetches and displays the recent activity of a specified GitHub user. It allows you to provide a GitHub username, fetch their recent activity, and display it directly in the terminal.

Features
Fetch recent activity of a GitHub user.
Display the activity in a readable format.
Handle errors such as invalid usernames or API failures.
Requirements
Python 3.x installed.
requests library (used to fetch data from GitHub's API).
Installation

Clone the repository:

git clone https://github.com/yourusername/github-activity-cli.git
Navigate into the project directory:

cd github-activity-cli
Install the required dependencies:

If you haven't installed requests yet, use the following command:

pip install requests
Usage
Fetch GitHub Activity
Run the script from the command line by passing the GitHub username as an argument:

python github_activity.py <username>
Example:

python github_activity.py kamranahmedse
Output
The application will display a list of recent activities of the user in a format like this:

Pushed 3 commits to kamranahmedse/developer-roadmap
Opened a new issue in kamranahmedse/developer-roadmap
Starred kamranahmedse/developer-roadmap
Error Handling
If an invalid username is provided or there is an issue with fetching data from the GitHub API, an error message will be shown.

Contributing
Feel free to open issues or submit pull requests to improve the functionality of the GitHub Activity CLI. Your contributions are welcome!

License
This project is open source and available under the MIT License.