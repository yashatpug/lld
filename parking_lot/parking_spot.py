from vehicle import Vehicle
from vehicle_type import VehicleType

class ParkingSpot:
    def __init__(self, spot_id: str, vehicle_type: VehicleType):
        self.spot_id = spot_id
        self.vehicle_type = vehicle_type
        self.is_occupied = False
        self.vehicle = None

    def occupy(self, vehicle: Vehicle):
        self.is_occupied = True
        self.vehicle = vehicle

    def vacate(self):
        self.is_occupied = False
        self.vehicle = None