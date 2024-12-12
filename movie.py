def SingleTon(arg):
    L=[]
    def Inner():
        if len(L)==0:
            obj=arg()
            L.append(obj)
        return L[0]
    return Inner
@SingleTon
class Movie1():
    def __init__(self):
        self.Totaltic=200
    def Booking(self):
        reqtic=int(input("Enter the number of tickets: "))
        if reqtic <= self.Totaltic:
            print("Tickets booked Successfuly")
            self.Totaltic -= reqtic
            print(f'Available Tickets are {self.Totaltic}')
        else:
            print("Tickets Not=Available")
@SingleTon
class Movie2():
    def __init__(self):
        self.Totaltic=200
    def Booking(self):
        reqtic=int(input("Enter the number of tickets: "))
        if reqtic <= self.Totaltic:
            print("Tickets booked Successfuly")
            self.Totaltic -= reqtic
            print(f'Available Tickets are {self.Totaltic}')
        else:
            print("Tickets Not=Available")

@SingleTon
class Movie3():
    def __init__(self):
        self.Totaltic=200
    def Booking(self):
        reqtic=int(input("Enter the number of tickets: "))
        if reqtic <= self.Totaltic:
            print("Tickets booked Successfuly")
            self.Totaltic -= reqtic
            print(f'Available Tickets are {self.Totaltic}')
        else:
            print("Tickets Not=Available")

def Paytm():
    print("Welcome to Paytm Theater")
    print(" 1)Movie1 \n 2) Movie2 \n 3) Movie3")
    choice=int(input("Enter the movie choice: "))
    if choice==1:
        user=Movie1()
        user.Booking()
    elif choice==2:
        user=Movie2()
        user.Booking()
    elif choice==3:
        user=Movie3()
        user.Booking()
    else:
        print("No Screen Avalilable")

user1=Paytm()
print('-'*20)
user2=Paytm()
print('-'*20)
user3=Paytm()
print('-'*20)
user4=Paytm()
print('-'*20)
