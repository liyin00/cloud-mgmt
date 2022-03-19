import unittest
from datetime import datetime
# from app import Employee, Senior_Engineer, Engineer, Trainer, Completion_Record, Course, Course_Prerequisite, Class_Run, Trainer_Record, Class_Record, Registration
from order import *



class TestOrder(unittest.TestCase):
    # def test_json(self):
    #     order = Orders(chapter_id="BEM460_C1_Chapt1", learner_id="LNR17",
    #     completion=0)
    #     self.assertEqual(chapter_learner_1.json(), {
    #         'chapter_id' : "BEM460_C1_Chapt1",
    #         "learner_id" : "LNR17",
    #         "completion": 0
    #         })

    def test_purchased_conversion(self):
        stock = Orders()
        stock.products_purchased = 'p1,p3,p4'
        array = Orders.array_conversion_purchased(stock)
        print(array)
        self.assertEqual(array, ['p1','p3','p4'])

    def test_quantity_conversion(self):
        stock = Orders()
        stock.purchased_quantity = '2,4,5'
        array = Orders.array_conversion_quantity(stock)
        print(array)
        self.assertEqual(array, ['2','4','5'])




if __name__ == "__main__":
    unittest.main()