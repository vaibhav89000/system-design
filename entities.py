from enum import Enum
from datetime import date, datetime, timedelta

class RoomType(Enum):
    BASIC = "BASIC"
    DELUXE = "DELUXE"
    
class RoomStatus(Enum):
    OCCUPIED = "OCCUPIED"
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"
    BOOKED = "BOOKED"
    
class BookingStatus(Enum):
    CONFIRMED = "CONFIRMED"
    CANCELED = "CANCELED"

class User:
    def __init__(self,id: str, name: str, email: str,mobile_number: str):
        self.id = id
        self.name = name
        self.email = email
        self.mobile_number = mobile_number
        
class Address:
    def __init__(self,
    id: str,
    address_line_1: str,
    address_line_2: str,
    state: str,
    country: str
    ):
        self.id = id
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.state = state
        self.country = country

class Hotel:
    def __init__(self,
    id: str,
    address: Address,
    name: str,
    mobile_number: str
    ):
        self.id = id
        self.name = name
        self.address = address
        self.mobile_number = mobile_number
      
class Room:
    def __init__(self,
    id: str,
    room_type: RoomType,
    price: float,
    status: RoomStatus
    ):
        self.id = id
        self.type = room_type
        self.price = price
        self.status = status
        
    def book(self):
        if(self.status == RoomStatus.AVAILABLE):
            self.status = RoomStatus.BOOKED
            return "Room booked successfully"
        else:
            return ValueError("This Room is not available") 
        
    def check_in(self):
        if(self.status == RoomStatus.BOOKED):
            self.status = RoomStatus.OCCUPIED
            return "Check in successful"
        else:
            return ValueError("Room is not booked") 
    
    def check_out(self):
        if(self.status == RoomStatus.OCCUPIED):
            self.status = RoomStatus.AVAILABLE
            return "Check out successful"
        else:
            return ValueError("Room is not occupied") 

class Booking:
    def __init__(self,
    id: str,
    user: User,
    room: Room,
    # hotel: Hotel,
    check_in_date: date,
    check_out_date: date
    ):
        self.id = id
        self.user = user
        self.room = room
        # self.hotel = hotel
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.status = BookingStatus.CONFIRMED
        self.booking_datetime = datetime.now()
        
    def cancel(self):
  
        if(self.status == BookingStatus.CONFIRMED):
            self.status = BookingStatus.CANCELED
            return self
        else:
            return ValueError("Booking is not confirmed!")
        
class Payment:
    pass
