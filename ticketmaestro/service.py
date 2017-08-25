
class BookingSystem(object):
    '''
    This is the class for booking system logic
    '''
    def __init__(self, row_count, seat_count):
        self._seats = {} # array of array containing seat data 0 - free, 1 - occupied
        self.row_count = row_count
        self.seat_count = seat_count
        for row in range(0,row_count):
            self._seats[row] = {}
            for seat in range(0, seat_count):
                self._seats[row][seat] = 0

    def book_specific_seat(self, row, seat):
        '''
        Book specific seat

        :param row:
        :param seat:
        :return: True if successfully booked False if already occupied
        '''

        try:
            x = self._seats[row][seat]
        except KeyError as x:
            raise ValueError("value is out of range")

        if x==0:
            self._seats[row][seat] = 1
            return True
        else:
            return False

    def book_best(self, n_seats):
        '''
        Book n best seats

        :param n_seats:
        :return: list of tuples [(row, seat),]
        '''
        bookinglist = []
        for row in range(0,self.row_count):
            for seat in range(0, self.seat_count):
                if self._seats[row][seat] == 0:
                    self._seats[row][seat] = 1
                    bookinglist.append((row, seat))

                if len(bookinglist) == n_seats:
                    break
            if len(bookinglist) == n_seats:
                break
        if len(bookinglist) < n_seats:
            for bookinglist[]:
                self._seats[row][seat] = 0
            return "error"

        return bookinglist