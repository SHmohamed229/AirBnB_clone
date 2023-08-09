#!/usr/bin/python3
""" this for User Class """
from models.base_model import BaseModel


class User(BaseModel):
    """ this for User class that inherits BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
