import os

def get_path_to_photo(name_file):
    abs_path = os.path.abspath(__file__)
    dir_tests = os.path.dirname(abs_path)
    return os.path.join(dir_tests, "resources", name_file)