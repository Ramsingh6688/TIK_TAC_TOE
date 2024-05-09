# def simple_generatorfun():
#     yield 1
#     yield 2
#     yield 3
    
# for value in simple_generatorfun():
#     print(value)
    
# def minus(x,y):
#      return x-y
# print(minus(9, 4))

# x = lambda a : a*2
# print(x( 4))

# x = lambda x,y, z : (x+y+z)/3
# print(x(3, 5, 10))

# x = lambda x, y : x+y
# print(x(3,4))

# marks = [20, 30, 40, 50, 60]

# new_marks = []
# for x in marks:
#     new_marks.append(x+2)
# print(new_marks)
# new_marks = [x+2 for x in marks]
# print(new_marks)
    
# dict1 = { }
# for i in range(10):
#     if i % 2 ==0:
#         dict1[i] = i * i
#         print(dict1)
        
# dict1 = {i: i*i for i in range(10) if i % 2 == 0}
# print(dict1)

# class person:
#     name = "Anuj"
#     occupation = "software Developer"
#     networth = 30
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")
        
# class first:
#     x = 50
# obj=first()
# print(obj.x)

# class Car:
#     name = "ROLLS ROYCE"
#     color = "Black"
#     manufacture = "2024"
# car1 = Car()
# print(car1.name)
# print(car1.color)
# print(car1.manufacture)

# class Student:
#     college_name = "university of technology"
#     def __init__(self, fullname, Marks):
#         self.name = fullname
#         self.Mark = Marks
#         print("adding new name of students..")
        
# s1 = Student("Anuj", 69)
# print(s1.name, s1.Mark)

# s2 = Student("pradeep", 89)
# print(s2.name, s2.Mark)

# print(s2.college_name)


##TIC TAK TOE


def sum(a, b, c):
    return a + b + c 

def printBoard(xstate, zstate):
    zero = 'x' if xstate[0] else ('0' if zstate[0] else 0)
    one = 'x' if xstate[1] else ('0' if zstate[1] else 1)
    two = 'x' if xstate[2] else ('0' if zstate[2] else 2)
    three = 'x' if xstate[3] else ('0' if zstate[3] else 3)
    four = 'x' if xstate[4] else ('0' if zstate[4] else 4)
    five = 'x' if xstate[5] else ('0' if zstate[5] else 5)
    six = 'x' if xstate[6] else ('0' if zstate[6] else 6)
    seven = 'x' if xstate[7] else ('0' if zstate[7] else 7)
    eight = 'x' if xstate[8] else ('0' if zstate[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")
    
def Checkwin(xstate, zstate):
    wins = [[0, 1, 2 ], [3, 4 , 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3):
            print("x won the match")
            return 1
        if(sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3):
            print("0 won the match")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to Tic tac toe ")
    while(True):
        printBoard(xState, zState)
        if(turn == 1):
          print("x's chance")
          value = int(input("please enter a value: "))
          xState[value]= 1
        else:
            print("0's chance")
            value = int(input("please enter a value: "))
            zState[value] = 1
        cwin = Checkwin(xState, zState)
        if(cwin != -1):
            print("Match over")
            break
        
        turn = 1 - turn