
class BookingSystem(object):
    '''
    This is the class for booking system logic
    '''
    def __init__(self, row_count, seat_count):
        self._seats = {} # array of array containing seat data 0 - free, 1 - occupied
        for row in range(0,row_count):
            self._seats[row] = {}
            for seat in range(0, seat_count):
                self._seats[row][seat] = 0

    def book_specific_seat(self, row, seat):
        '''
        Book specific seat

        :param row:
        :param seat:
        :return: True if booked False otherwise
        '''
        return False

    def book_best(self, n_seats):
        '''
        Book n best seats

        :param n_seats:
        :return: list of tuples [(row, seat),]
        '''
        return []