class StringCalculator():

    class NegativeNumbers(Exception):
        pass

    def __init__(self):
        self.otherDelimiters = "\n"
        self.defaultDelimiter = ","
        self.string = ""
        self.exceptionString = ""

    def add(self,string):
        self.string = string
        self.extractDelimiters()
        self.splitString()

        return self.sumValues()

    def sumValues(self):
        sumResult = 0
        for value in self.stringValues:
            if self.valueExistsAndIsCorrect(value):
                self.checkNegativeValue(value)
                sumResult += int(value)
        self.raiseExceptionOrNot()
        return str(sumResult)

    def splitString(self):
        self.string = self.replaceOtherDelimitersByDefault()
        self.stringValues = self.string.split(self.defaultDelimiter)

    def replaceOtherDelimitersByDefault(self):
        for delimiter in self.otherDelimiters:
            self.string = self.string.replace(delimiter,self.defaultDelimiter)
        return self.string

    def extractDelimiters(self):
        if self.string and self.string[0] == "/":
            [delimiterString,self.string] = self.string.split("\n")
            delimiterString = delimiterString.lstrip("//")
            self.otherDelimiters = delimiterString
            self.extractOtherDelimiters(delimiterString)

    def extractOtherDelimiters(self,delimiterString):
        if self.hasMultipleCharDelimiter(delimiterString):
            delimiterString = delimiterString.lstrip("[")
            delimiterString = delimiterString.rstrip("]")
            self.otherDelimiters = delimiterString
            if self.isMultipleDelimitersMultiChar(self.otherDelimiters):
                self.otherDelimiters = str(self.otherDelimiters.split("]["))

    def raiseExceptionOrNot(self):
        if not self.exceptionString == "":
            raise self.NegativeNumbers(self.exceptionString.rstrip(","))

    def checkNegativeValue(self,value):
        if int(value) < 0:
            self.exceptionString += value
            self.exceptionString += ","

    def valueExistsAndIsCorrect(self,value):
        return value and int(value) <= 1000

    def hasMultipleCharDelimiter(self,delimiterString):
        return delimiterString[0] == "["

    def isMultipleDelimitersMultiChar(self,delimitersString):
        return delimitersString.find("][") != -1
