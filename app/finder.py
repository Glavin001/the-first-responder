import os
import subprocess

from langchain.text_splitter import RecursiveCharacterTextSplitter, Language


def find_vulnerabilities(code):
    # Placeholder implementation
    return True


def get_report(vul) -> str:
    return ""


def get_latest_commit_author(file_path):
    result = subprocess.run(['git', 'blame', file_path, '-l', '-L', '1,1'], stdout=subprocess.PIPE)
    return result.stdout.decode().split()[1]


def _split(file_path: str, code: str):
    author = get_latest_commit_author(file_path)

    python_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, chunk_size=200, chunk_overlap=0
    )
    documents = python_splitter.create_documents([code], metadatas=[{"author": author, "file_path": file_path}])
    print(documents)


def process_repo():
    reports = []
    repo_path = '/Users/m/Repositories/responder/the-first-responder/vulnerable_code'
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                code = f.read()

            vulnerability = find_vulnerabilities(code)
            if vulnerability:
                _split(file_path, code)
                reports.append(get_report(vulnerability))


# Example usage
if __name__ == "__main__":
    process_repo()
