def add_2(a):
    return a+2
iter_list = [2,3,5]
added_2 = map(add_2, iter_list)
print(added_2)
print(list(added_2))

doubled = map(lambda input: input+2, iter_list)
print(list(doubled))