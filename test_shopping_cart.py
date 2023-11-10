from shopping_cart import ShoppingCart
import unittest

# write your tests here

class TestShoppingCart(unittest.TestCase):
    # def __init__(self,methodName:str = "runTest"):
    #     super().__init__(methodName)
    #     self.obj = ShoppingCart()
    def setUp(self):
        self.obj = ShoppingCart()
    
    def test_add_item(self):
        self.obj.add_item('ab',6000)
        self.assertGreater(self.obj.item_count , 0 , 'item not added')
    
    def test_remove_item(self):
        self.obj.remove_item('ab')
        self.assertEqual(self.obj.item_count,0,'item not removed')
    
    # def 

    

if __name__ == "__main__":
    unittest.main()

    
