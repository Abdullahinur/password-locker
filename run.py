#!/usr/bin/env python3.6
from user import User


def create_user(fname, lname, email):
    '''
    Function to create a new user
    '''
    new_user = Contact(fname, lname, email)
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
