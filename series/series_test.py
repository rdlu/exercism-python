import unittest

from series import slices

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0


class SeriesTest(unittest.TestCase):
    def test_slices_of_one_from_one(self):
        self.assertEqual(slices("1", 1), ["1"])

    def test_slices_of_one_from_two(self):
        self.assertEqual(slices("12", 1), ["1", "2"])

    def test_slices_of_two(self):
        self.assertEqual(slices("35", 2), ["35"])

    def test_slices_of_two_overlap(self):
        self.assertEqual(slices("9142", 2), ["91", "14", "42"])

    def test_slices_can_include_duplicates(self):
        self.assertEqual(slices("777777", 3), ["777", "777", "777", "777"])

    def test_slices_of_a_long_series(self):
        self.assertEqual(
            slices("918493904243", 5),
            ["91849", "18493", "84939", "49390", "93904", "39042", "90424", "04243"],
        )

    def test_slice_length_is_too_large(self):
        self.assertEqual(slices("12345", 6), [])

    def test_slice_length_cannot_be_zero(self):
        self.assertEqual(slices("12345", 0), [])

    def test_slice_length_cannot_be_negative(self):
        self.assertEqual(slices("12345", -1), [])


if __name__ == "__main__":
    unittest.main()
