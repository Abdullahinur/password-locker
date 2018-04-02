#!/usr/bin/env python3.6
from user import User


def create_user(first_name, last_name, email):
    '''
    Function to create a new user
    '''
    new_user = User(first_name, last_name, email)
    return new_user


def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()


def del_user(user):
    '''
    Function to delete a contact
    '''
    user.delete_user()


def find_user(fname):
    '''
    Function that finds a user by their first name
    '''
    return User.find_by_firstName(fname)


def check_existing_users(fname):
    '''
    Function that checks if a contact exists with that first name and returns a boolean
    '''
    return User.user_exist(fname)


def display_users():
    '''
    Function that returns all the saved user_list
    '''
    return User.display_users()


def copy_existing_email(fname):
    '''
    Function that copys the Firstname of a user to the machine #### This will be changed
    '''

    return User.copy_email(fname)


def main():
    print("\n")
    print("Welcome to Ab's PassWord Locker")
    print("This will store your credentails and generate a password for you")
    print("My name is Ab,")
    print("What's yours")
    user_name = input()

    print(f"Hello {user_name}.")
    print("You can use this program by typing some simple phrases")
    print("Here are some phrases to get you started: # new - create new user, # display - displays the users, # find - find a user, # del - del a user, # copy - copy user info, # exit - exit the password locker")

    phrases = input().lower()

    if phrases == 'new':
        print("New User")
        print("-" * 10)

        print("What is your First Name:")
        first_name = input()

        print("What is your last Name:")
        last_name = input()

        print("What is your email address:")
        email = input()

        # Create and save a new user
        save_users(create_user(first_name, last_name, email))

        print("\n")
        print("\n")
        print(f"Welcome NEW USER: {first_name}")
        print("\n")


if __name__ == '__main__':
    main()
