# more strings and text

# devining x
x = "there are %d types fo people." %10
# defining text
binary = "binary"
# defining don't
donot = "don't"
# defing y to yous 2 vaereubels
y = "those who know %s and those who %s " % (binary, donot)

# perinting x
print(x)
# perintinh y
print(y)
# perinting i said with vaereubels
print("I said: %r.:" % x)
print("I alos said: '%s'." % y)
# defins this a true
hilarious = True
# defining vaeryubel with text
jokeEvaluation = "ins't that joke so funny?! %r"

# combind to vaereubels
print(jokeEvaluation % hilarious)
# defining w as text
W = "this is the left side of..."
# defining e as text
e = "a string with a rith side"
print(W+e)

# more printing fun
print("mary had a little lamb.")
print("its fleece was white as %s." % 'snow')
print("and everywhere that mary went.")
print("." * 10)
end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"


print(end1 + end2 + end3 + end4 + end5 +end6)
print(end7 + end8 + end9 + end10 + end11 +end12)

# but wait there's more:
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "tow", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))

# why do I use %r instead of %s in the above example?
# anser
# which should I use on a regular basis?
# anser
# why does %r sometimes give me single quotes around things?
# anser

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# examine closely the differences between the %r formatter and %s formatter
print("Here are the months: %r" % months)
print("Here are the months: %s" % months)

# escape sequences redux
tabbyCat = "\tI'm tabbed in."
persianCat = "I'm split\non a line."
backslashCat = "I'm \\ a \\ cat."
topCat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabbyCat)
print(persianCat)
print(backslashCat)
print(topCat)

# Escape Seq            What it does?
# \\ perints \ one time
print("\\")
# \' perints a sengel '
print("\'")
# \" perints dubel '
print("\"")
# \a mack a bell sawnd
print("\a")
# \b this removes the last cheariter
print("ab" + "\b" + "c")
# \f move werd after dawn and ferwerd
print("hello\fworld")
# \n just move it dawn
print("hello\nworld")
# \N{name}  perints sheps
print("\N{Hammer and sickle} = hapenes")
# \r removes the stuf be for it
print("wen i play bet saber mt\rmy dad bets me \N{White smiling face}")
# \t
# \uxxxx
# \Uxxxxxxxx
# \v
# \ooo
# \xhh


# What does the following code do:
#   while True:
#       for i in ["/", "-", "|", "\\", "|"]:
#           print("%s\r" % i, end='')

#  Can you use ''' instead of """ ?

age = input("How old are you?")
height = input("How tall are you?")

print("So, you are %r old and %r tall." % (age, height))