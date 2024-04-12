
print("Ich bin ein Tic-Tac.Toe Programm")
my_list = [[3, 3, 3],[3, 3, 3],[3, 3, 3]]
def Print(list):
    counter = 0
    for i in range(0, 3):
        print("=========", end="\n")
        for j in range(0,3):
            
            if list[i][j] == 1:
                print("|X|", end="")
            elif list[i][j] == 2:
                print("|O|", end="")
            elif list[i][j] ==3:
                print("| |", end="")
            elif list[i][j] ==4:
                print("|#|", end="")
            counter += 1
        print("", end="\n")
    print("=========", end="\n")



def move(color):
    x = int(input(""))
    y = int(input(""))
    my_list[x - 1][y - 1] = color




def Game():
    
    counter = 1
    while True:
        counter += 1
        if counter % 2:
            color = 1
        else:
            color = 2
        move(color)
        Print(my_list)
    

Game()