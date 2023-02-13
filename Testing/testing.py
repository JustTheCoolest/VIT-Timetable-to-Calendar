import unittest
from Backend import calendar_generator


class TestCalendarGenerator(unittest.TestCase):

    def test_get_courses(self):
        with open('WinterSemester2023sample.txt') as text_source:
            self.assertEqual(
                calendar_generator.get_courses(text_source.read()),
                [{'code': 'BCSE102L',
                  'title': 'Structured and Object-Oriented Programming',
                  'slot': 'G1', 'venue': 'AB1-402', 'professor': 'ILAVENDHAN A'},
                 {'code': 'BCSE102P',
                  'title': 'Structured and Object-Oriented Programming Lab',
                  'slot': 'L29+L30+L37+L38', 'venue': 'AB1-404B',
                  'professor': 'ILAVENDHAN A'},
                 {'code': 'BECE102L',
                  'title': 'Digital Systems Design',
                  'slot': 'D1+TD1', 'venue': 'AB1-411',
                  'professor': 'J DIVYA'},
                 {'code': 'BECE102P',
                  'title': 'Digital Systems Design Lab',
                  'slot': 'L33+L34',
                  'venue': 'AB1-207',
                  'professor': 'J DIVYA'},
                 {'code': 'BENG101L',
                  'title': 'Technical English Communication',
                  'slot': 'C1',
                  'venue': 'AB1-411',
                  'professor': 'BHUVANESWARI R'},
                 {'code': 'BENG101P',
                  'title': 'Technical English Communication Lab',
                  'slot': 'L31+L32',
                  'venue': 'AB1-405',
                  'professor': 'BHUVANESWARI R'},
                 {'code': 'BMAT102L',
                  'title': 'Differential Equations and Transforms',
                  'slot': 'A1+TA1+TAA1',
                  'venue': 'AB1-402',
                  'professor': 'HANNAH GRACE G'},
                 {'code': 'BPHY101L',
                  'title': 'Engineering Physics',
                  'slot': 'E1+TE1',
                  'venue': 'AB1-402',
                  'professor': 'VINITHA G'},
                 {'code': 'BPHY101P',
                  'title': 'Engineering Physics Lab',
                  'slot': 'L55+L56',
                  'venue': 'AB1-202',
                  'professor': 'VINITHA G'},
                 {'code': 'BSTS101P',
                  'title': 'Quantitative Skills Practice I',
                  'slot': 'F1+TF1',
                  'venue': 'AB1-401',
                  'professor': 'ETHNUS (APT)'}]
            )


if __name__ == '__main__':
    unittest.main()
