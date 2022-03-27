# AssortedPrograms
programs that aren't large enough to be their own project, 
usually just tools to help with small tasks or to fulfill a curiosity.

# F1 Championship Permutations
Calculates the number of F1 championship permutations won by each driver given
the score system (number of available places) and driver's points (number of
drivers).

Small efficiency adjustments matter a lot because the number of total permutations
is ((n!/(n-r)!)^c) * n where n is the number of positions, r is the number of drivers,
and c is the number of races.

E.g., 20 positions with 3 championship contenders and 2 races left is
((20!/(20-3)!)^2) * 20 = 935,712,000 permutations

# Evernote Week Divider
Small program, just prints out the monday of each week in a custom format
with an evernote divider for my personal calendar.

