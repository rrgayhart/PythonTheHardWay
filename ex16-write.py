print "Would you like to open a file in this directory?"
print "If not, hit CTRL-C (^C)."
print "Otherwise, which file should we open?"

file = raw_input(": ")

target = open(file)

print "\n"
print target.read()
