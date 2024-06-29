import unittest
import random
import datetime
from simulations import Simulations 
from unittest.mock import patch


class TestSimulations(unittest.TestCase):
    def test_get_temp_sensor1(self):
        temp = Simulations.get_temp_sensor1()
        self.assertIsInstance(temp, float)
        self.assertGreaterEqual(temp, 20)
        self.assertLessEqual(temp, 30)

    def test_get_temp_sensor2(self):
        temp = Simulations.get_temp_sensor2()
        self.assertIsInstance(temp, float)
        self.assertGreaterEqual(temp, 20)
        self.assertLessEqual(temp, 30)

    def test_get_humidity(self):
        humidity = Simulations.get_humidity()
        self.assertIsInstance(humidity, int)
        self.assertGreaterEqual(humidity, 0)
        self.assertLessEqual(humidity, 100)

    def test_get_current_datetime(self):
        with patch('simulations.datetime') as mock_datetime:
            mock_datetime.datetime.now.return_value = datetime.datetime(2023, 1, 1, 12, 0, 0)
            mock_datetime.datetime.strftime = datetime.datetime.strftime
            current_datetime = Simulations.get_current_datetime()
            self.assertEqual(current_datetime, "2023-01-01 12:00:00")

if __name__ == '__main__':
    unittest.main()