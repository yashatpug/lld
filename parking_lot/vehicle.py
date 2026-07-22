from abc import ABC, abstractmethod

from vehicle_type import VehicleType

class Vehicle(ABC):
    def __init__(self, vehicle_reg_num: str, vehicle_type: VehicleType):
        self.vehicle_reg_num = vehicle_reg_num
        self.vehicle_type = vehicle_type
