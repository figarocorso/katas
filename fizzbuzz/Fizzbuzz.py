class Fizzbuzz():
    def __init__(self):
        pass

    def answerQuestion(self,number):
        self.stringResult = ""
        self.number = number
        self.addFizz().addBuzz().addNumber()
        return self.stringResult

    def addFizz(self):
        if self.dividedBy3():
            self.stringResult += "Fizz"
        return self

    def addBuzz(self):
        if self.dividedBy5():
           self.stringResult += "Buzz"
        return self

    def addNumber(self):
        if self.stringResult == "":
            self.stringResult += str(self.number)
        return self

    def dividedBy3(self):
        return self.number % 3 == 0 or self.containsNumber(3)

    def dividedBy5(self):
        return self.number % 5 == 0 or self.containsNumber(5)

    def containsNumber(self,numberContained):
        for digit in str(self.number):
            if digit == str(numberContained):
                return True
        return False

