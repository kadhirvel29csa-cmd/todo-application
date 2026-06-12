tasks={}
while(True):
    try:
        print("-------------------------------------------------------------------------")
        print("                                                  TODO                                                       ")
        print("-------------------------------------------------------------------------")
        print("1.Add")
        print("2.View")
        print("3.Mark complete")
        print("4.Delete")
        print("5.Exit")
        a = int(input("Enter Your Choice:"))
        if(a==1):
            task = input("Enter the task:")
            tasks[task]="pending"
            print("Task added!")
        elif(a==2):
             print("-------------------------------------------------------------------------")
             print("                                                  TASK LIST                                                       ")
             print("-------------------------------------------------------------------------")
             if not tasks:
                    print("No task available")
             else:
                    for i,(e,x) in enumerate(tasks.items(),start=1):
                             print(i,e,"-",x.capitalize())
        elif(a==3):
                 c=input("Enter the task name:")
                 if c in tasks:
                        tasks[c]="completed"
                        print("Task marked as complete")
                 else:
                        print("Task not found!")
               
        elif(a==4):
                d = input("Enter the task name:")
                if d in tasks:
                       del tasks[d]
                       print("Task deleted!")
                else:
                       print("Task not found")
               
        elif(a==5):
                print("Thanks for using todo,complete the job asap!")
                break
        else:
            print("Enter the valid choice 1-5")
    except ValueError:
               print("Enter the valid number!")
               continue
     
          
    
  

       

    
