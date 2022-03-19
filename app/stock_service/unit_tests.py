import unittest
from datetime import datetime
# from app import Employee, Senior_Engineer, Engineer, Trainer, Completion_Record, Course, Course_Prerequisite, Class_Run, Trainer_Record, Class_Record, Registration
from stock import *



class TestStock(unittest.TestCase):
    def test_json(self):
        stock = Stock(product_id="p3", stock_count="4")

        self.assertEqual(stock.json(), {
            "product_id": "p3",
            "stock_count": "4"
        })




if __name__ == "__main__":
    unittest.main()