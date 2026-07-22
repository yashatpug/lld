from parking_lot import ParkingLot
from vehicle_type import VehicleType

class ParkingLotManager:
    def __init__(self, name: str, address: str, total_slots: int):
        self.parking_lot = ParkingLot(name, address, total_slots)
        self.create_parking_spots()

    def create_parking_spots(self):
        for spot_num in range(1, self.parking_lot.total_slots + 1):
            vehicle_type = VehicleType.TWO_WHEELER if spot_num % 2 == 0 else VehicleType.FOUR_WHEELER
            self.parking_lot.create_parking_spot(f"Spot-{spot_num}", vehicle_type)

    def park_vehicle(self, vehicle):
        return self.parking_lot.park_vehicle(vehicle)

    def unpark_vehicle(self, vehicle):
        return self.parking_lot.unpark_vehicle(vehicle)

    def get_available_slots(self):
        return self.parking_lot.available_slots

    def get_occupied_slots(self):
        return self.parking_lot.occupied_slots

    def show_parked_vehicles(self):
        parked_vehicles = self.parking_lot.parked_vehicles()
        for vehicle, spot_id in parked_vehicles:
            print(f"Vehicle {vehicle.vehicle_reg_num} of type {vehicle.vehicle_type.name} is parked at spot {spot_id}.")
            