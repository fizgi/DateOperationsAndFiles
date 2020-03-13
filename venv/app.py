"""A study focuses on Date Arithmetic Operations

    author: Fatih IZGI
    date: 13-Mar-2020
    version: python 3.8.1
"""

from datetime import datetime, timedelta
from typing import Iterator, Tuple, IO
import prettytable


def date_arithmetic():
    """ Code segment demonstrating expected return values. """

    three_days_after_02272000 = datetime(2020, 2, 27) + timedelta(days=3)
    three_days_after_02272017 = datetime(2019, 2, 27) + timedelta(days=3)
    days_passed_01012017_10312017 = (datetime(2019, 9, 30) - datetime(2019, 2, 1)).days

    return three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017


def file_reader(path: str, fields: int, sep: str = ",", header: bool = False) -> Iterator[Tuple[str]]:
    """ a generator function to read field-separated text files
        and yield a tuple with all of the values from a single line """
    try:  # to open the file
        file: IO = open(path, "r")
    except FileNotFoundError:
        print(f"File {path} is not found")
    else:
        line_number: int = 0

        with file:  # close file after opening
            for line_number, line in enumerate(file, 1):
                row_fields = [field.strip("\n") for field in line.split("|")]
                row_field_count: int = len(row_fields)

                if row_field_count != fields:
                    raise ValueError(f"‘{path}’ has {len(line.split('|'))} fields "
                                     f"on line {line_number} but expected {fields}")

                if not header or line_number != 1:
                    yield tuple(row_fields)


class FileAnalyzer:
    """ a class that given a directory name, searches that directory
        for Python files and calculates a summary of the file """
    def __init__(self, directory):
        """ store the directory and files summary"""
        self.directory = directory # NOT mandatory!
        self.files_summary: Dict[str, Dict[str, int]] = dict()

        self.analyze_files() # summerize the python files data

    def analyze_files(self):
        """ Your docstring should go here for the description of the method."""
        pass # implement your code here

    def pretty_print(self):
        """ Your docstring should go here for the description of the method."""
        pass # implement your code here