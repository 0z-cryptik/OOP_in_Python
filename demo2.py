a, b = 2, 3

print(a.__add__(b))
print(b.__rmul__(a))
print(~b)

check_str = 'abakaliki'
check_list = 'a b a k a l i k i'.split()

if 'i' in check_list:
    print(True)
else:
    print(False, check_list)

#results in an array of 5 zeros
print([0] * 5)