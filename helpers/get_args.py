import argparse


def get_path() -> tuple:
    """
    Reads script arguments and returns it.
    :return: tuple: path to logs, path to report
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-ptl", "--path_to_logs", required=True, help="Path to logs")
    parser.add_argument("-ptr", "--path_to_report", required=True, help="Path to report")
    args = parser.parse_args()
    return args.path_to_logs, args.path_to_report
