name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#Old String Formatting
print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight

print "If I add %d, %d, and %d I get %d." % (
  age, height, weight, age + height + weight)

#New Output Formatting
print name, repr(weight).rjust(10)

print "Let's talk about {}".format(name)
print "If I add {0}, {1}, and {2} I get {3}.".format(
  age, height, weight, age + height + weight)

#Conversion of pounds to centimeters and kilos
height_c = height/0.39370
weight_k = weight/2.2046

print "".rjust(8), "U.S.".rjust(4), "Metric".rjust(8)
print "weight", repr(weight).rjust(5), repr(weight_k).rjust(20)
print "height", repr(height).rjust(5), repr(height_c).rjust(21)

