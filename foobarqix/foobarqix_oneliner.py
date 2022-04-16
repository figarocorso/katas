TEXTS_TO_APPEND = {
    3: 'Foo',
    5: 'Bar',
    7: 'Qix',
}

class FooBarQix:

    def compute(self, string):
        return (''.join([TEXTS_TO_APPEND[x] for x in TEXTS_TO_APPEND if int(string) % x == 0])
                + ''.join([TEXTS_TO_APPEND.get(int(x), '') for x in string])) or string
