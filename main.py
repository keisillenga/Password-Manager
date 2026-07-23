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
def save_password():
  with open(FILE_NAME, "w") as file:
    json.dump(password, file, indent=4)
def generate_password(length=12):
  characters = (
  string.ascii_letters +
  string.digits +
  string.punctuation
)
password = ""
for _ in range(length):
  password += random.choice(characters)
return password
def  add_password():
  password = load_password()
   website = input("Website: ")
   username = input("Username ")
   choice = input("Generate password? (y/n): ").lower()
   if choice == "y":
   password = generate_password()
   print("Generate password: ",passsword)
  else:
  password = input("Password: ")
password[website] = {
  "username" : username,
  "password" : password
}
save_passwords(passwords)
print("\nPassword saved successfully!\n")
 def view_password():
   passwords = view_passwords()
   if not passwords:
     print("\nNo password saved.\n")
     return
    print("\nSaved password\n")
    for website, info in passwords.items():
      print("----------------")
      print("Website :", website)
      print("Username :", info["username"])
      print("Password :", info["password"])
    print()
def search_password():
  passwords = load_passwords()
   website = input("Enter website: ")
 if website in passwords:
   print("\nFound\n")
   print("Username:", passwords[website]["username"])
   print("Password:", passwords[website]["password"])
else:
  print("\nPassword not found")

  print()
def delete_password():
  passwords = load_passwords()
   website = input("Website to delete: ")
  if website in passwords:
    del passwords[website]
    save_passwords(passwords)
    print("Deleted successfully\n")
  else:
    print("Website not found\n")


 

