from datetime import datetime

import pandas as pd

fake_affidavit = pd.DataFrame({'Date': [datetime(2020, 2, 6),
                                        datetime(2020, 2, 6),
                                        datetime(2020, 2, 6),
                                        datetime(2020, 2, 6),
                                        datetime(2020, 2, 6)],
                               'PlayedOn': [datetime(2020, 2, 6, 3, 21, 46),
                                            datetime(2020, 2, 6, 3, 21, 49),
                                            datetime(2020, 2, 6, 3, 21, 52),
                                            datetime(2020, 2, 6, 3, 21, 58),
                                            datetime(2020, 2, 6, 3, 22, 6)],
                               'MediaName': ['cetgroup1_1.jpg',
                                             'cetgroup1_2.jpg',
                                             '1stguard_new2.jpg',
                                             'cetgroup1_1.jpg',
                                             'cetgroup1_2.jpg'],
                               'FileName': ['cetgroup1_1.jpg',
                                            'cetgroup1_2.jpg',
                                            '1stguard_new2.jpg',
                                            'cetgroup1_1.jpg',
                                            'cetgroup1_2.jpg'],
                               'DeviceName': ['CET TRUCK 2 (Trailer 53-154)',
                                              'CET TRUCK 2 (Trailer 53-154)',
                                              'CET TRUCK 2 (Trailer 53-154)',
                                              'CET TRUCK 2 (Trailer 53-154)',
                                              'CET TRUCK 1 (Trailer 53-155)']})
