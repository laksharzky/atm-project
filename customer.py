from atm_card import ATMcard

class Customer:
    def __init__(self,id,custBalance = 10000,custPin = 1234):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance
    
    def infoPin(self):
        return self.custPin
    
    def infoBalance(self):
        return self.custBalance
        
    def withdrawBalance(self,nominal):
        self.nominal = nominal
        debet = self.custBalance - self.nominal
        return debet

    def saveDeposit(self,nominal):
        self.nominal = nominal
        simpan = self.custBalance + self.nominal
        return simpan
