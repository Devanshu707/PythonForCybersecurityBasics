# Regular Expressions (regex) are a sequence of characters that forms a pattern.
import re
# device_id = ["aaa2f5", "fser52a", "dcsaaa24" , "464gfg", "aa354h"]
# \w matches any alphanumeric character, + represents one or more occurences of a specific character.
# \w+ is used most commonly for any number of characters in a alphanumeric.
# email_addresses = """devanshu@gmail.com, aryan32@gmail.com, atharv90@gmail.in"""
#re.findall() returns a list of matches to a regular expression
# print(re.findall("\w+@\w+\.\w+", email_addresses))
# You can use these additional symbols to match to specific kinds of characters:
#  . matches to all characters, including symbols
# \d matches to all single digits [0-9]
# \s matches to all single spaces
# \. matches to the period character
# --------------------------------------------------------------------------
# print(re.findall("\d{2}", "h32rb17 k825t0m c2994eh"))
# print(re.findall("\d+", "h32rb17"))
# print(re.findall("\d*", "h32rb17"))
# print(re.findall("\d{1,3}", "h32rb17 k825t0m c2994eh"))
# ------------------------------------------------------------------------------
pattern = "\w+:\s\d+"
employee_logins_string = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"
print(re.findall(pattern, employee_logins_string))


