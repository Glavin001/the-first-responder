import os
import subprocess
from git import Repo


def find_vulnerabilities(code):
    # Placeholder implementation
    return True


def get_latest_commit_author(file_path):
    result = subprocess.run(['git', 'blame', file_path, '-l', '-L', '1,1'], stdout=subprocess.PIPE)
    return result.stdout.decode().split()[1]


def process_repo(url):
    repo_path = '/Users/m/Repositories/the-first-responder/vulnerable_code'
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                code = f.read()

            vulnerabilities = find_vulnerabilities(code)
            if vulnerabilities:
                author = get_latest_commit_author(file_path)
                print(f"Vulnerabilities in {file_path} by {author}")


# Example usage
if __name__ == "__main__":
    process_repo('https://github.com/MikeKovetsky/vulnarable-code-demo')
