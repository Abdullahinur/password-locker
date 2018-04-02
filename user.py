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
