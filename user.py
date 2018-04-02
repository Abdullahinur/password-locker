class User:
    """
    class that generates new instances of users.
    """

    user_list = []

    def __init__(self, first_name, last_name, email):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def save_user(self):

        User.user_list.append(self)

    def delete_user(self):

        User.user_list.remove(self)

    @classmethod
    def find_by_firstName(cls, first_name):

        for user in cls.user_list:
            if user.first_name == first_name:
                return user

    @classmethod
    def user_exist(cls, first_name):

        for user in cls.user_list:
            if user.first_name == first_name:
                return True

    @classmethod
    def display_user(cls):

        return cls.user_list

        return False
