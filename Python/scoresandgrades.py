#scores and grades

import math
import random

count = 10

while count > 0:
    scores = math.trunc(random.random()*41)+60
    if 60 <= scores <= 69:
        print "Score:", str(scores) +":", "Your grade is a D"
        count -= 1
    elif 70 <= scores <= 79:
        print "Score:", str(scores) +":", "Your grade is a C"
        count -= 1
    elif 80 <= scores <= 89:
        print "Score:", str(scores) +":", "Your grade is a B"
        count -= 1
    else:
        print "Score:", str(scores) +":", "Your grade is a A"
        count -= 1
