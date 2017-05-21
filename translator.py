# English to TestLang

import re

english_string = input("Type some text to translate - e.g. The red and the blue ball sing.")

testlang_string = english_string

testlang_string = re.sub("red", "kra", english_string)
testlang_string = re.sub("blue", "ci", testlang_string)
testlang_string = re.sub("the", "-", testlang_string)
testlang_string = re.sub("and", "i", testlang_string)
testlang_string = re.sub("ball", "mach", testlang_string)
testlang_string = re.sub("sing", "pjut", testlang_string)

print(testlang_string)

# red = kra
# blue = ci
# the = -
# and = i
# ball = mach
# sing = pjut

# Translate The red and the blue ball sing, output should be - kra i - ci mach pjut
