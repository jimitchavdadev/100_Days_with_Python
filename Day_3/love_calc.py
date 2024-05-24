print("The Love Calculator is calculating your score...")
name1=input("What is your name? ")
name2=input("What is their name? ")
name3=(name1+name2).lower()
Tcount=0
Lcount=0
for i in name3:
    if i=='t':
        Tcount+=1
    elif i=='r':
        Tcount+=1
    elif i=='u':
        Tcount+=1
    elif i=='e':
        Tcount+=1
        Lcount+=1
    elif i=='l':
        Lcount+=1
    elif i=='o':
        Lcount+=1
    elif i=='v':
        Lcount+=1

total=Tcount*10+Lcount

if total<10 or total >90:
    print(f"our score is {total}, you go together like coke and mentos.")
elif total >=40 or total <=50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"your score is {total}")