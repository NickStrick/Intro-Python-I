#return the centered average of an array of ints,
# which well say is the mean average of the values,
# except ignoring the largetst and smallest values in the array.

# [1,2,3,4,100]  - 3
#[1,1,5,5,10,8,7]  - 5
# [-10,-4,-2,-4,-2, 0]  - -3
# centered_average()

#Understand
# "mean average": 2, 3, 4 --> 3
# are arrays sorted? NO
# are all values different, or are some duplicate? some are duplicate
# assumption: we will always have 3 or more values
# no mutating the list
# maybe non-integers

#Plan
# how to get largest and smallest?

def centered_average(a_list):
    # make a copy
    # sort list
    # slice the list to exclude the first and last elements
    # sum the list

    copy_list = a_list.copy()
    copu_list.sort()
    list_to_sum = copy_list[1:-1]
    return sum(list_to_sum)/len(list_to_sum)

print(centered_average([1,2,3,4,100])) #3

#Reflect
# duplicate list --> space complexity
# MOAR tests