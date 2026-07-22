from parking_lot_manager import ParkingLotManager
from vehicle import Vehicle
from vehicle_type import VehicleType

parking_lot_manager = ParkingLotManager("My Parking Lot", "123 Main St", 100)
print("Available slots:", parking_lot_manager.get_available_slots())
print("Occupied slots:", parking_lot_manager.get_occupied_slots())
parking_lot_manager.show_parked_vehicles()
parking_lot_manager.park_vehicle(Vehicle("KA-01-HH-1234", VehicleType.FOUR_WHEELER))
print("Available slots after parking:", parking_lot_manager.get_available_slots())
print("Occupied slots after parking:", parking_lot_manager.get_occupied_slots())
parking_lot_manager.show_parked_vehicles()
parking_lot_manager.park_vehicle(Vehicle("KA-01-HH-5678", VehicleType.TWO_WHEELER))
print("Available slots after parking:", parking_lot_manager.get_available_slots())
print("Occupied slots after parking:", parking_lot_manager.get_occupied_slots())
parking_lot_manager.show_parked_vehicles()
parking_lot_manager.unpark_vehicle(Vehicle("KA-01-HH-1234", VehicleType.FOUR_WHEELER))
print("Available slots after unparking:", parking_lot_manager.get_available_slots())
print("Occupied slots after unparking:", parking_lot_manager.get_occupied_slots())
parking_lot_manager.show_parked_vehicles()
parking_lot_manager.park_vehicle(Vehicle("KA-01-HH-9999", VehicleType.FOUR_WHEELER))
print("Available slots after parking:", parking_lot_manager.get_available_slots())
print("Occupied slots after parking:", parking_lot_manager.get_occupied_slots())
parking_lot_manager.show_parked_vehicles()
parking_lot_manager.unpark_vehicle(Vehicle("KA-01-HH-5678", VehicleType.TWO_WHEELER))
print("Available slots after unparking:", parking_lot_manager.get_available_slots())
print("Occupied slots after unparking:", parking_lot_manager.get_occupied_slots())
parking_lot_manager.show_parked_vehicles()



