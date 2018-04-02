import unittest
from user import User


class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User("Abdullahinur", "Abdullahi", "aabdullahinur@gmail.com")

    def test_init(self):

        self.assertEqual(self.new_user.first_name, "Abdullahinur")
        self.assertEqual(self.new_user.last_name, "Abdullahi")
        self.assertEqual(self.new_user.email, "aabdullahinur@gmail.com")


if __name__ == '__main__':
    unittest.main()
