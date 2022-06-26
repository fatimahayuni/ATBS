import re

food = "hat rat mat pat"
aqilah = re.compile("[r]at")
food = aqilah.sub("andrea", food)
print(food)