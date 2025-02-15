from entities import User, Address, Hotel, Room, Booking, Payment, RoomType, RoomStatus
from hotel_management_system import HotelManagementSystem
from datetime import datetime, date
import threading
from multiprocessing import Process

hotel_booking_system = HotelManagementSystem()

# hotel_booking_system2 = HotelManagementSystem()
# print(hotel_booking_system is hotel_booking_system2)

user1 = User("id1","vaibhav","vaibhav@g.com","9999999999")
user2 = User("id2","vaibhav 2","vaibhav@g.com","9999999999")
hotel_booking_system.add_user(user1)
hotel_booking_system.add_user(user2)

room1 = Room("roomid1",RoomType.BASIC,2000,RoomStatus.AVAILABLE)
room2 = Room("roomid2",RoomType.DELUXE,4000,RoomStatus.AVAILABLE)
hotel_booking_system.add_room(room1)
hotel_booking_system.add_room(room2)


def attempt_booking(user, room):
    booking_result = hotel_booking_system.book_room(user, room, date(2024, 2, 20), date(2024, 2, 23))
    print(f"{user.name} booking attempt: {booking_result}")

process1 = Process(target=attempt_booking, args=(user1, room1.id))
process2 = Process(target=attempt_booking, args=(user2, room1.id))

# Start both processes
process1.start()
process2.start()

# Wait for both processes to complete
process1.join()
process2.join()


# # Create two threads trying to book the same room
# thread1 = threading.Thread(target=attempt_booking, args=(user1, room1))
# thread2 = threading.Thread(target=attempt_booking, args=(user2, room1))

# # Start threads simultaneously
# thread1.start()
# thread2.start()


# # booking room
# booking = hotel_booking_system.book_room(user1, room1, date(2024, 2, 20), date(2024, 2, 23))
# booking2 = hotel_booking_system.book_room(user2, room1, date(2024, 2, 20), date(2024, 2, 23))
# booking3 = hotel_booking_system.book_room(user1, room2, date(2024, 3, 20), date(2024, 3, 23))

# print("first booking got successfull", booking)
# print("second booking failed at room is not available", booking2)

# print("room1 status ->", room1.status)

# # cancel booking
# print(hotel_booking_system.cancel_booking(booking["booking"].id))
# print(hotel_booking_system.cancel_booking(booking["booking"].id))


# print(hotel_booking_system.get_user_bookings(user1.id))










