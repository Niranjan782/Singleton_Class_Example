def SingleTon(arg):
    L=[]
    def Inner():
        if len(L)==0:
            obj=arg()
            L.append(obj)
        return L[0]
    return Inner

@SingleTon
class NPCB():
    def __init__(self):
        self.Totaltic=200
    def Booking(self):
        reqtic=int(input("Enter the number of tickets: "))
        if reqtic <= self.Totaltic:
            print("Tickets booked Successfuly")
            self.Totaltic -= reqtic
            print(f'Available Tickets are {self.Totaltic}')
        else:
            print("Tickets Not Available")


def Paytm():
    print("Welcome to Paytm Theater")
    user=NPCB()
    user.Booking()

def BookMyShow():
    print("Welcome to BookMyShow Theater")
    user=NPCB()
    user.Booking()

def TicketNew():
    print("Welcome to TicketNew Theater")
    user=NPCB()
    user.Booking()


def PVR():
    print("Welcome to PVR Theater")
    user=NPCB()
    user.Booking()

user1=Paytm()
print('-'*20)
user2=BookMyShow()
print('-'*20)
user3=TicketNew()
print('-'*20)
user4=PVR()
print('-'*20)
user5=Paytm()
