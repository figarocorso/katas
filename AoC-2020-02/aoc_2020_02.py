import unittest


class Password():
    def __init__(self, policy_and_password):
        self.password = policy_and_password.split(':')[1].replace(' ', '')

    def __str__(self):
        return str(self.password)


class Policy():
    def __init__(self, policy_and_password):
        self.min_occurrences = int(policy_and_password.split('-')[0])
        self.max_occurrences = int(policy_and_password.split('-')[1].split(' ')[0])
        self.letter = policy_and_password.split('-')[1].split(' ')[1].split(':')[0]

    def password_matches(self, password):
        occurrences = password.count(self.letter)
        return self.min_occurrences <= occurrences and self.max_occurrences >= occurrences


class PasswordPolicyChecker():
    def is_correct(self, policy_and_password):
        policy = Policy(policy_and_password)
        password = Password(policy_and_password)
        return policy.password_matches(str(password))

    def count_correct_passwords(self, policies_and_passwords):
        return len([x for x in policies_and_passwords if self.is_correct(x)])


class PasswordPolicyCheckerTest(unittest.TestCase):
    def setUp(self):
        self.ppc = PasswordPolicyChecker()

    def test_correct_password(self):
        self.assertTrue(self.ppc.is_correct("1-3 a: abcde"))

    def test_incorrect_password_below_min(self):
        self.assertFalse(self.ppc.is_correct("1-3 b: cdefg"))

    def test_incorrect_password_above_max(self):
        self.assertFalse(self.ppc.is_correct("1-3 b: cdefgbbbb"))

    def test_count_correct_passwords(self):
        policies_and_passwords = [
            '1-3 a: abcde',
            '1-3 b: cdefg',
            '2-9 c: ccccccccc'
        ]
        self.assertEqual(2, self.ppc.count_correct_passwords(policies_and_passwords))

    def test_count_zero_correct_passwords(self):
        policies_and_passwords = [
            '1-3 a: bcde',
            '1-3 b: cdefg',
            '2-9 c: c'
        ]
        self.assertEqual(0, self.ppc.count_correct_passwords(policies_and_passwords))

    def test_password_class(self):
        self.assertEqual('cdefg', str(Password('1-3 b: cdefg')))

    def test_policy_parser(self):
        policy_and_password = '1-3 b: cdefg'
        self.assertEqual(1, Policy(policy_and_password).min_occurrences)
        self.assertEqual(3, Policy(policy_and_password).max_occurrences)
        self.assertEqual('b', Policy(policy_and_password).letter)

    def test_policy_parser_two_digits(self):
        policy_and_password = '10-30 b: cdefg'
        self.assertEqual(10, Policy(policy_and_password).min_occurrences)
        self.assertEqual(30, Policy(policy_and_password).max_occurrences)
        self.assertEqual('b', Policy(policy_and_password).letter)


if __name__ == '__main__':
    unittest.main()
