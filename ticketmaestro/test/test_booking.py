import unittest

from ticketmaestro.service import BookingSystem


class TestBooking(unittest.TestCase):
    def setUp(self):
        self.booking = BookingSystem(10,10)

    def test_book_specific(self):
        # always able to book last seat in last row
        self.assertTrue(self.booking.book_specific_seat(9, 9))
        # but only once
        self.assertFalse(self.booking.book_specific_seat(9, 9))
        # seats and rows are zero based
        self.assertRaises(ValueError, lambda : self.booking.book_specific_seat(10, 10))

    def test_best_seats(self):
        self.assertEqual(len(self.booking.book_best(5)), 5)