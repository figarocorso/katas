class BowlingV2:
    def __init__(self):
        self.functions = {"-":"Miss","/":"Spare","X":"Strike"}
        self.translations = {"X":10,"/":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"1":1,"-":0}
        self.initialRoll = ""
        self.translatedRoll = []
        self.calculatedRoll = []

    def calculateRoll(self,roll):
        self.initialRoll = roll
        return self.sumRoll()

    def sumRoll(self):
        self.calculateSpecialThrows()
        return self.sumThrows()

    def calculateSpecialThrows(self):
        for throwNumber in reversed(range(0,len(self.initialRoll))):
            calculateFunction  = getattr(self,self.functionName(self.initialRoll[throwNumber]))
            calculateFunction(throwNumber)

    def sumThrows(self):
        sum = 0
        for throwNumber in range(0,len(self.calculatedRoll)):
            sum += self.calculatedRoll[throwNumber]
        return sum

    def functionName(self,throw):
        if throw in self.functions:
            return "calculate" + self.functions[throw]
        return "calculateNormalThrow"

    def calculateNormalThrow(self,throwNumber):
        self.translatedRoll.insert(0,int(self.initialRoll[throwNumber]))
        self.calculatedRoll.insert(0,self.translatedRoll[0])

    def calculateMiss(self,throwNumber):
        self.translatedRoll.insert(0,0)
        self.calculatedRoll.insert(0,0)

    def calculateSpare(self,throwNumber):
        self.translatedRoll.insert(0, 10 - self.previousThrowValue(throwNumber))
        self.calculatedRoll.insert(0, self.translatedRoll[0] + self.translatedRoll[1])
        self.correctLastThrowValue()

    def calculateStrike(self,throwNumber):
        self.translatedRoll.insert(0,10)
        if not self.lastTwoThrows():
            self.calculatedRoll.insert(0,10)
            self.lastThrowConditions()
        else:
            self.calculatedRoll.insert(0,0)

    def lastThrowConditions(self):
        if len(self.translatedRoll) > 1:
            self.calculatedRoll[0] += self.translatedRoll[1]

        if len(self.translatedRoll) > 2:
            self.calculatedRoll[0] += self.translatedRoll[2]

    def correctLastThrowValue(self):
        if len(self.calculatedRoll) < 3:
            self.calculatedRoll[1] = 0

    def lastTwoThrows(self):
        return len(self.calculatedRoll) < 2

    def previousThrowValue(self, currentThrow):
        return int(self.initialRoll[currentThrow - 1])
