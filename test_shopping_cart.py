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
        self.obj.add_item('mive',6000)
        self.assertGreater(self.obj.item_count , 0 , 'item not added')
    
    def test_remove_item(self):
        self.obj.add_item('ab',6000)
        self.obj.add_item('mive',6000)
        print(self.obj.remove_item('ab'))
        self.assertEqual(self.obj.item_count,1,'item not removed')
    
    def test_mean_item_price(self):
        self.obj.add_item('ab',4000)
        self.obj.add_item('mive',6000)
        self.assertEqual(self.obj.total/self.obj.item_count,5000,'mean is not calculated')
    
    

        


    

if __name__ == "__main__":
    unittest.main()

    
