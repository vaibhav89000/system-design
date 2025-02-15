from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime

class VehicleType(Enum):
    CAR = "CAR"
    MOTORCYCLE = "MOTORCYCLE"
    TRUCK = "TRUCK"
    
class SpotType(Enum):
    CAR = "CAR"
    MOTORCYCLE = "MOTORCYCLE"
    TRUCK = "TRUCK"
    
class ParkingSpotStatus(Enum):
    AVAILABLE = "AVAILABLE"
    OCCUPIED = "OCCUPIED"
    UNAVAILABLE = "UNAVAILABLE"

class Vehicle(ABC):
    def __init__(self, vehicle_number: str, vehicle_type: VehicleType):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        
class Motorcycle(Vehicle):
    def __init__(self, vehicle_number: str):
        super().__init__(vehicle_number,VehicleType.MOTORCYCLE)

class Car(Vehicle):
    def __init__(self, vehicle_number: str):
        super().__init__(vehicle_number,VehicleType.CAR)
        
class Truck(Vehicle):
    def __init__(self, vehicle_number: str):
        super().__init__(vehicle_number,VehicleType.TRUCK)

class ParkingSpot(ABC):
    def __init__(self, spot_number: str, spot_type: SpotType):
        self.vehicle = None 
        self.status = ParkingSpotStatus.AVAILABLE
        self.spot_number = spot_number
        self.spot_type = spot_type
        self.price = self.get_spot_price()
        
    def park_vehicle(self,vehicle: Vehicle):
        if (vehicle.vehicle_type.value == self.spot_type.value
        and self.vehicle == None 
        and self.status == ParkingSpotStatus.AVAILABLE):
            self.vehicle = vehicle
            self.status = ParkingSpotStatus.OCCUPIED
            return True
        else:
            return False
    
    def unpark_vehicle(self, vehicle: Vehicle):
        if (self.vehicle == vehicle):
            self.vehicle = None
            self.status = ParkingSpotStatus.AVAILABLE
            return True
        else:
            return False
            
    def check_available(self):
        if(self.status == ParkingSpotStatus.AVAILABLE and self.vehicle == None):
            return True
        return False
    
    def get_spot_price(self):
        if(self.spot_type == SpotType.CAR):
            return 50
        elif(self.spot_type == SpotType.MOTORCYCLE):
            return 20
        else:
            return 100
        
class ParkingReciept:
    def __init__(self, parking_spot: ParkingSpot,vehicle: Vehicle):
        self.parking_spot = parking_spot
        self.parked_time = datetime.now()
        self.exit_time = None
        self.vehicle = vehicle
    
        
    
        
    

        
