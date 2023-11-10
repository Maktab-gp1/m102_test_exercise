from shopping_cart import ShoppingCart
import unittest

# write your tests here
first = ShoppingCart
class TestShoppingCart(unittest.TestCase):
    def __init__(self):
        self.obj = ShoppingCart()
    # def test_setup(self):
    #     self.first = ShoppingCart()
    
    def test_add_item(self):
        self.obj.add_item('ab',6000)
        self.assertGrater(first.item_count , 0 , 'item not added')


if __name__ == "__main__":
    unittest.main()

    
