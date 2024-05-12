import re

text = "Contact emails are: john.doe@example.com and Jane.Doe@example.com."

emails = re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", text, re.IGNORECASE)

print(emails)