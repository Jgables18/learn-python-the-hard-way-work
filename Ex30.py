people = 30
cars = 40
trucks = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "we can't decide."

if trucks > cars:
    print "thats too many trucks"
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "we still cant decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
