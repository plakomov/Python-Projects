# This program will take in email (string) (valid email) and it will extract the username and the domain
# and return a print statement


def email_slice(email):
    store = email.split("@")
    username = store[0]
    domain = store[1].split(".")[0]
    return print("Username: {} \nDomain: {}".format(username, domain))

email_slice("pavlolakomov@gmail.com")

