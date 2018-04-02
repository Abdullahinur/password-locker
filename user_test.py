import unittest
from user import User


class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User("Abdullahinur", "Abdullahi", "aabdullahinur@gmail.com")

    def tearDown(self):

        User.user_list = []

    def test_init(self):

        self.assertEqual(self.new_user.first_name, "Abdullahinur")
        self.assertEqual(self.new_user.last_name, "Abdullahi")
        self.assertEqual(self.new_user.email, "aabdullahinur@gmail.com")

    def test_save_user(self):

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):

        self.new_user.save_user()
        test_user = User("Abdullahinur", "Abdullahi", "aabdullahinur@gmail.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):

        self.new_user.save_user()
        test_user = User("Abdullahinur", "Abdullahi", "aabdullahinur@gmail.com")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_firstName(self):

        self.new_user.save_user()
        test_user = User("Abdullahinur", "Abdullahi", "aabdullahinur@gmail.com")
        test_user.save_user()

        found_user = User.find_by_firstName("Abdullahinur")

        self.assertEqual(found_user.email, test_user.email)

    def test_user_exists(self):

        self.new_user.save_user()
        test_user = User("Abdullahinur", "Abdullahi", "aabdullahinur@gmail.com")
        test_user.save_user()

        user_exists = User.user_exist("Abdullahinur")

        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()
