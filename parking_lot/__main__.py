"""Run the parking-lot demonstration."""

if __package__:
    from .parking_lot import ParkingLot
    from .vehicle import Vehicle
    from .vehicle_type import VehicleType
else:
    # Support running this file directly from an editor or terminal.
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from parking_lot.parking_lot import ParkingLot
    from parking_lot.vehicle import Vehicle
    from parking_lot.vehicle_type import VehicleType


def main() -> None:
    parking_lot = ParkingLot("My Parking Lot", "123 Main St", 7)
    parking_lot.show_available_spots()
    parking_lot.show_parked_vehicles()

    vehicle_one = Vehicle("KA-01-HH-1234", VehicleType.FOUR_WHEELER)
    parking_lot.park_vehicle(vehicle_one)
    parking_lot.show_available_spots()
    parking_lot.show_parked_vehicles()

    vehicle_two = Vehicle("KA-01-HH-5678", VehicleType.TWO_WHEELER)
    parking_lot.park_vehicle(vehicle_two)
    parking_lot.show_available_spots()
    parking_lot.show_parked_vehicles()

    parking_lot.unpark_vehicle(vehicle_one)
    parking_lot.show_available_spots()
    parking_lot.show_parked_vehicles()

    parking_lot.park_vehicle(Vehicle("KA-01-HH-9999", VehicleType.FOUR_WHEELER))
    parking_lot.show_available_spots()
    parking_lot.show_parked_vehicles()

    parking_lot.unpark_vehicle(vehicle_two)
    parking_lot.show_available_spots()
    parking_lot.show_parked_vehicles()


if __name__ == "__main__":
    main()
