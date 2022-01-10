# 1. Countdown
def countdown(num):
    new_list = []
    i = 0
    for i in range(num + 1):
        num = num - 1
        new_list.append(num + 1)
        
    return new_list
print(countdown(5))

def countdown(num):
    new_list = [num]
    i = 0
    for i in range(num):
        num = num - 1
        new_list.append(num)
        
    return new_list
print(countdown(5))

# 2. Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,4]))

# 3. First Plus Length
def first_plus_length(list):
    my_sum = list[0] + len(list)
    return my_sum
print(first_plus_length([2,5,3,7,3,1,3,0,6,4]))

# 4. Values Greater Than Second
def values_greater_than_second(list):
    new_list = []
    for i in range(len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
    print(len(new_list))
    return new_list
print(values_greater_than_second([3,2,7,8,0,4,3]))

# 5. This Length, That Value
def this_length_that_value(a,b):
    new_list = []
    for i in range(a):
        new_list.append(b)
    return new_list
print(this_length_that_value(5,6))
