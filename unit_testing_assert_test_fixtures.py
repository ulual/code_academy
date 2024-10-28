import unittest

def power_cycle_device():
  print('Power cycling bluetooth device...')

class BluetoothDeviceTests(unittest.TestCase):
  def setUp(self):
    power_cycle_device()

  def test_feature_a(self):
    print('Testing Feature A')

  def test_feature_b(self):
    print('Testing Feature B')

  def tearDown(self):
    power_cycle_device()

unittest.main()