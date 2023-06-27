"""
This python module implements  simple pipeline for renaming files
"""
from pathlib import Path

root_dir = Path("files_excercises")
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        year_folder = path.parts[-3]
        parent_folder = path.parts[-2]
        new_filename = year_folder + '_'+ parent_folder + '_' + path.name
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)