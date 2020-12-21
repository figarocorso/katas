import unittest


class Passport():
    VALID_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    OPTIONAL_FIELDS = ['cid']

    def __init__(self, fields):
        self.fields = fields

    @classmethod
    def from_string(cls, passport_string):
        passport_string = passport_string.replace("\n", ' ')
        fields = [x.split(':')[0] for x in passport_string.split(' ')]
        return Passport(fields)

    @classmethod
    def bulk_from_string(cls, passports_string):
        return [cls.from_string(x) for x in passports_string.split('\n\n')]

    @classmethod
    def count_valid(cls, passports):
        valid_count = 0
        for passport in passports:
            valid_count += 1 if passport.is_valid else 0
        return valid_count

    @property
    def is_valid(self):
        for field in self.VALID_FIELDS:
            if field not in self.fields and field not in self.OPTIONAL_FIELDS:
                return False

        for field in self.fields:
            if field not in self.VALID_FIELDS:
                return False

        return True


class PassportCheckerTest(unittest.TestCase):
    def setUp(self):
        self.passports_string = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

    def test_passport_valid(self):
        all_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
        self.assertTrue(Passport(all_fields).is_valid)

    def test_passport_invalid_missing_field(self):
        wrong_fields = ['iyr', 'eyr', 'hgt', 'ecl', 'pid', 'cid']
        self.assertFalse(Passport(wrong_fields).is_valid)

    def test_passport_invalid_wrong_field(self):
        all_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
        wrong_fields = all_fields + ['xxx']
        self.assertFalse(Passport(wrong_fields).is_valid)

    def test_passport_valid_without_cid(self):
        all_fields_but_cid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        self.assertTrue(Passport(all_fields_but_cid).is_valid)

    def test_passport_from_string(self):
        passport_string = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm"""
        self.assertTrue(Passport.from_string(passport_string).is_valid)
        passport_string = """iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929"""
        self.assertFalse(Passport.from_string(passport_string).is_valid)
        passport_string = """hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm"""
        self.assertTrue(Passport.from_string(passport_string).is_valid)
        passport_string = """hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
        self.assertFalse(Passport.from_string(passport_string).is_valid)

    def test_bulk_password_checker(self):
        passports = Passport.bulk_from_string(self.passports_string)
        self.assertEqual(4, len(passports))
        self.assertTrue(passports[0].is_valid)
        self.assertFalse(passports[1].is_valid)
        self.assertTrue(passports[2].is_valid)
        self.assertFalse(passports[3].is_valid)

    def test_count_valid_passports(self):
        self.assertEqual(2, Passport.count_valid(Passport.bulk_from_string(self.passports_string)))


if __name__ == '__main__':
    unittest.main()
