'''
opening file

open(
file_name_required,
mode_read_write_append_required_and_binary_or_text,
encoding_to_use_in_text_mode)

mode : read=r write=w append=a
selector : binary_mode=b text_mode=t

ex :
mode=wt [write text]
rb [read binary]
'''

import sys
from pprint import pprint as pp

print(sys.getdefaultencoding())

f = open("scratch.txt", mode="at", encoding="utf-8")
'''
write() returns then umber of codepoints written. Do not sum these values to determine the file length.
'''
code_points = f.write("\n-----------This is new line appended from code-------")
print(code_points)
f.close()

g = open("scratch.txt", mode="rt", encoding="utf-8")
pp([x for x in g.read().split("\n")])

# should print blank... ''
pp(g.read())

# to go to starting of the file
g.seek(0)
pp([x for x in g.read().split("\n")])

pp("-- readlines() --")
g.seek(0)
pp([x for x in g.readlines()])

pp("-- readline() --")
g.seek(0)
pp([x for x in g.readline() if x])
