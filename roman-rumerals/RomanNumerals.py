class RomanNumerals():

    def __init__(self):
        self.easterEggMesssage = "Oops! We have not implemented it yet"
        self.numberToConvert = 0
        self.resultString = ""
        self.resultDigit = 0
        self.unitsConversionTable = {0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
        self.tensConversionTable = {0:'',1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}
        self.hundredsConversionTable = {0:'',1:'C',2:'CC',3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}
        self.thousandsConversionTable = {0:'',1:'M',2:'MM',3:'MMM'}
        self.reverseConversionTable = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    def convert(self,number):
        if type(number) is int:
            return self.digitToNumeral(number)
        elif type(number) is str:
            return self.numeralToDigit(number)
        return "Unsupported type."

    def numeralToDigit(self,number):
        for letter in number:
            self.resultDigit += self.reverseConversionTable.get(letter)
            self.resultDigit -= self.adjustConversion(letter)
        return self.resultDigit

    def digitToNumeral(self,number):
        if self.rangeIsCorrect(number):
            self.initializeConversor(number).addThousands().addHundreds().addTens().addUnits()
        return self.resultString

    def adjustConversion(self,letter):
        if letter == "M" and self.resultDigit % 1000 == 100:
            return 200
        elif letter == "D" and self.resultDigit % 1000 == 100:
            return 200
        elif letter == "C" and self.resultDigit % 100 == 10:
            return 20
        elif letter == "L" and self.resultDigit % 100 == 10:
            return 20
        elif letter == "X" and self.resultDigit % 10 == 1:
            return 2
        elif letter == "V" and self.resultDigit % 10 == 1:
            return 2
        else:
            return 0


    def rangeIsCorrect(self,number):
        if number == 0:
            self.resultString = self.easterEggMesssage
            return False
        elif number < 0 or number >3999:
            return False
        else:
            return True

    def addUnits(self):
        self.resultString += self.unitsConversion()
        return self

    def addTens(self):
        self.resultString += self.tensConversion()
        return self

    def addHundreds(self):
        self.resultString += self.hundredsConversion()
        return self

    def addThousands(self):
        self.resultString += self.thousandsConversion()
        return self

    def unitsConversion(self):
        return self.unitsConversionTable.get(self.numberToConvert % 10)

    def tensConversion(self):
        return self.tensConversionTable.get(self.numberToConvert % 100 // 10)

    def hundredsConversion(self):
        return self.hundredsConversionTable.get(self.numberToConvert % 1000 // 100)

    def thousandsConversion(self):
        return self.thousandsConversionTable.get(self.numberToConvert % 10000 // 1000)

    def initializeConversor(self,number):
        self.resultString = ""
        self.numberToConvert = number
        return self
