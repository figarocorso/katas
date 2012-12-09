class RomanNumerals():

    def __init__(self):
        self.easterEggMesssage = "Oops! We have not implemented it yet"
        self.numberToConvert = 0
        self.resultString = ""
        self.unitsConversionTable = {0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
        self.tensConversionTable = {0:'',1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}

    def convert(self,number):
        self.cleanVariablesAndInitialize(number)
        if self.isZero(): return self.easterEggMesssage
        self.addTens().addUnits()
        return self.resultString

    def isZero(self):
        return self.numberToConvert == 0

    def addUnits(self):
        self.resultString += self.unitsConversion()
        return self

    def addTens(self):
        self.resultString += self.tensConversion()
        return self

    def unitsConversion(self):
        return self.unitsConversionTable.get(self.numberToConvert % 10)

    def tensConversion(self):
        return self.tensConversionTable.get(self.numberToConvert % 100 // 10)

    def cleanVariablesAndInitialize(self,number):
        self.resultString = ""
        self.numberToConvert = number
