import subprocess
import sys
import unittest
from pathlib import Path

from parking_lot import ParkingLot, Vehicle, VehicleType


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class ParkingLotTests(unittest.TestCase):
    def test_public_package_imports(self):
        lot = ParkingLot("Test Lot", "Test Address", 2)

        self.assertEqual(lot.name, "Test Lot")
        self.assertEqual(lot.get_available_slots(), 2)
        self.assertEqual(lot.get_occupied_slots(), 0)

    def test_park_and_unpark_vehicle_updates_slot_counts(self):
        parking_lot = ParkingLot("Test Lot", "Test Address", total_slots=2)
        vehicle = Vehicle("KA-01-HH-1234", VehicleType.FOUR_WHEELER)

        self.assertTrue(parking_lot.park_vehicle(vehicle))
        self.assertEqual(parking_lot.get_available_slots(), 1)
        self.assertEqual(parking_lot.get_occupied_slots(), 1)

        self.assertTrue(parking_lot.unpark_vehicle(vehicle))
        self.assertEqual(parking_lot.get_available_slots(), 2)
        self.assertEqual(parking_lot.get_occupied_slots(), 0)

    def test_cannot_unpark_a_vehicle_that_is_not_parked(self):
        parking_lot = ParkingLot("Test Lot", "Test Address", total_slots=2)
        vehicle = Vehicle("KA-01-HH-1234", VehicleType.FOUR_WHEELER)

        self.assertFalse(parking_lot.unpark_vehicle(vehicle))
        self.assertEqual(parking_lot.get_available_slots(), 2)
        self.assertEqual(parking_lot.get_occupied_slots(), 0)


class EntryPointTests(unittest.TestCase):
    def run_entry_point(self, *command):
        return subprocess.run(
            [sys.executable, *command],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_package_entry_point_runs(self):
        result = self.run_entry_point("-m", "parking_lot")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Available Parking Spots:", result.stdout)
        self.assertIn("KA-01-HH-1234 parked", result.stdout)

    def test_direct_entry_point_runs(self):
        result = self.run_entry_point("parking_lot/__main__.py")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Available Parking Spots:", result.stdout)
        self.assertIn("KA-01-HH-1234 parked", result.stdout)


if __name__ == "__main__":
    unittest.main()
