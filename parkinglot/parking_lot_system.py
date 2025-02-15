from entities import ParkingSpot, SpotType, Vehicle
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class ParkingLotSystem:
    __instance = None
    
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
            cls.__instance.parking_spots = {}
        return cls.__instance
        
    def add_parking_spot(self, spot_number: str, spot_type: SpotType):
        try:
            parking_spot = self.__instance.parking_spots.get(spot_number)
            if not parking_spot:
                parking_spot = ParkingSpot(spot_number, spot_type)
                self.__instance.parking_spots[parking_spot.spot_number] = parking_spot
                logging.info("Spot added succesfully")
                print("Spot added succesfully")
                return parking_spot
            else:
                raise Exception("Spot already exists")
        except Exception as e:
            print(f"error:{e}")
        
    def park_vehicle(self, vehicle: Vehicle, parking_spot_id: str):
        try:
            parking_spot = self.__instance.parking_spots.get(parking_spot_id)
            if not parking_spot:
                raise Exception("No parking spot with this parking number")
            if parking_spot.park_vehicle(vehicle):
                logging.info("Parked successfully")
                print("Parked successfully")
            else:
                raise Exception(f"Can not park, spot is not available or only {parking_spot.spot_type} can be park at this spot")
        except Exception as e:
            print(f"error:{e}")
    
    def unpark_vehicle(self, vehicle: Vehicle):
        try:
            parking_spots = self.__instance.parking_spots
            parked_spot = None
            for parking_spot_id in parking_spots:
                if(parking_spots[parking_spot_id].vehicle.vehicle_number == vehicle.vehicle_number):
                    parked_spot = parking_spots[parking_spot_id]
                    break
            if not parked_spot:
                raise Exception("Vehicle is not parked, can not unpark")
            unpark = parking_spots[parking_spot_id].unpark_vehicle(vehicle)
            
            print(f"unparked {vehicle.vehicle_number}")
                
        except Exception as e:
            print(f"error:{e}")
    
    def display_available_spots(self):
        try:
            parking_spots = self.__instance.parking_spots
            available_parking_spots = []
            for parking_spot_id in parking_spots:
                if(parking_spots[parking_spot_id].check_available()):
                    available_parking_spots.append(parking_spots[parking_spot_id].spot_number)
            return available_parking_spots
        except:
            print(f"error:{e}")
        
        
        
        
    
    
    
