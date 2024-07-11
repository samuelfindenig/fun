from ntpath import join
import time

def frame(text, symble):
    print((len(text)+4)*str(symble))
    print(str(symble) + " " + str(text) + " " + str(symble))
    print((len(text)+4)*str(symble))

def output(text):
    alphapeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZß abcdefghijklmnopqrstuvwxyz"
    output = []
    for i in range(0, len(text)):
        x = 0
        while text[i] != alphapeth[x]:
            print("".join(output) + str(alphapeth[x]))
            x += 1
            time.sleep(0.08)
        print("".join(output) + str(alphapeth[x]))
        output.append(alphapeth[x])
    frame("".join(output), "#")

    
 
output(str(input("Bitte geben sie den Text ein der geprintet werden soll: ")))

