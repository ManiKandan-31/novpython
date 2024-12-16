# num=int(input("enternumber:"))
# if num<0:
#     print("-ve num")
# elif num>0:
#     print("+ve num")
# else:
#     print("num is zero")1






maths=int(input("enter maths mark:"))
phy=int(input("enter phys mark:"))
chem=int(input("enter chem mark:"))
total_marks=600
sum_marks=maths+phy+chem
per=(sum_marks/total_marks)*100
print(per)
if per<35:
    print('Grade is F')
elif per>35 and per<=50:
     print('Grade is C')
elif per in range(51,91):
      print('Grade is B')
elif per in range(91,101):
      print('Grade is A')
else:
      print('Invaid per')