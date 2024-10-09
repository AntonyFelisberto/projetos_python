#?! negative lookahead
#?= positive lookahead

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
from pprint import pprint

regex = re.compile(r"^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})(\d{3}\.\d{3}\.\d{3}-\d{2})$",flags=re.MULTILINE)

test_str = "088.289.689-07"

pprint(regex.findall(test_str))