from .parking_spot_manager import ParkingSpotManager
from .vehicle import Vehicle

class ParkingLot:
    def __init__(self, name: str, address: str, total_slots: int):
        self.name = name
        self.address = address
        self.total_slots = total_slots
        self.parking_spot_manager = ParkingSpotManager(total_slots)

    def park_vehicle(self, vehicle: Vehicle):
        spot = self.parking_spot_manager.get_available_spot(vehicle.vehicle_type)
        if spot:
            spot.occupy(vehicle)
            self.parking_spot_manager.occupied_spots[vehicle] = spot
            self.parking_spot_manager.available_spots[vehicle.vehicle_type].remove(spot)
            log_message = f"Vehicle {vehicle.vehicle_reg_num} parked at spot {spot.spot_id}"
            print(log_message)
            return True
        else:
            log_message = f"No available parking spot for vehicle type: {vehicle.vehicle_type.name}"
            print(log_message)
            return False

    def unpark_vehicle(self, vehicle: Vehicle):
        spot = self.parking_spot_manager.find_occupied_spot(vehicle)
        if spot:
            spot.vacate()
            self.parking_spot_manager.available_spots[vehicle.vehicle_type].add(spot)
            self.parking_spot_manager.occupied_spots.pop(vehicle, None)
            log_message = f"Vehicle {vehicle.vehicle_reg_num} unparked from spot {spot.spot_id}"
            print(log_message)
            return True
        else:
            log_message = f"Vehicle {vehicle.vehicle_reg_num} not found in the parking lot"
            print(log_message)
            return False

    def show_parked_vehicles(self):
        if self.parking_spot_manager.occupied_spots:
            print("Parked Vehicles:")
            for vehicle, spot in self.parking_spot_manager.occupied_spots.items():
                print(f"Vehicle Reg Num: {vehicle.vehicle_reg_num} of type {vehicle.vehicle_type.name}, Spot ID: {spot.spot_id}")
        else:
            print("No vehicles parked.")

    def show_available_spots(self):
        print("Available Parking Spots:")
        for vehicle_type, spots in self.parking_spot_manager.available_spots.items():
            print(f"Vehicle Type: {vehicle_type.name}, Available Spots: {[spot.spot_id for spot in spots]}")

    def get_available_slots(self) -> int:
        return sum(len(spots) for spots in self.parking_spot_manager.available_spots.values())

    def get_occupied_slots(self) -> int:
        return len(self.parking_spot_manager.occupied_spots)
