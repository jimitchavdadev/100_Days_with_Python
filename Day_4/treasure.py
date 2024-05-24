list1=[" "," "," "]
list2=[" "," "," "]
list3=[" "," "," "]

map=[list1,list2,list3]
print("where do you want to hide your treasure? ")
position=input()
map[int(position[0])][int(position[1])]="🪙"
print(f"{list1}\n{list2}\n{list3}")