import os

def upload_to_gitlab(image_file, gitlab_url, repository):
    """
    Uploads an image to a GitLab repository after validation.
    Args:
    image_file (str): The path to the image file.
    gitlab_url (str): The URL of the GitLab instance.
    repository (str): The target repository in GitLab.
    """
    if validate_image(image_file):
        _upload(image_file)
    else:
        raise Exception("Invalid image file")

def validate_image(image_file):
    """TODO: Implement the actual image validation logic"""
    print(f"Validating {image_file}...")
    return True

def _upload(file): 
    pass