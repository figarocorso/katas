from math import sqrt

class PrimeFactors():

    def __init__(self):
        pass

    def get_prime_factors(self,number):
        reminder = number
        prime_factors = []

        while not (reminder == 1):
            prime_factors.append(self.get_first_factor(reminder))
            reminder = reminder // prime_factors[-1]

        prime_factors.insert(0,1)

        return prime_factors


    def get_first_factor(self, number):
        for factor in self.get_divisors_for_factor_checking(number):
            if self.divides(number,factor) and self.is_prime(factor):
                return factor

        return number

    def is_prime(self, number):
        for divisor in self.get_divisors_for_prime_checking(number):
            if self.divides(number, divisor):
                return False

        return True

    def divides(self, number, divisor):
        return (number % divisor) == 0

    def get_divisors_for_prime_checking(self, number):
        return range(2, int( sqrt(number) ) + 1)

    def get_divisors_for_factor_checking(self,number):
        return range(2, number // 2 + 1)
