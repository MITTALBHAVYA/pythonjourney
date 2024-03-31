import random
matrix=[['D','W','L'],['L','D','W'],['W','L','D']]
choose=[0,1,2]
print("Welcome to ---SNAKE--- ---WATER--- ---GUN--- game:\n")
while True:
    print("Enter you choice \n")
    print("0 for Snake\n")
    print("1 for Water\n")
    print("2 for Gun\n")
    op=int(input())
    print(matrix[op][random.choice(choose)])
    print("Wanna play again choose 1 to quit press -1\n")
    tra=int(input())
    if tra==-1:
        break 