from collections import defaultdict

from .parking_spot import ParkingSpot
from .vehicle_type import VehicleType
from .vehicle import Vehicle

class ParkingSpotManager:
    def __init__(self, total_spots: int = 100):
        self.available_spots = self.__instantiate_parking_spots__(total_spots)
        self.occupied_spots = {}

    def __instantiate_parking_spots__(self, total_spots: int):
        available_spots = defaultdict(set)
        for spot_num in range(1, total_spots + 1):
            vehicle_type = VehicleType.TWO_WHEELER if spot_num % 2 == 0 else VehicleType.FOUR_WHEELER
            spot = ParkingSpot(f"Spot-{spot_num}", vehicle_type)
            available_spots[vehicle_type].add(spot)
        return available_spots

    def get_available_spot(self, vehicle_type: VehicleType):
        if vehicle_type in self.available_spots:
            if self.available_spots[vehicle_type]:
                return next(iter(self.available_spots[vehicle_type]))
            else:
                log_message = f"No available parking spot for vehicle type: {vehicle_type.name}"
                print(log_message)
                return None
        else:
            log_message = f"No available parking spot for vehicle type: {vehicle_type.name}"
            print(log_message)
            return None

    def find_occupied_spot(self, vehicle: Vehicle):
        if vehicle in self.occupied_spots:
            return self.occupied_spots[vehicle]
        else:
            log_message = f"Vehicle {vehicle.vehicle_reg_num} not found in the parking lot"
            print(log_message)
            return None


            
        
