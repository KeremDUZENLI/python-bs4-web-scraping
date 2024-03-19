import os


def setup_output_directory(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    os.chdir(folder_name)
