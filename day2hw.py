
# Exercise 1
# Given a list as a parameter,write a function that returns a list of numbers that are less than ten
# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]
# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]

def less_than_ten(l_1):
    new_list=[]
    for number in l_1:
        if number < 10:
            new_list.append(number)
        else:
            continue
    return new_list
print(less_than_ten(l_1))
#with different list
l_1 = [1,11,14,5,8,9,100,20,-1]
print(less_than_ten(l_1))


# Exercise 2
# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def merged_list(l_1,l_2):
    l_3= l_1 + l_2
    l_3.sort()
    return l_3
print(merged_list(l_1,l_2))

#another approach
def merged_list2(l_1,l_2):
    return sorted(l_1 +l_2)
print(merged_list2(l_1,l_2))
