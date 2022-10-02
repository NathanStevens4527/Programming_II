import random

print(random.randint(5, 20))  # line 1
#11 was the number printed for line 1.
#5 is the smallest that could be seen and 20 is the largest.
print(random.randrange(3, 10, 2))  # line 2
#7 was the number printed for line 2.
#3 is the smallest number possible and 9 is the largest as the step is 2 so ten cannot be seen.
#line 2 could not produce a 4 as the step is 2 and the minimum inclusive is 3.
print(random.uniform(2.5, 5.5))  # line 3
#5.269354931431106 is what was printed for line 3
#2.5 is the smallest number possible and 5.5 was the largest.