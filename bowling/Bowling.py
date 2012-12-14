# First: Introduced a dictionary "-":0, ....
# Secondly: Introduced the concept of row
# Abandoned because of a rule missunderstanding
# Abandoned because of unfixeable problem with last throws
class Bowling():
    def __init__(self):
        self.firstThrow = 0
        self.secondThrow = 1
        self.rollResult = 0
        self.throwNumberInRow = 1
        self.row = [0,0]
        self.rowPoints = 0
        self.multiplierWindow = [1,1]
        self.itHasBeenSpecial = False
        self.throw = ""

    def calculateRoll(self,throws):
        for throw in throws:
            self.nextTrow(throw).checkSpecialRow().addPoints()

        return self.rollResult

    def nextTrow(self,throw):
        self.throw = throw
        self.nextThrowInRow()
        if self.isFirstThrow():
            self.rowPoints = 0
        self.row[self.throwNumberInRow] = throw
        return self

    def checkSpecialRow(self):
        if self.isSpecialThrow():
            self.addSpecialRow()
            self.itHasBeenSpecial = True
        return self

    def addSpecialRow(self):
        if self.isFirstThrow():
            self.nextThrowInRow()
        self.rowPoints = 10

    def isSpecialThrow(self):
        return self.isSpare() or self.isStrike()

    def addPoints(self):
        if not self.isFirstThrow():
            self.calculateRowPoints().strikeSpareBonus()
            self.rollResult += self.rowPoints
            print "Throw = " + self.throw + " - " + str(self.rowPoints)
        return self

    def calculateRowPoints(self):
        if self.normalThrow():
            self.rowPoints = self.addThrow(self.row[self.firstThrow])
            self.rowPoints += self.addThrow(self.row[self.secondThrow])
        return self

    def addThrow(self,throw):
        if self.missed(throw):
            return 0
        else:
            return int(throw)

    def strikeSpareBonus(self):
        print "Pre: " + str(self.multiplierWindow)
        self.addStrikeSpareBonus().updateMultipliers()
        print "Post: " + str(self.multiplierWindow)

    def addStrikeSpareBonus(self):
        self.rowPoints *= self.multipliersPending()
        return self

    def multipliersPending(self):
        return self.multiplierWindow[0]

    def updateMultipliers(self):
        self.rotateMultipliers()
        if self.itHasBeenSpecial:
            self.itHasBeenSpecial = False
            self.multiplierWindow[0] += 1
            if self.isStrike():
                self.multiplierWindow[1] += 1

    def rotateMultipliers(self):
        self.multiplierWindow[0] = self.multiplierWindow[1]
        self.multiplierWindow[1] = 1

    def nextThrowInRow(self):
        self.throwNumberInRow = (self.throwNumberInRow + 1) % 2

    def isFirstThrow(self):
        return self.throwNumberInRow == self.firstThrow

    def isStrike(self):
        return self.throw == "X"

    def isSpare(self):
        return self.throw == "/"

    def normalThrow(self):
        return self.rowPoints == 0

    def missed(self,throw):
        return throw == "-"
