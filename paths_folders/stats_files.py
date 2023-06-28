"""
This python module implements names modification of files based on creation time of every file
"""
from pathlib import Path
from datetime import datetime

root_dir = Path("files2")
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        # The stats function gives information about a certain path
        stats =  path.stat()
        # the property after calling stats function can gives us the second of creation
        second_created = stats.st_ctime
        # converting to readable time for humans
        # transform the seconds from 1970 to actual date time
        date_created = datetime.fromtimestamp(second_created)
        # choose the format of the date string
        date_created_str = date_created.strftime("%Y-%m-%d_%H:%M")+ "_"+path.name
        new_filepath = path.with_name(date_created_str)
        path.rename(new_filepath)