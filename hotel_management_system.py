from entities import User, Room, Booking, RoomStatus
# from threading import Lock
import uuid
from datetime import datetime, date
import time
from multiprocessing import Lock, Manager

class HotelManagementSystem:
    __instance = None
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
            manager = Manager()
            cls.__instance.users = manager.dict() 
            cls.__instance.rooms = manager.dict() 
            cls.__instance.bookings = manager.dict() 
            cls.__instance.lock = Lock()
            
        return cls.__instance
        
    def add_user(self, user: User):
        self.__instance.users[user.id] = user
    
    def add_room(self, room: Room):
        self.__instance.rooms[room.id] = room
        
    def book_room(self, user: User, roomId: str, check_in_date: date, check_out_date: date):
        with self.__instance.lock:
            room = self.__instance.rooms.get(roomId)
            if room.status != RoomStatus.AVAILABLE:
                return "Room is not available"
            time.sleep(2)
            if isinstance(room.book(),ValueError):
                return "Room is not available"
            else:
                room.status = RoomStatus.BOOKED
                self.__instance.rooms[room.id] = room
                booking = Booking(uuid.uuid4(), user, room, check_in_date, check_out_date)
                self.__instance.bookings[booking.id] = booking
                return {"booking": booking, "message": "Room is booked successfully"}
            
    def cancel_booking(self, bookingId: str):
        booking = self.__instance.bookings.get(bookingId)
        booking_response = booking.cancel()
        if isinstance(booking_response,ValueError):
            return "Can not cancel booking,try reaching support team."
        else:
            self.__instance.bookings[bookingId] = booking_response
            room = booking_response.room
            room.status = RoomStatus.AVAILABLE
            return "Booking is canceled"
            
    def get_user_bookings(self,userId: str):
        user = self.__instance.users.get(userId)
        if(user):
            user_bookings = []
            for bookingId in self.__instance.bookings:
                booking = self.__instance.bookings[bookingId]
                if(booking.user == user):
                    user_bookings.append(booking.__dict__)
            return user_bookings
        else:
            return "There is no user with this id"
        
    
    
    
        
