from parking_lot_system import ParkingLotSystem
from entities import SpotType, Car

parking_system = ParkingLotSystem()
# parking_system2 = ParkingLotSystem()
# print(parking_system is parking_system2)

parking_system.add_parking_spot("sp1", SpotType.CAR)
parking_system.add_parking_spot("sp2", SpotType.CAR)
parking_system.add_parking_spot("sp1", SpotType.CAR)

parking_system.add_parking_spot("sp4", SpotType.CAR)
parking_system.add_parking_spot("sp5", SpotType.CAR)

vehicle1 = Car("1234")
vehicle2 = Car("2345")

parking_system.park_vehicle(vehicle1, "sp1")
parking_system.park_vehicle(vehicle2, "sp1")

parking_system.unpark_vehicle(vehicle1)
parking_system.park_vehicle(vehicle2, "sp1")

available_spots = parking_system.display_available_spots()
print("available_spots:", available_spots)
