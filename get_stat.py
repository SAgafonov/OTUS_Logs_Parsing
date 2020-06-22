from helpers.handle_file import FileHandler
from helpers.data_analyzer import DataAnalyzer

if __name__ == "__main__":
    da = DataAnalyzer()
    fh = FileHandler()

    fh.write_to_file(path=fh.path_to_save_report, data=da.report_maker(), access_type="w")
