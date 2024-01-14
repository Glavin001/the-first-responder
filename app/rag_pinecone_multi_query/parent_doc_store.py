from pathlib import Path

from langchain.storage import LocalFileStore

# root_path = Path.cwd() / "data"  # can also be a path set by a string
root_path = Path.cwd() / "docs"  # can also be a path set by a string
store = LocalFileStore(root_path)
