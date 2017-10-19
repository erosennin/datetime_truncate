from datetime import datetime
import unittest

from datetime_truncate import truncate
from datetime_truncate import truncate_half_year
from datetime_truncate import truncate_quarter
from datetime_truncate import truncate_week

DEFAULT_DT = datetime(2012, 7, 12, 12, 14, 14, 342)


class TestDatetimeTruncate(unittest.TestCase):
    def setUp(self):
        self.default_dt = datetime(2012, 7, 12, 12, 14, 14, 342)

    def test_truncate_to_second(self):
        self.assertEqual(truncate(self.default_dt, 'second'),
                         self.default_dt.replace(microsecond=0))

    def test_truncate_to_minute(self):
        self.assertEqual(truncate(self.default_dt, 'minute'),
                         self.default_dt.replace(second=0, microsecond=0))

    def test_truncate_to_nth_minute(self):
        self.assertEqual(truncate(self.default_dt, '5_minute'),
                         self.default_dt.replace(minute=10, second=0,
                                                 microsecond=0))

        self.assertEqual(truncate(self.default_dt, '2_minute'),
                         self.default_dt.replace(minute=14, second=0,
                                                 microsecond=0))

        self.assertEqual(truncate(self.default_dt.replace(minute=40),
                                  '13_minute'),
                         self.default_dt.replace(minute=39, second=0,
                                                 microsecond=0))

        self.assertEqual(truncate(self.default_dt.replace(minute=20),
                                  '9_minute'),
                         self.default_dt.replace(minute=18, second=0,
                                                 microsecond=0))

        with self.assertRaises(ValueError) as cm:
            truncate(self.default_dt, '60_minute')
        assert cm.exception.args[0] == (
            '`nth_minute` must be >= 0 and < 60, was 60'
        )

    def test_truncate_to_hour(self):
        self.assertEqual(truncate(self.default_dt, 'hour'),
                         self.default_dt.replace(minute=0, second=0,
                                                 microsecond=0))

    def test_truncate_to_day(self):
        self.assertEqual(truncate(self.default_dt, 'day'),
                         self.default_dt.replace(hour=0, minute=0,
                                                 second=0, microsecond=0))

    def test_truncate_to_month(self):
        self.assertEqual(truncate(self.default_dt, 'month'),
                         self.default_dt.replace(day=1, hour=0, minute=0,
                                                 second=0, microsecond=0))

    def test_truncate_to_year(self):
        self.assertEqual(truncate(self.default_dt, 'year'),
                         self.default_dt.replace(month=1, day=1, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))

    def test_truncate_to_week(self):
        self.assertEqual(truncate(self.default_dt, 'week'),
                         self.default_dt.replace(day=9, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(truncate(self.default_dt.replace(day=9), 'week'),
                         self.default_dt.replace(day=9, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(truncate(self.default_dt.replace(day=16), 'week'),
                         self.default_dt.replace(day=16, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))

        self.assertEqual(truncate_week(self.default_dt),
                         self.default_dt.replace(day=9, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(truncate_week(self.default_dt.replace(day=9)),
                         self.default_dt.replace(day=9, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(truncate_week(self.default_dt.replace(day=16)),
                         self.default_dt.replace(day=16, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))

    def test_truncate_to_quarter(self):
        self.assertEqual(truncate(self.default_dt.replace(month=2), 'quarter'),
                         self.default_dt.replace(month=1, day=1, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(truncate(self.default_dt.replace(month=6), 'quarter'),
                         self.default_dt.replace(month=4, day=1, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(truncate(self.default_dt, 'quarter'),
                         self.default_dt.replace(month=7, day=1, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(
            truncate(self.default_dt.replace(month=10), 'quarter'),
            self.default_dt.replace(month=10, day=1, hour=0,
                                    minute=0, second=0,
                                    microsecond=0))

        self.assertEqual(truncate_quarter(self.default_dt.replace(month=2)),
                         self.default_dt.replace(month=1, day=1, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(truncate_quarter(self.default_dt.replace(month=6)),
                         self.default_dt.replace(month=4, day=1, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(truncate_quarter(self.default_dt),
                         self.default_dt.replace(month=7, day=1, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(
            truncate_quarter(self.default_dt.replace(month=10)),
            self.default_dt.replace(month=10, day=1, hour=0,
                                    minute=0, second=0,
                                    microsecond=0))

    def test_truncat_to_half_year(self):
        self.assertEqual(
            truncate(self.default_dt.replace(month=6), 'half_year'),
            self.default_dt.replace(month=1, day=1, hour=0,
                                    minute=0, second=0,
                                    microsecond=0)
        )
        self.assertEqual(
            truncate_half_year(self.default_dt.replace(month=6)),
            self.default_dt.replace(month=1, day=1, hour=0,
                                    minute=0, second=0,
                                    microsecond=0)
        )
        self.assertEqual(truncate(self.default_dt, 'half_year'),
                         self.default_dt.replace(month=7, day=1, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(truncate_half_year(self.default_dt),
                         self.default_dt.replace(month=7, day=1, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
