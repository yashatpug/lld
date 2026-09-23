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

    def __get_available_spot__(self, vehicle_type: VehicleType):
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

    def __find_occupied_spot__(self, vehicle: Vehicle):
        if vehicle in self.occupied_spots:
            return self.occupied_spots[vehicle]
        else:
            log_message = f"Vehicle {vehicle.vehicle_reg_num} not found in the parking lot"
            print(log_message)
            return None

    def allocate_spot(self, vehicle: Vehicle):
        spot = self.__get_available_spot__(vehicle.vehicle_type)
        if spot:
            spot.occupy(vehicle)
            self.occupied_spots[vehicle] = spot
            self.available_spots[vehicle.vehicle_type].remove(spot)
            log_message = f"Vehicle {vehicle.vehicle_reg_num} parked at spot {spot.spot_id}"
            print(log_message)
            return True
        else:
            log_message = f"No available parking spot for vehicle type: {vehicle.vehicle_type.name}"
            print(log_message)
            return False

    def release_spot(self, vehicle: Vehicle):
        spot = self.__find_occupied_spot__(vehicle)
        if spot:
            spot.vacate()
            self.available_spots[vehicle.vehicle_type].add(spot)
            self.occupied_spots.pop(vehicle, None)
            log_message = f"Vehicle {vehicle.vehicle_reg_num} unparked from spot {spot.spot_id}"
            print(log_message)
            return True
        else:
            log_message = f"Vehicle {vehicle.vehicle_reg_num} not found in the parking lot"
            print(log_message)
            return False

    def show_parked_vehicles(self):
        if self.occupied_spots:
            print("Parked Vehicles:")
            for vehicle, spot in self.occupied_spots.items():
                print(f"Vehicle Reg Num: {vehicle.vehicle_reg_num} of type {vehicle.vehicle_type.name}, Spot ID: {spot.spot_id}")
        else:
            print("No vehicles parked.")

    def show_available_spots(self):
        print("Available Parking Spots:")
        for vehicle_type, spots in self.parking_spot_manager.available_spots.items():
            print(f"Vehicle Type: {vehicle_type.name}, Available Spots: {[spot.spot_id for spot in spots]}")


            
        
