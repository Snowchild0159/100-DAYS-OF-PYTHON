
#Don't change the code below
row1 =  ['⬜️' , '⬜️' , '⬜️']
row2 =  ['⬜️' , '⬜️' , '⬜️']
row3 =  ['⬜️' , '⬜️' , '⬜️']

map = [row1, row2, row3]
position = input("Where do you want to put the treasure?")
#Don't change the code above

treasure = int(position[0])
treasure1 = int(position[1])
map[treasure][treasure1]="x"

print(f"{row1}\n{row2}\n{row3}")