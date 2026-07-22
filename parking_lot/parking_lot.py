from vehicle_type import VehicleType
from parking_spot import ParkingSpot
from vehicle import Vehicle

class ParkingLot:
    def __init__(self, name: str, address: str, total_slots: int):
        self.name = name
        self.address = address
        self.total_slots = total_slots
        self.available_slots = total_slots
        self.occupied_slots = 0
        self.parking_spots = []

    def create_parking_spot(self, spot_id: str, vehicle_type: VehicleType):
        if self.occupied_slots >= self.total_slots:
            raise Exception("Parking lot max capacity reached. Cannot create more parking spots.")
        spot = ParkingSpot(spot_id, vehicle_type)
        self.parking_spots.append(spot)
        return spot

    def find_available_spot(self, vehicle_type: VehicleType):
        for spot in self.parking_spots:
            if spot.vehicle_type == vehicle_type and not spot.is_occupied:
                return spot
        log_message = f"No available parking spot for vehicle type: {vehicle_type.name}"
        print(log_message)
        return None

    def park_vehicle(self, vehicle: Vehicle):
        spot = self.find_available_spot(vehicle.vehicle_type)
        if spot:
            spot.occupy(vehicle)
            self.available_slots -= 1
            self.occupied_slots += 1
            log_message = f"Vehicle {vehicle.vehicle_reg_num} parked at spot {spot.spot_id}"
            print(log_message)
            return True
        else:
            log_message = f"No available parking spot for vehicle type: {vehicle.vehicle_type.name}"
            print(log_message)
            return False

    def unpark_vehicle(self, vehicle: Vehicle):
        for spot in self.parking_spots:
            if spot.is_occupied and spot.vehicle.vehicle_reg_num == vehicle.vehicle_reg_num:
                spot.vacate()
                self.available_slots += 1
                self.occupied_slots -= 1
                log_message = f"Vehicle {vehicle.vehicle_reg_num} unparked from spot {spot.spot_id}"
                print(log_message)
                return True
        log_message = f"Vehicle {vehicle.vehicle_reg_num} not found in the parking lot"
        print(log_message)
        return False

    def parked_vehicles(self):
        return [(spot.vehicle, spot.spot_id) for spot in self.parking_spots if spot.is_occupied]

    