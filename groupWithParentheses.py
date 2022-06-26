import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
mo.group(2)
mo.group(0)
mo.group()