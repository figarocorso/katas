class FooBarQix:

    def compute(self, string):
        result = ""
        result += self.divisibility_string(string)
        result += self.number_presence_string(string)
        return result if result else string

    def divisibility_string(self, string):
        result = ""
        number = int(string)
        if number % 3 == 0:
            result += "Foo"

        if number % 5 == 0:
            result += "Bar"

        if number % 7 == 0:
            result += "Qix"

        return result

    def number_presence_string(self, string):
        result = ""
        for char in string:
            if char == "3":
                result += "Foo"
            elif char == "5":
                result += "Bar"
            elif char == "7":
                result += "Qix"

        return result
