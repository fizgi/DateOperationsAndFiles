""" Test implementation class of the study
    which focuses on Date Arithmetic Operations

    author: Fatih IZGI
    date: 13-Mar-2020
    version: python 3.8.1
"""

import unittest
from datetime import datetime
from app import date_arithmetic, file_reader


class ListTest(unittest.TestCase):
    """ Test class of the methods """

    def test_date_arithmetic(self):
        """ testing date arithmetic """
        self.assertTrue(date_arithmetic() == (datetime(2020, 3, 1, 0, 0),
                                              datetime(2019, 3, 2, 0, 0),
                                              241))

    def test_file_reader(self):
        """ testing file reader """
        path = "student_majors.txt"

        result = [(cwid, name, major) for cwid, name, major in
                  file_reader(path, 3, sep='|', header=True)]  # if header is True
        expect: tuple(str, str, str) = [('123', 'Jin He', 'Computer Science'),  # dont show header
                                        ('234', 'Nanda Koka', 'Software Engineering'),
                                        ('345', 'Benji Cai', 'Software Engineering')]
        self.assertTrue(result == expect)

        result = [(cwid, name, major) for cwid, name, major in
                  file_reader(path, 3, sep='|', header=False)]  # if header is False
        expect: tuple(str, str, str) = [('CWID', 'Name', 'Major'),  # show the first row as well
                                        ('123', 'Jin He', 'Computer Science'),
                                        ('234', 'Nanda Koka', 'Software Engineering'),
                                        ('345', 'Benji Cai', 'Software Engineering')]
        self.assertTrue(result == expect)

        with self.assertRaises(ValueError):  # raise ValueError if field != row_field_count
            result = [(cwid, name, major) for cwid, name, major in
                      file_reader(path, 2, sep='|', header=True)]  # sent 2, should be 3

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
