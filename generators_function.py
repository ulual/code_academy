def return_evens(lst):
    for l in lst:
        if l % 2 == 0:
            yield l

eggs = [x for x in range(200)]

#print(list(return_evens(eggs)))

spam = (x for x in eggs if x % 4 == 0)

print(next(spam))
print(next(spam))
