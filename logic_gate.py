# This is a program that implements Logic Gates

class LogicGate:
    """This is a class on Logic Gate"""
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self,n):
        super(BinaryGate,self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate "+ self.getLabel()+"--->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getLabel()+"---->"))

class UnaryGate(LogicGate):

    def __init__(self, n):
        super(UnaryGate,self).__init__(n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"---->"))

    


