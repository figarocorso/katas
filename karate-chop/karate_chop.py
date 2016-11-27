class KarateChop():
    def __init__(self, elements):
        self.elements = sorted(elements)

    @property
    def size(self):
        return len(self.elements)

    @property
    def half(self):
        return self.size // 2

    def chop(self, elem_to_check):
        if self.size == 0:
            return False

        while self.size > 1:
            if self._is_element_in_first_half(elem_to_check):
                self.elements = self._get_first_half()
            else:
                self.elements = self._get_second_half()

        return self.elements[0] == elem_to_check

    def _is_element_in_first_half(self, element):
        return element < self.elements[self.half]

    def _get_first_half(self):
        return self.elements[:self.half]

    def _get_second_half(self):
        return self.elements[self.half:]
