# def greet_employee():
#     print("Hello Employees")
#
# greet_employee()
#
# def greet_employee(fname, lname):
#     print("Welcome", fname, lname)
#     print(fname, "is logged into the system")
#
# fname = input("Enter your first name: ")
# lname = input("Enter your last name: ")
# greet_employee(fname, lname)

# RETURN STATEMENT
def calculate_fails(total_attempts, failed_attempts):
    fail_percentage = failed_attempts / total_attempts
    return fail_percentage

failed_attempts = int(input())
total_attempts = int(input())
percentage = calculate_fails(total_attempts, failed_attempts)
if percentage >= 0.5:
    print("Account Locked")
else:
    print("You have a few chances left to login")
