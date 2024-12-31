# print([x for x in [1,3,4,5,6,7] if x %2 == 1])

val =[1,2,3.4,5,6,7]
print([f'even value{x}' if x%2 ==0 else f'{x} odd value' for x in val])