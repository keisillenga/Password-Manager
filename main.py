import json
import random
import string
import os

FILE_NAME = "password-manager"
def load_password():
  if not os.path.exists(FILE_NAME):
    return{}

   with open(FILE_NAME, "r") as file:
     try:
       return json.load(file)
     except json.JSONDcodeError:
       return{}
