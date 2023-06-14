#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    a = 0
    b = 0
    for i in range(len(my_list)):
        a += ((int(my_list[i][0])) * (int(my_list[i][1])))
        b += ((int(0)) + (int(my_list[i][1])))
    return a / b
