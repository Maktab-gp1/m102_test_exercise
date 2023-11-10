from shopping_cart import ShoppingCart
import unittest
# write your tests here


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.first = ShoppingCart()

    def test_add_item(self):
        self.first.add_item('mesvak', 5000)
        self.first.add_item('khamir dandon', 2000)
        # self.assertEqual(first.total, 7000, 'item not added')
        self.assertGreater(self.first.item_count, 0, 'item not added')

    def test_remove_item(self):
        self.first.add_item('mesvak', 5000)
        self.first.remove_item('mesvak')
        self.assertTrue(self.first.item_count == 0, 'item not removed')

    def test_mean_item_price(self):
        self.first.add_item('mesvak', 5000)
        self.first.add_item('medad', 1000)
        self.assertEqual(self.first.mean_item_price(),
                         3000, "price is not correct")


# if __name__ == '__main__':
#     unittest.main()
