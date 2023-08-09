#!/usr/bin/python3
""" this Class for review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ this for Review Class inherits BaseModel """
    place_id = ""
    user_id = ""
    text = ""
