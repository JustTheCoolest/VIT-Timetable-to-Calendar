import unittest
from Backend import calendar_generator


class TestCalendarGenerator(unittest.TestCase):

    def test_get_courses(self):
        with open('WinterSemester2023sample.txt') as text_source:
            self.assertEqual(
                calendar_generator.get_courses(text_source.read()),
                {
                 'BCHY102N': {'LTPJC': (0.0, 0.0, 0.0, 0.0, 2.0),
                              'class_code': 'CH2022232300816',
                              'professor': 'ILAIYARAJA PERUMAL',
                              'slot': 'NIL',
                              'title': 'Environmental Sciences',
                              'venue': 'NIL'},
                 'BCSE102L': {'LTPJC': (2.0, 0.0, 0.0, 0.0, 2.0),
                              'class_code': 'CH2022232300536',
                              'professor': 'ILAVENDHAN A',
                              'slot': 'G1',
                              'title': 'Structured and Object-Oriented Programming',
                              'venue': 'AB1-402'},
                 'BCSE102P': {'LTPJC': (0.0, 0.0, 4.0, 0.0, 2.0),
                              'class_code': 'CH2022232300674',
                              'professor': 'ILAVENDHAN A',
                              'slot': 'L29+L30+L37+L38',
                              'title': 'Structured and Object-Oriented Programming Lab',
                              'venue': 'AB1-404B'},
                 'BECE102L': {'LTPJC': (3.0, 0.0, 0.0, 0.0, 3.0),
                              'class_code': 'CH2022232300133',
                              'professor': 'J DIVYA',
                              'slot': 'D1+TD1',
                              'title': 'Digital Systems Design',
                              'venue': 'AB1-411'},
                 'BECE102P': {'LTPJC': (0.0, 0.0, 2.0, 0.0, 1.0),
                              'class_code': 'CH2022232300183',
                              'professor': 'J DIVYA',
                              'slot': 'L33+L34',
                              'title': 'Digital Systems Design Lab',
                              'venue': 'AB1-207'},
                 'BENG101L': {'LTPJC': (2.0, 0.0, 0.0, 0.0, 2.0),
                              'class_code': 'CH2022232300363',
                              'professor': 'BHUVANESWARI R',
                              'slot': 'C1',
                              'title': 'Technical English Communication',
                              'venue': 'AB1-411'},
                 'BENG101P': {'LTPJC': (0.0, 0.0, 2.0, 0.0, 1.0),
                              'class_code': 'CH2022232300364',
                              'professor': 'BHUVANESWARI R',
                              'slot': 'L31+L32',
                              'title': 'Technical English Communication Lab',
                              'venue': 'AB1-405'},
                 'BMAT102L': {'LTPJC': (3.0, 1.0, 0.0, 0.0, 4.0),
                              'class_code': 'CH2022232300430',
                              'professor': 'HANNAH GRACE G',
                              'slot': 'A1+TA1+TAA1',
                              'title': 'Differential Equations and Transforms',
                              'venue': 'AB1-402'},
                 'BPHY101L': {'LTPJC': (3.0, 0.0, 0.0, 0.0, 3.0),
                              'class_code': 'CH2022232300020',
                              'professor': 'VINITHA G',
                              'slot': 'E1+TE1',
                              'title': 'Engineering Physics',
                              'venue': 'AB1-402'},
                 'BPHY101P': {'LTPJC': (0.0, 0.0, 2.0, 0.0, 1.0),
                              'class_code': 'CH2022232300070',
                              'professor': 'VINITHA G',
                              'slot': 'L55+L56',
                              'title': 'Engineering Physics Lab',
                              'venue': 'AB1-202'},
                 'BSTS101P': {'LTPJC': (0.0, 0.0, 3.0, 0.0, 1.5),
                              'class_code': 'CH2022232300689',
                              'professor': 'ETHNUS (APT)',
                              'slot': 'F1+TF1',
                              'title': 'Quantitative Skills Practice I',
                              'venue': 'AB1-401'}
                }
            )


if __name__ == '__main__':
    unittest.main()
