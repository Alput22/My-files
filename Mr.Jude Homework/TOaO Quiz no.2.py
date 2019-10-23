#%%
Almada Putra A.

2.
#%%
filename = r'C:\Users\hp\Desktop\Mada\Homework\new\data.txt'

class Display:
    def __init__(self):
        self.id = ID
        self.name = Name
        self.position = Pos
        self.salary = Salary
    @classmethod
    def display(self):
        for da in open(filename):
            data = da.rstrip().split('#')
            print(data)
    def choice():
        choose = input("1.New Staff" +"\n2.Delete Staff" + "\n3.View Summary Data" + "\n4.Save & Exit" + "\ninput number: ")
        
    def conseq():
        if (choose == 1):
            Number.newstaff()

class Number:
    def __init__(self):
        self.id = ID
        self.name = Name
        self.position = Pos
        self.salary = Salary
        
    def newstaff():
        num = ['0','1','2','3','4','5','6','7','8','9']
        while True:
            ID = input('Welcome. Please enter your ID: ')
            if (len(ID) == 5):
                if (ID[0] == 'S'):
                   # if (ID[1][:6] == num):
                   #     if (ID not in filename):
                            break
                   #  else:
                    #     print('Try again.')
                else:
                    print('Try again.')
            else:
                print('Try again.')
        while True:
            Name = input('Enter your Name: ')
            if (len(Name) < 20):
                break
        while True:
            Positions = ['Staff','Officer','Manager']
            Pos = input('Enter your position: ')
            if (Pos == 'Staff','Officer','Manager'):
                break
        while True:
            Salary = int(input('Enter your salary: '))
            if (Pos == 'Staff'and Salary >= 3500000 and Salary <= 7000000):
                break
            elif (Pos == 'Officer' and Salary > 7000000 and Salary <= 10000000 ):
                break
            elif (Pos == 'Manager'and Salary > 10000000):
                break
        
Display.display()   
Display.choice()
    
        
