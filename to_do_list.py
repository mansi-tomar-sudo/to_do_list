#to do list
def menu():
    print("welcome in to do list ! \n" \
    "please press \n" \
    "1. add tasks \n" \
    "2. view tasks \n" \
    "3. delete tasks \n" \
    "4. marks complete to task \n" \
    )

def add():
    f=open("list.txt","a")
    task=input("enter the task:")
    f.write(task)
    f.close()

def view():
    f=open("list.txt","r")
    data=f.readlines()
    print(data," ")
    f.close()

def delete():
    f=open("list.txt","r")
    data=f.readlines()
    lst=list(data)
    choice=int(input("enter the choice to delete:"))
    if choice > 0 and choice <= len(lst):
        lst.pop(choice-1)
    else:
        print("you enter wrong ")
    
    f.close()
    f=open("list.txt","w")
    for i in lst:
        f.write(i)
    f.close()
def marks_complete():
    f=open("list.txt","r")
    data=f.readlines()
    lst=list(data)
    for i in range(len(lst)):
        print(i+1,",",lst[i])
    user=int(input("enter the task number which is complete:"))
    if user > 0 and user <= len(lst):
        lst[i]="[✓] " + lst[i]
    else:
        print("wrong input")
    f = open("list.txt", "w")

    for i in lst:
        f.write(i)

    f.close()
while True:
    menu()
    ch=int(input("enter the number:"))
    if(ch==1):
        add()
    if(ch==2):
        view()
    if(ch==3):
        delete()
    if(ch==4):
        marks_complete()
    if(ch>=6):
        print("please enter the correct value")
    


    


        
    

