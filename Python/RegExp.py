import re
email = input("Enter a email : ").strip()

# username, domain = email.split("@")
# domains = ["google","yahoo","outlook"]
# if username and domain.endswith(".com"):
#     print("valid")
# else:
#     print("Invalid")


if re.search(r"^\w+@(\w+\.)?\w+\.(com|gov|net|edu)$",email):
    print("Valid")
else:
    print("Invalid")
