usd_to_inr=83    #converting usd to inr   
age=int(input("enter the age:"))
if age in range(18,31):        #age>18 and age<30
    price=5*usd_to_inr
    print(f"your ticket price is:₹{price}" )
elif age in range(30,51):      #age>30 and age<50
    price=30*usd_to_inr
    print(f"your ticket price:₹{price}")
elif age>50:
    print(f"your ticket is free")
else:
    print("your not eligble to atten  match")
