import unittest

from ticketmaestro.service import BookingSystem

def fn1():
    return 1

def decorator(f):
    if f.func_name == 'fn2':
        return fn1

@decorator
def fn2():
    return 2

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

    def test_best_seats_notok(self):
        self.assertEqual(self.booking.book_best(200), "error")

    def test_best_seats_ok(self):
        self.assertEqual(len(self.booking.book_best(10)), 10)

    def test_list(self):
        odd_numbers = []
        for x in range(0,1000):
            if x % 2 == 1:
                odd_numbers.append(x)
        print odd_numbers

        odd_numbers2 = [ x for x in range(1,1000,2)]
        self.assertListEqual(odd_numbers,odd_numbers2)

    def test_decorator(self):
        self.assertEqual(fn2(),1)

    def test_static_method(self):
        self.assertEqual(BookingSystem.something_static(), 123)

    def test_class_method(self):
        self.assertEqual(BookingSystem.something_for_the_class(), BookingSystem)