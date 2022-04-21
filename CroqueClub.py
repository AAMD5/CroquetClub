# Senior must be age <= 55 and handicap > 7.
# Handicaps -2 <= Handicap <= 26.
# The better the player the lower the handicap.

# Input will consist of a list of pairs. Each pair 
# contains information for a single potential member. 
# Information consists of an integer for the person's 
# age and an integer for the person's handicap. """

# Output will consist of a list of string values stating 
# whether the respective member is to be placed in the 
# senior or open category.

# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]  

#         age, handicap
myInput = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]

def seniorOrOpen(pairList):
    Output = []
    for pair in pairList:
        if pair[0] >= 55 and pair[1] > 7:
            Output.append("Senior")
            #print(pair, "is Senior")
        else:
            Output.append("Open")
            #print(pair, "is Open")
    return pairList, Output

print("Your input list is:", seniorOrOpen(myInput)[0])        
print("Your output list is:", seniorOrOpen(myInput)[1])
        
