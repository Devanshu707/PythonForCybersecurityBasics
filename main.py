#code to authenticate

username = "Devanshu"
password = "mehtadevanshu1234"
def login(uname, passw):

    login_attempts = 0
    successful_attempt = 0
    failed_attempts = 0
    if uname == "Devanshu" and passw == "mehtadevanshu1234":
        print("Login Successful")
        successful_attempt += 1
        failed_attempts += 0
    else:
        print("Invalid Username or Password")
        successful_attempt += 0
        failed_attempts += 1
    login_attempts += 1

    print("No. of times login attempted: ", login_attempts)
    print("No. of times login was successful: ", successful_attempt)
    print("No. of times login failed: ", failed_attempts)



uname = input("Enter username:\n")
passw = input("Enter a password: \n")
login(uname, passw)






