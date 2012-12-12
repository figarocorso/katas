# Primero un dicionario "-":0, ...
# Add el concepto de row

class Bowling():
    def __init__(self):
        self.firstThrow = 0
        self.secondThrow = 1
        self.rollResult = 0
        self.throwNumberInRow = 1
        self.row = [0,0]
        self.rowPoints = 0
        self.spareMultiplier = 0
        self.strikeMultiplier = 0

    def calculateRoll(self,throws):
        for throw in throws:
            self.nextTrow(throw).checkSpare().addPoints()

        return self.rollResult

    def nextTrow(self,throw):
        self.nextThrowInRow()
        if self.isFirstThrow():
            self.rowPoints = 0
        self.row[self.throwNumberInRow] = throw
        return self

    def checkSpare(self):
        if self.isSpare():
            self.addSpare()
        return self

    def addSpare(self):
        if self.isFirstThrow():
            self.nextThrowInRow()

        self.rowPoints = 10

    def addPoints(self):
        if not self.isFirstThrow():
            self.calculateRowPoints()
            self.addStrikeSpareBonus()
            self.rollResult += self.rowPoints
        return self

    def calculateRowPoints(self):
        if self.normalThrow():
            self.rowPoints = self.addThrow(self.row[self.firstThrow])
            self.rowPoints += self.addThrow(self.row[self.secondThrow])

    def addThrow(self,throw):
        if self.missed(throw):
            return 0
        else:
            return int(throw)


    def addStrikeSpareBonus(self):
            pass

    def nextThrowInRow(self):
        self.throwNumberInRow = (self.throwNumberInRow + 1) % 2

    def isFirstThrow(self):
        return self.throwNumberInRow == self.firstThrow

    def isSpare(self):
        return self.row[self.throwNumberInRow] == "/"

    def normalThrow(self):
        return self.rowPoints == 0

    def missed(self,throw):
        return throw == "-"
