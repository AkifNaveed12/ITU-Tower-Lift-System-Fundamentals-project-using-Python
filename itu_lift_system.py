def check_lift(lift_no, floor_no):
    # [lift no, no of passengers in lift, the floor on which lift is present]
    lift_1_info = [1,1,2]    
    lift_2_info = [2,0,11]     
    lift_3_info = [3,5,14]     
    lift_4_info = [4,4,10] 
    lift_5_info = [5,0,1]     
    lift_6_info = [6,5,5]     
    lift_7_info = [7,4,7]     
    lift_8_info = [8,3,3]
    
    go_floor_no = int(input("Enter the floor number you want to go (1 to 14): "))
    if lift_no == lift_1_info[0]:
        if lift_1_info[1] == 5:
            print("Really Sorry for the Inconvenience but the lift is full!\n Please try entering into another lift!")
        else:
            
            if  lift_1_info[2] > floor_no:
                print("The lift is currently on floor", lift_1_info[2]," The lift is coming down.")
                print("now the Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            elif lift_1_info[2] < floor_no:
                print("The lift is currently on floor", lift_1_info[2]," The lift is coming up.")
                print("now the Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            else:
                print("The lift is already on the",floor_no," floor you have entered\nyou can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
    elif lift_no == lift_2_info[0]:
        if lift_2_info[1]  == 5:
            print("Really Sorry for the Inconvenience but the lift is full!\n Please try entering into another lift!")
        else:
            
            if lift_2_info[2] > floor_no:
                print("The lift is currently on floor", lift_2_info[2]," The lift is coming down.")
                print("Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            elif lift_2_info[2] < floor_no:
                print("The lift is currently on floor", lift_2_info[2]," The lift is coming up.")
                print("Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            else:
                print("The lift is already on the ",floor_no," floor you have entered\nyou can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
    elif lift_no == lift_3_info[0]:
        if lift_3_info[1]  == 5:
            print("Really Sorry for the Inconvenience but the lift is full!\n Please try entering into another lift!")
        else:
            print("you can enter the lift")
            if lift_3_info[2] > floor_no:
                print("The lift is currently on floor", lift_3_info[2]," The lift is coming down.")
                print("Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            elif lift_3_info[2] < floor_no:
                print("The lift is currently on floor", lift_3_info[2]," The lift is coming up.")
                print("now the Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            else:
                print("The lift is already on the ",floor_no," floor you have entered\nyou can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
    elif lift_no == lift_4_info[0]:
        if lift_4_info[1]  == 5:
            print("Really Sorry for the Inconvenience but the lift is full!\n Please try entering into another lift!")
        else:
            
            if lift_4_info[2] > floor_no:
                print("The lift is currently on floor", lift_4_info[2]," The lift is coming down.")
                print("now the Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            elif lift_4_info[2] < floor_no:
                print("The lift is currently on floor", lift_4_info[2]," The lift is coming up.")
                print("now the Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            else:
                print("The lift is already on the ",floor_no,"floor you have entered\nyou can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
    elif lift_no == lift_5_info[0]:
        if lift_5_info[1]  == 5:
            print("Really Sorry for the Inconvenience but the lift is full!\n Please try entering into another lift!")
        else:
            
            if lift_5_info[2] > floor_no:
                print("The lift is currently on floor", lift_5_info[2]," The lift is coming down.")
                print("now the Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            elif lift_5_info[2] < floor_no:
                print("The lift is currently on floor", lift_5_info[2]," The lift is coming up.")
                print("now the Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            else:
                print("The lift is already on the ",floor_no,"floor you have entered\nyou can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)    
    elif lift_no == lift_6_info[0]:
        if lift_6_info[1]  == 5:
            print("Really Sorry for the Inconvenience but the lift is full!\n Please try entering into another lift!")
        else:
            
            if lift_6_info[2] > floor_no:
                print("The lift is currently on floor", lift_6_info[2]," The lift is coming down.")
                print("now the Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            elif lift_6_info[2] < floor_no:
                print("The lift is currently on floor", lift_6_info[2]," The lift is coming up.")
                print("now the Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            else:
                print("The lift is already on the ",floor_no,"floor you have entered\nyou can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
    elif lift_no == lift_7_info[0]:
        if lift_7_info[1]  == 5:
            print("Really Sorry for the Inconvenience but the lift is full!\n Please try entering into another lift!")
        else:
            
            if lift_7_info[2] > floor_no:
                print("The lift is currently on floor", lift_8_info[2]," The lift is coming down.")
                print("now the Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            elif lift_7_info[2] < floor_no:
                print("The lift is currently on floor", lift_7_info[2]," The lift is coming up.")
                print("now the Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            else:
                print("The lift is already on the ",floor_no,"floor you have entered\nyou can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
    else:
        if lift_8_info[1]  == 5:
            print("Really Sorry for the Inconvenience but the lift is full!\n Please try entering into another lift!")
        else:
            
            if lift_8_info[2] > floor_no:
                print("The lift is currently on floor", lift_8_info[2]," The lift is coming down.")
                print("now the Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            elif lift_8_info[2] < floor_no:
                print("The lift is currently on floor", lift_8_info[2]," The lift is coming up.")
                print("now the Lift is on floor", floor_no, "you can enter the lift")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)
            else:
                print("The lift is already on the ",floor_no,"floor you have entered")
                if go_floor_no == floor_no:
                    print("you are already on the desired floor number!")
                elif go_floor_no > floor_no:
                    print("The lift is moving up to floor", go_floor_no)
                else:
                    print("The lift is moving down to floor", go_floor_no)

choice = input("Are you already present in ARFA TOWER ? (yes(Y/y)/no(N/n)) ")   
if choice == "y" or choice == "Y":
    print("-------------------------------------Welcome to ARFA TOWER LIFT SYSTEM---------------------------------------------")
    floor_no = int(input("Enter the floor number on which currently you are present: "))
    lift_no = int(input("Enter the lift number on which you want to go: "))
    check_lift(floor_no,lift_no)
    print("-------------------------------------THANK YOU FOR USING ARFA TOWER LIFT SYSTEM---------------------------------------------")
else:
    print("-------------------------------------Welcome to ARFA TOWER---------------------------------------------")
    print("-------------------------------------Welcome to ARFA TOWER LIFT SYSTEM---------------------------------------------")
    floor_no = int(input("Enter the floor number on which currently you are present: "))
    lift_no = int(input("Enter the lift number on which you want to go: "))
    check_lift(floor_no,lift_no)
    print("-------------------------------------THANK YOU FOR USING ARFA TOWER LIFT SYSTEM---------------------------------------------")