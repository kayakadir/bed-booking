from classes import Bed, Bedroom, Booking, Guest
import datetime as dt

daire8 = Bedroom('daire8')

b1 = Bed(1, 'single')
b2 = Bed(2, 'single')
b3 = Bed(3, 'single')
daire8.findEmptyBeds()
daire8.addBed(b1)
daire8.addBed(b2)
daire8.addBed(b3)
""" daire8.findEmptyBeds()
daire8.removeBed(b1)
daire8.findEmptyBeds()
daire8.addBed(b1)
daire8.findEmptyBeds()

 """
guest1 = Guest('Kadir', 'kadir@gmail.com', '+905555555555')
guest2 = Guest('Ahmet', 'ahmet@gmail.com', '+905555555555')
guest3 = Guest('Mehmet', 'mehmet@gmail.com', '+905555555555')

# reserve bed
print('reserving bed')
s_date = dt.datetime.now()
e_date = dt.datetime(2022, 12, 30)
guest1.reserveBed(b1, s_date, e_date)
daire8.findEmptyBeds()
guest1.allBookings()

# release bed
print('releasing bed')
guest1.releaseBed(b1, dt.datetime.now())
daire8.findEmptyBeds()
guest1.allBookings()
