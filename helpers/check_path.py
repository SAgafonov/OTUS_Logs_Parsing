import os
from helpers.get_args import get_path


class PathChecker:

    def __init__(self):
        self.path_to_logs, self.path_to_report = get_path()

    def check_if_file(self, path=None) -> bool:
        """
        Check if provided path is a path to a file.
        :return: bool
        """
        if path:
            return os.path.isfile(path)
        else:
            return os.path.isfile(self.path_to_logs)

    def check_if_dir_is_not_empty(self) -> int:
        """
        Check if provided directory is not empty.
        :return: int
        """
        return len(os.listdir(self.path_to_logs))

    def get_files_in_directory(self) -> list:
        """
        Returns names of files and subdirs in the given directory
        :return: list
        """
        return os.listdir(self.path_to_logs)
