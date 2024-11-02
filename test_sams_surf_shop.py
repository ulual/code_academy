# Write your code below:
# Step 1.
import unittest
import surfshop
import datetime # Steps # 13.

# Steps 2.
# Class name to test Sam's Surf Shop website.
class TestSamsSurfShop(unittest.TestCase):

  # Steps 3
  # Setup fixture that executed before the start of every test.
  def setUp(self):
    self.cart = surfshop.ShoppingCart()
  
  # Test # 1 for steps 4.
  def test_add_surfboard(self):
    message = self.cart.add_surfboards(quantity = 1)
    self.assertEqual(message, f'Successfully added 1 surfboard to cart!')

  # Test # 2 improved for steps 5.
  def test_add_surfboards(self):
        for i in range(2, 5):
            with self.subTest(i=i): # Steps 10.
                message = self.cart.add_surfboards(i)
                self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()
# Test # 2 for steps 5.
# old version without parameterization
# def test_add_surfboards(self):
#     message = self.cart.add_surfboards(2)
#     self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
#     self.cart = surfshop.ShoppingCart()

  # Test # 3 for steps 6.
  @unittest.skip
  def test_add_too_many_surfboards(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 4)
    
  # Test # 4 for steps 7.
  #@unittest.expectedFailure
  def test_apply_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

  def test_add_invalid_checkout_date(self):
    date = datetime.datetime.now()
    self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, date)

unittest.main()