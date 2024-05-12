import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"

key_to_extract = "Occupation"


pattern = fr"{key_to_extract}: (.*?)(?:;|$)"


match = re.search(pattern, text)


if match:
    occupation = match.group(1)
    print(f"The {key_to_extract} is: {occupation}")
else:
    print(f"No {key_to_extract} found in the text.")