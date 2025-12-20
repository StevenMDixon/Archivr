import unittest
from domain.date_normalizer import DateNormalizer

class TestAddTwo(unittest.TestCase):

    def test_dates_in_file_names_are_normal(self):
        tests = [
            ("1993 sdfsd", "sdfsd 1993"),
            ("(1993) sdfsd", "sdfsd 1993"),
            ("[1993] sdfsd", "sdfsd 1993"),
            ("{1993} sdfsd", "sdfsd 1993"),
            ("1992 1993 sdfsd", "sdfsd 1992"),
            ("1992 sdfsd 1993 (2000)", "sdfsd 1992"),
            ("90s sdfsd", "sdfsd 1990"),
            ("[1990, 2000, 2001] sdfsd", "sdfsd 1990"),
            ("sdfsdf 1990", "sdfsdf 1990"),
            ("90's sdfsdf", "sdfsdf 1990"),
            ("(90s) sdfsdf", "sdfsdf 1990"),
            ("sdfsdf 90's", "sdfsdf 1990"),
            ("80's sdfsdf", "sdfsdf 1980"),
            ("80s sdfsdf", "sdfsdf 1980"),
            ("[1.90] sdfsdf", "sdfsdf 1990"),
            ("[1.1.90] sdfsdf", "sdfsdf 1990"),
            ("[1.1.1990] sdfsdf", "sdfsdf 1990"),
            ("(1.1.1990) sdfsdf", "sdfsdf 1990"),
            ("(1/1/1990) sdfsdf", "sdfsdf 1990"),
            ("(1/1/90) sdfsdf", "sdfsdf 1990"),
            ("(1-1-90) sdfsdf", "sdfsdf 1990")
        ]

        for input_file, expected_output in tests:
            self.assertEqual(DateNormalizer.normalize(input_file), expected_output)

if __name__ == '__main__':
    unittest.main()