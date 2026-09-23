from .parking_spot_manager import ParkingSpotManager
from .vehicle import Vehicle

class ParkingLot:
    def __init__(self, name: str, address: str, total_slots: int):
        self.name = name
        self.address = address
        self.total_slots = total_slots
        self.parking_spot_manager = ParkingSpotManager(total_slots)

    def park_vehicle(self, vehicle: Vehicle):
        self.parking_spot_manager.allocate_spot(vehicle)

    def unpark_vehicle(self, vehicle: Vehicle):
        self.parking_spot_manager.release_spot(vehicle)

    def show_available_spots(self):
        self.parking_spot_manager.show_available_spots()

    def show_parked_vehicles(self):
        self.parking_spot_manager.show_parked_vehicles()
