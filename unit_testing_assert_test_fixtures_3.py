import unittest
import kiosk

class CheckInKioskTests(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    kiosk.power_on_kiosk()

  def test_check_in_with_flight_number(self):
    print('Testing the check-in process based on flight number')

  def test_check_in_with_passport(self):
    print('Testing the check-in process based on passport')

  @classmethod
  def tearDownClass(cls):
    kiosk.power_off_kiosk()

  # Write your code below:


unittest.main()