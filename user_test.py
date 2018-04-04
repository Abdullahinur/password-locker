import unittest
from user import User
import pyperclip


class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User("Abdullahinur", "Abdullahi", "0725967528", "aabdullahinur@gmail.com")

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
        test_user = User("Abdullahinur", "Abdullahi", "0725967528",  "aabdullahinur@gmail.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):

        self.new_user.save_user()
        test_user = User("Abdullahinur", "Abdullahi", "0725967528", "aabdullahinur@gmail.com")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_firstName(self):

        self.new_user.save_user()
        test_user = User("Abdullahinur", "Abdullahi", "0725967528", "aabdullahinur@gmail.com")
        test_user.save_user()

        found_user = User.find_by_number("0725967528")

        self.assertEqual(found_user.email, test_user.email)

    def test_user_exists(self):

        self.new_user.save_user()
        test_user = User("Abdullahinur", "0725967528", "Abdullahi", "aabdullahinur@gmail.com")
        test_user.save_user()

        user_exists = User.user_exist("0725967528")

        self.assertTrue(user_exists)

    def test_display_all_users(self):

        self.assertEqual(User.display_users(), User.user_list)

    def test_copy_email(self):

        self.new_user.save_user()
        User.copy_email("0725967528")

        self.assertEqual(self.new_user.email, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
