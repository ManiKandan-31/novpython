lst =[1,2,3,4,1,2]
emp_lst =[]
dupt_lst=[]
for x in lst: 
    if x not in emp_lst:
        emp_lst.append(x) 

    else:
        dupt_lst.append(x) 
print(emp_lst,dupt_lst)



