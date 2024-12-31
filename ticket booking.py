tkts =[1,2,3,4,5]
print('avible tickets',tkts)
user_intput = int(input('enter how many tickets u wanna buy:'))
for x in range(user_intput):
    ticket_num = int(input('enter tkts number:'))
    tkts.remove(ticket_num)
print('avible tkts',tkts)


