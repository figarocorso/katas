class StringCalculator():

    class NegativeNumbers(Exception):
        pass

    def __init__(self):
        self.otherDelimiters = "\n"
        self.defaultDelimitier = ","
        self.string = ""
        self.exceptionString = ""

    def add(self,string):
        self.string = string
        self.extractDefaultDelimitier()
        self.splitString()

        return self.sumValues()

    def sumValues(self):
        sumResult = 0

        for value in self.stringValues:
            if value:
                self.checkNegativeValue(value)
                sumResult += int(value)

        self.raiseExceptionOrNot()
        return str(sumResult)

    def splitString(self):
        self.string = self.replaceOtherDelimitersByDefault()
        self.stringValues = self.string.split(self.defaultDelimitier)

    def replaceOtherDelimitersByDefault(self):
        return self.string.replace(self.otherDelimiters,self.defaultDelimitier)

    def extractDefaultDelimitier(self):
        if self.string and self.string[0] == "/":
            [delimiterStrin,self.string] = self.string.split("\n")
            self.defaultDelimitier = delimiterStrin.lstrip("//")

    def raiseExceptionOrNot(self):
        if not self.exceptionString == "":
            raise self.NegativeNumbers(self.exceptionString.rstrip(","))

    def checkNegativeValue(self,value):
        if int(value) < 0:
            self.exceptionString += value
            self.exceptionString += ","
