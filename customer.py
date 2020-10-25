from atm_card import ATMcard

class Customer:
    def __init__(self,id,custBalance = 10000,custPin = 1234):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance
    
    def checkId(self):
        return self.id

    def infoPin(self):
        return self.custPin
    
    def infoBalance(self):
        return self.custBalance
        
    def withdrawBalance(self,nominal):
        self.custBalance -= nominal

    def saveDeposit(self,nominal):
        self.custBalance += nominal
