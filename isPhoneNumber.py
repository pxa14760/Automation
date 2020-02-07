import re
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = phoneNumRegex.search("My phone num is 123-456-7890")
print('Phone number:' +mo.group())
print('Phone number:' +mo.group(0))
print('Phone number:' +mo.group(1))
print('Phone number:' +mo.group(2))



