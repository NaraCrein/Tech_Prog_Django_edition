#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import cloudinary as cloudinary


def main():
    """Run administrative tasks."""
    cloudinary.config(
        cloud_name = "ad-board-for-students",
        api_key = "383582569475818",
        api_secret = "_3gfpkuK7Ef3_ABhbI7ErxsCIAc"
    )
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
