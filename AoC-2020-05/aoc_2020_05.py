import unittest


class WrongCharException(Exception):
    pass


class SeatLocator():
    UPPER_HALF = '1'
    LOWER_HALF = '0'

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def highest_id(self, seat_locations):
        highest = 0
        for location in seat_locations:
            seat_id = self.set_seat(location).id_number
            highest = seat_id if seat_id > highest else highest
        return highest

    def set_seat(self, seat_location):
        self.seat_location = seat_location
        first_l_or_r = self.first_l_or_r_index(self.seat_location)
        self.seat_row_location = self.seat_location[:first_l_or_r]
        self.seat_row_location = self.seat_row_location.replace('F', self.LOWER_HALF)\
                .replace('B', self.UPPER_HALF)
        self.seat_column_location = self.seat_location[first_l_or_r:]
        self.seat_column_location = self.seat_column_location.replace('L', self.LOWER_HALF)\
                .replace('R', self.UPPER_HALF)
        return self

    @classmethod
    def first_l_or_r_index(self, location):
        index_l = location.find('L')
        index_r = location.find('R')
        return index_l if index_l >= 0 and (index_r < 0 or index_l <= index_r) else index_r

    @property
    def id_number(self):
        return self.seat_row * self.columns + self.seat_column

    @property
    def seat_row(self):
        return self.binary_partition(self.rows, self.seat_row_location)

    @property
    def seat_column(self):
        return self.binary_partition(self.columns, self.seat_column_location)

    @classmethod
    def binary_partition(cls, upper_limit, location):
        lower_limit = 0
        for partition in location:
            limit_gap = upper_limit - lower_limit
            if partition == cls.UPPER_HALF:
                lower_limit += limit_gap // 2
            elif partition == cls.LOWER_HALF:
                upper_limit -= limit_gap // 2
            else:
                raise WrongCharException(f"Incorrect token for binary partition: {location} - {partition}")
        return lower_limit


class SeatLocatorTest(unittest.TestCase):
    def setUp(self):
        self.seat_locator = SeatLocator(128, 8)

    def test_seat_id(self):
        self.assertEqual(567, self.seat_locator.set_seat('BFFFBBFRRR').id_number)
        self.assertEqual(119, self.seat_locator.set_seat('FFFBBBFRRR').id_number)
        self.assertEqual(820, self.seat_locator.set_seat('BBFFBBFRLL').id_number)

    def test_seat_id_wrong_char(self):
        with self.assertRaises(WrongCharException):
            self.seat_locator.set_seat('BFFFBBFRRK').id_number

    def test_find_l_or_r(self):
        self.assertEqual(7, self.seat_locator.first_l_or_r_index('BFFFBBFRRR'))
        self.assertEqual(7, self.seat_locator.first_l_or_r_index('FFFBBBFLLL'))
        self.assertEqual(7, self.seat_locator.first_l_or_r_index('BBFFBBFRLL'))

    def test_binary_partition_8(self):
        self.assertEqual(7, self.seat_locator.binary_partition(8, '111'))
        self.assertEqual(4, self.seat_locator.binary_partition(8, '100'))

    def test_binary_partition_128(self):
        self.assertEqual(70, self.seat_locator.binary_partition(128, '1000110'))
        self.assertEqual(14, self.seat_locator.binary_partition(128, '0001110'))
        self.assertEqual(102, self.seat_locator.binary_partition(128, '1100110'))

    def test_highest_id(self):
        self.assertEqual(820, self.seat_locator.highest_id(['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']))


if __name__ == '__main__':
    unittest.main()
