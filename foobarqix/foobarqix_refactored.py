class FooBarQix:

    @property
    def values(self):
        return {
            3: "Foo",
            5: "Bar",
            7: "Qix"
        }

    def compute(self, input_string):
        result = ""
        result += self.divisibility_input_string(input_string)
        result += self.number_presence_input_string(input_string)
        return result if result else input_string

    def divisibility_input_string(self, input_string):
        result = ""
        for key, value in self.values.items():
            result += value if self.is_divisible_by(int(input_string), key)  else ""
        return result

    @classmethod
    def is_divisible_by(cls, a, b):
        return a % b == 0

    def number_presence_input_string(self, input_string):
        result = ""
        for char in input_string:
            result += self.values.get(int(char), "")
        return result
