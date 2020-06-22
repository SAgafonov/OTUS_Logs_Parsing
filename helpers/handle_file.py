import os
import sys
from helpers.check_path import PathChecker


class FileHandler(PathChecker):

    def __init__(self):
        super().__init__()
        self.name_of_combined_logs = "Combined_logs.log"
        self.name_of_report = "Report.json"
        self.path_to_combined_logs = self.path_to_logs + os.sep + self.name_of_combined_logs
        self.path_to_save_report = self.path_to_report + os.sep + self.name_of_report

    def delete_file(self, path):
        """
        Delete file with combined logs if exists.
        :return:
        """
        if os.path.isfile(path):
            os.remove(path)

    def read_files(self):
        """
        Reads all files in a provided directory and combine data into one file;
        Change provided path from directory to path to the created file.
        :return:
        """
        self.delete_file(self.path_to_combined_logs)
        files_to_read = []
        if self.check_if_dir_is_not_empty() == 0:
            raise FileNotFoundError("Directory {} is empty".format(self.path_to_logs))

        all_sub_files = self.get_files_in_directory()
        # collect all files in sub-folder
        for name in all_sub_files:
            if self.check_if_file(path=self.path_to_logs + os.sep + name):
                files_to_read.append(name)
            else:
                continue

        for file_name in files_to_read:
            print(file_name)
            try:
                with open(self.path_to_logs + os.sep + file_name, "r") as file_read:
                    data = file_read.read()
                self.write_to_file(path=self.path_to_combined_logs, data=data, access_type="a")
            except IOError as e:
                print("I/O error({0}): {1}".format(e.errno, e.strerror))
            except:
                print("Unexpected error:", sys.exc_info()[0])

        self.path_to_logs = self.path_to_combined_logs

    def read_file(self):
        """
        Read from a provided file and return its data
        :return:
        """
        data = []
        if not self.check_if_file():
            self.read_files()

        try:
            with open(self.path_to_logs, "r") as file:
                data = file.readlines()
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        except:
            print("Unexpected error:", sys.exc_info()[0])
        return data

    def write_to_file(self, path, data, access_type):
        """
        Write data to a file.
        :param path: str: path to a file
        :param data: str: data to be saved
        :param access_type: str: 'w' - file will be created or overwritten; 'a' - append to a file
        :return:
        """
        try:
            with open(path, access_type) as file:
                file.write(data)
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        except:
            print("Unexpected error:", sys.exc_info()[0])
