## test_cashRegister.py ##

import unittest
import cashRegister 

class TestCashRegister(unittest.TestCase):

    def test_isFloat(self):
        self.assertEqual(cashRegister.isFloat(12.34, 56.78), True)

    def test_greaterThanZero(self):
        self.assertEqual(cashRegister.greaterThanZero(1.23, 567.80), True)

    def test_greaterCash(self):
        self.assertEqual(cashRegister.greaterThanZero(1.23, 567.80), True)

    def test_checkCashRegister(self):
        self.assertEqual(cashRegister.checkCashRegister(19.50, 20.00, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.10], ["QUARTER", 4.25], ["ONE", 90.00], ["FIVE", 55.00], ["TEN", 20.00], ["TWENTY", 60.00], ["ONE HUNDRED", 100.00]]), [["QUARTER", 0.50]])
        self.assertEqual(cashRegister.checkCashRegister(19.50, 20.00, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]), "Insufficient Funds")

        self.assertRaises(ValueError, cashRegister.checkCashRegister, 0, 0, 0)
        self.assertRaises(ValueError, cashRegister.checkCashRegister, 123, 567, [])
        self.assertRaises(ValueError, cashRegister.checkCashRegister, -123, -567, [])
        self.assertRaises(ValueError, cashRegister.checkCashRegister, "abc", "def", [])
#        self.assertRaises(ValueError, cashRegister.checkCashRegister, 5000)

if __name__ == '__main__':
    unittest.main()
    
#    change = cashRegister.checkCashRegister(10, 100, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 200], ["ONE HUNDRED", 0]])
#    print(change)
