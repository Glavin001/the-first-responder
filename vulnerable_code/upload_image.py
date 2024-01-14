def upload_to_gitlab(image_file, gitlab_url, repository):
    if validate_image(image_file):
        _upload(image_file)
    else:
        raise Exception("Invalid image file")


def validate_image(image_file):
    """Image_file is a FILE"""
    """TODO: Implement the actual image validation logic"""
    return True


def _upload(file):
    """TODO: Implement the upload"""
    pass
