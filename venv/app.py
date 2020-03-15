""" A study focuses on date operations and working with files (prettytable)

    author: Fatih IZGI
    date: 13-Mar-2020
    version: python 3.8.1
"""

from datetime import datetime, timedelta
from typing import Iterator, Tuple, IO, Dict
import os
from prettytable import PrettyTable


def date_arithmetic():
    """ Code segment demonstrating expected return values. """

    three_days_after_02272000 = datetime(2020, 2, 27) + timedelta(days=3)
    three_days_after_02272017 = datetime(2019, 2, 27) + timedelta(days=3)
    days_passed_01012017_10312017 = (datetime(2019, 9, 30) - datetime(2019, 2, 1)).days

    return three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017


def file_reader(path: str, fields: int, sep: str = ",", header: bool = False)\
        -> Iterator[Tuple[str]]:
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
    def __init__(self, directory: str):
        """ store the directory and files summary"""
        self.directory: str = directory # NOT mandatory!
        self.files_summary: Dict[str, Dict[str, int]] = dict()

        self.analyze_files() # summarize the python files data

    def analyze_files(self):
        """ analyze the file """
        for file in os.listdir(self.directory):
            if file.endswith(".py"):
                try:  # to open the file
                    py_file: IO = open(os.path.join(self.directory, file), "r")
                except FileNotFoundError:
                    print(f"File {py_file} is not found")
                else:
                    with py_file:  # close file after opening
                        class_count: int = 0
                        function_count: int = 0
                        line_count: int = 0
                        char_count: int = 0

                        for line in py_file:
                            if line.strip(" ").startswith("class "):
                                class_count += 1
                            elif line.strip(" ").startswith("def "):
                                function_count += 1

                            line_count += 1
                            char_count += len(line)

                        self.files_summary[str(os.path.join(self.directory, file))] = {
                            "class": class_count,
                            "function": function_count,
                            "line": line_count,
                            "char": char_count
                        }


    def pretty_print(self):
        """ prettify the data """
        table: PrettyTable = PrettyTable()
        table.field_names = ["File Name", "Classes", "Functions", "Lines", "Characters"]
        for key, value in self.files_summary.items():
            table.add_row([key] + [v for k, v in value.items()])

        print(table)
