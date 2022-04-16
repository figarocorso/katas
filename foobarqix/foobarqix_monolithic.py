class FooBarQix:

    def compute(self, string):
        result = ""

        if int(string) % 3 == 0:
            result += "Foo"

        if int(string) % 5 == 0:
            result += "Bar"

        if int(string) % 7 == 0:
            result += "Qix"

        for char in string:
            if char == "3":
                result += "Foo"
            elif char == "5":
                result += "Bar"
            elif char == "7":
                result += "Qix"

        return result if result else string
