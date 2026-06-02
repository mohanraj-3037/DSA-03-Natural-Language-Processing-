import re
text = "My email is student123@gmail.com and my phone number is 9876543210."
email_pattern = r'\w+@\w+\.\w+'
email_match = re.search(email_pattern, text)
if email_match:
    print("Email found:", email_match.group())
phone_pattern = r'\d{10}'
phone_match = re.search(phone_pattern, text)
if phone_match:
    print("Phone number found:", phone_match.group())
result = re.match(r'My', text)
if result:
    print("'My' matched at the beginning of the text.")
numbers = re.findall(r'\d+', text)
print("Numbers found:", numbers)
