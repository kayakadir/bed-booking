
# bedroms has beds
class Bedroom:
    def __init__(self, name):
        self.name = name
        self.beds = [] # array of Bed objects
        print(f'bedroom: {name} created!')
    def addBed(self, b):
        self.beds.append(b)
        print('bed should be added')
    def removeBed(self, b):
        self.beds.remove(b)
        print('bed should be removed!')
    def findEmptyBeds(self): 
        beds = self.beds
        filtered_beds = filter(lambda bed: bed.available == True, beds)
        for bed in filtered_beds:
            print(bed)
    def __str__(self):
        return f'Bedroom; name: {self.name}'
# application have many beds for guests
class Bed:
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.available = True
        print(f'Bed id: {id} created!')
    def reserve(self):
        self.available = False
    def release(self):
        self.available = True
    def __str__(self):
        return f'Bed; id: {self.id}, type: {self.type}, available: {self.available}'

class Booking:
    def __init__(self, bed, start_date, end_date):
        self.bed = bed
        self.start_date = start_date
        self.end_date = end_date
        self.active = True
        print(f'Booking created for {bed}')
    def finishBooking(self, end_date):
        self.active = False
        self.end_date = end_date
    def __str__(self) -> str:
        return f'Booking: {self.bed}, start_date: {self.start_date}, end_date: {self.end_date}, active: {self.active}'

# guest books one or many beds.
class Guest:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.bookings = []
        print(f'Guest name: {name} created!')
    def reserveBed(self, bed, start_date, end_date):
        # make booking
        new_book = Booking(bed, start_date, end_date)
        self.bookings.append(new_book)
        # make reservation
        bed.reserve()
        print('Bed should be reserved!')
    def releaseBed(self, bed, end_date):
        # make booking deactive
        book = self.findBooking(bed)
        if book is not None:
            book.finishBooking(end_date)
            # make bad available again
            bed.release()
        else:
            print(f'The bed didn\'t find from bookings. So it can\'t released.')
    def findBooking(self, bed):
        # searches bed inside of bookings. returns None automaticaly if bed not exist!
        for booking in self.bookings:
            if booking.bed == bed:
                return booking
    def allBookings(self):
        # show all bookings of current guest
        print(f'Bookings of {self.name}')
        for book in self.bookings:
            print(book)
    def __str__(self):
        return f'Guest; name: {self.name}, email: {self.email}, phone: {self.phone}'

