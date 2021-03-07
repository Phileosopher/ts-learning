import re

searchString = "Testing pattern matches"

expr1 = re.compile( r"Test" )
expr2 = re.compile( r"^Test" )
expr3 = re.compile( r"Test$" )
expr4 = re.compile( r"\b\w*es\b" )
expr5 = re.compile( r"t[aeiou]", re.I )

if expr1.search( searchString ):
   print('"Test" was found.')

if expr2.match( searchString ):
   print('"Test" was found at the beginning of the line.')

if expr3.match( searchString ):
   print('"Test" was found at the end of the line.')

result = expr4.findall( searchString )

if result:
   print('There are %d words(s) ending in "es":' % \
      ( len( result ) ),)

   for item in result:
      print(" " + item,)

print

result = expr5.findall( searchString )
if result:
   print('The letter t, followed by a vowel, occurs %d times:' % \
      ( len( result ) ),)

   for item in result:
      print(" " + item,)

print

