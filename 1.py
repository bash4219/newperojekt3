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


