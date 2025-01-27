def show():
    tkts=[1,2,3,4,5]
    print('avilble tickets')
    for x in tkts:
        print(x)
class bus_booking:
    def book_tkt(self):
      show()
      user=input('how many tickest:')
      for x in range(user):
          tkt_no=int(input('enter seat number:'))
          if tkt_no in tkts:
              print('Ticket is bookes')
              tkts.remove(tkt_no) 
        else:
ola=bus_booking()
