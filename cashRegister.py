### cashRegister.py ###
# NOTE: Only functional with Python 3.6

denomArray = [["ONE HUNDRED", 100.00], ["TWENTY", 20.00], ["TEN", 10.00], ["FIVE", 5.00], ["ONE", 1.00], ["QUARTER", 0.25], ["DIME", 0.10], ["NICKEL", 0.05], ["PENNY", 0.01]]

def checkCashRegister(price, cash, cashInDrawer):

#    cashInDrawer = cashInDrawer.reverse()
    cashInDrawer = cashInDrawer[::-1]
    change = cash - price
    changeInDenominations = []
    totalCashInDrawer = 0

    if not isFloat(price, cash) or not greaterThanZero(price, cash):
        raise ValueError('Please enter a valid price and cash value greater than zero')
    
    if not isArray(cashInDrawer):
        raise ValueError('Cash in Drawer is formatted incorrectly')
    
    else:
        for index in range(9):
            totalCashInDrawer += cashInDrawer[index][1]

        for index in range(9):
            multiple = int(change/denomArray[index][1])

            if totalCashInDrawer == change:
                return "Closed"
            elif multiple > 0 and cashInDrawer[index][1] > change:
                changeInDenominations.append([denomArray[index][0], (denomArray[index][1] * multiple)])
                change -= (denomArray[index][1] * multiple)
            elif index == 8 and cashInDrawer[index][1] < change:
                return "Insufficient Funds"

    return changeInDenominations   

def isFloat(price, cash):
    return (type(price) == float) and (type(cash) == float) 

def isArray(cashInDrawer):
    return (type(cashInDrawer) == list)

def greaterThanZero(price, cash):
    return (price > 0) and (cash > 0)

def greaterCash(price, cash):
    return (cash > price)
