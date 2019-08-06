###Student ID: B1202330 ######
###Student Name: Ugbaja Benedict #####
###Date: 30/04/2019 #####

import clockApp
from datetime import datetime
def main():

    menu()
    
def menu():
    print()
    userName = input("Enter user's name: ")
    #### getting user name #####
    newClockList= clockApp.ClockList(userName)
    
    choice = ''
    # Starting a while loop that runs until the user enters the value for 0 to quit.
    while choice != '0':
        # adding user options in series of print.
    
        print()
        print("Alarm Clock Application")
        print('---------------------------------------------------------------')
        print("1 Add an alarm clock ")
        print("2 Remove clock based on given index ")
        print("3 Display number of clock in list ")
        print("4 Display all clock in the list ")
        print("5 Display total alarm clock by priority ")
        print("6 Display clock with the latest time ")
        print("7 Display clock with user-specified priority ")
        print("8 Display total number of clock based on user-specific display type ")
        print("9 Read clock information from file")
        print("10 Write clock information to file")
        print("0 - Quit")
    
        # Accepting users choice.
        choice = input("\nYour choice? ")
    
        # Respond to the user's choice.
        #.............. Choice 1.................
        if choice == '1':
            clockName = input("\nName Of Clock? ")
            newTime = int(input("Time? "))

            while True:
                priorInput = input("Priority ('H/M/L') ? ")
                if priorInput.lower() in {"h","m","l"} != True :

                 ### recieves both uppercase and lowercase from user ###
                 
                    if priorInput == "h" or priorInput == "H":       
                        nPriority = 'high'
                    
                    elif priorInput == "m" or priorInput == "M":
                        nPriority = 'medium'

                    elif priorInput == "l" or priorInput == "L":
                        nPriority = 'low'
                    
                    break
                else:
                    print('Invalid type! Please enter again!')
                    

            while True :
                displayType = input("Display Type ('A/D') ? ")
                if displayType.lower() in {"a","d"} != True:
                        
                    if displayType == "a" or displayType == "A":
                        dType = 'analog'
                    elif displayType == "d" or displayType == "D":
                        dType = 'digital'
                    break
                else:
                    print('Invalid Value! Please enter again!')
                    
             ### passing user input to Clock class ###
            alarm = clockApp.Clock(clockName,newTime, nPriority, dType)
            ### add method ###
            newClockList.add_clock(alarm)
           
            print("... Clock has been added successfully")
                    
                            
        #.............. Choice 2.................
        elif choice == '2':
            if (len(newClockList.get_clockList())) == 0:
                print("\nNo clock registered for", newClockList.get_userName())
                menu
            else:
                while True:
                    #### remove clock ####
                    delClock = int(input("Which clock details to remove? "))
                    ## validate for input of zero ###
                    if delClock in {0} != True:
                        print("Invalid index. Try again!")
                    else:
                        rmdClock = newClockList.removeClock(delClock)
                        print(" Clock with index "+ str(delClock) +": { " + str(rmdClock)+ "} has been removed !")
                        break
               
                
        #.............. Choice 3.................           
        elif choice == '3':
            if (len(newClockList.get_clockList())) == 0:
                print("\nNo clock registered for", newClockList.get_userName())
                menu
            else:
                ### display number of clock in the list ###
                print("Total clock in user’s list: " + str(newClockList.noOfClock()))
                         
                
        #.............. Choice 4.................
        elif choice == '4':
            if (len(newClockList.get_clockList())) == 0:
                print("\nNo clock registered for", newClockList.get_userName())
                menu
            else:
                ### print all clock in list ###
                print("All clock in this list:")
                newClockList.displayClock()

                     
        #.............. Choice 5.................
        elif choice == '5':
            if (len(newClockList.get_clockList())) == 0:
                print("\nNo clock registered for", newClockList.get_userName())
                menu
            else:
                #### displays total alarm clock by priority ####
                totClock = newClockList.totalClock()
                print("Total clock with low priority: " + str(totClock.get("low")))
                print("Total clock with medium priority: " + str(totClock.get("medium")))
                print("Total clock with high priority: " + str(totClock.get("high")))


        #.............. Choice 6.................
        elif choice == '6':
            if (len(newClockList.get_clockList())) == 0:
                print("\nNo clock registered for", newClockList.get_userName())
                menu
            else:
                ### Displays clock with latest time ###
                print("Clock with latest time: ")
                print(str(newClockList.latestClock()))

        #.............. Choice 7.................
        elif choice == '7':
            if (len(newClockList.get_clockList())) == 0:
                print("\nNo clock registered for", newClockList.get_userName())

                menu
                
            else:
                while True:
                    priorInput = input("Priority ('H/M/L') ? ")
                    if priorInput.lower() in {"h","m","l"} != True :
                 
                        if priorInput == "h" or priorInput == "H":
                            nPriority = 'high'
                    
                        elif priorInput == "m" or priorInput == "M":
                            nPriority = 'medium'

                        elif priorInput == "l" or priorInput == "L":
                            nPriority = 'low'

                        ### display clock by user specified priority ####
                        clk = newClockList.findClockByPriority(nPriority)
                        print(nPriority +":")
                        print(clk)  
                    
                        break
                    else:
                        print('Invalid type!')   
                
           
        #.............. Choice 8.................
        elif choice == '8':
            if (len(newClockList.get_clockList())) == 0:
                print("\nNo clock registered for", newClockList.get_userName())
                menu
            else:
                while True:
                    displayType = input("Display Type ('A/D') ? ")
                    if displayType.lower() in {"a","d"} != True :
                    
                        if displayType == "a" or displayType =="A":
                            dType = 'analog'
                        elif displayType == "d" or displayType =="D":
                            dType = 'digital'

                            #### total number of clock based on display type ####
                        clkType = newClockList.totalClockByDisplay(dType)
                        print("Total clock to be displayed in " + dType +" form: "+ str(clkType))
                        break
                    else:
                        print('Invalid Value! Please enter again!')
                                     

        #.............. Choice 9.................
        elif choice == '9':
            #### gets a .txt file ####
            loadFile = input("Please enter filename to load from: ")
            newClockList.loadFromFile(loadFile)
            print("File loaded successfully")

        #.............. Choice 10.................
        elif choice == '10':
            if (len(newClockList.get_clockList())) == 0:
                print("\nNo clock registered for", newClockList.get_userName())
                menu
            else:
                #### save clocklist #####
                saveFile = input("Please enter filename to save to: ")
                newClockList.saveToFile(saveFile)
                print("File saved successfully")
            
                
        #.............. Choice Quit.................
        elif choice == '0':
            print("\nExiting Menu.\n")
        else:
            print("\nInvalid choice! Please select from the list of choices.")
        
    # Print a message that we are all finished.
    print("Thank you for using this program.")
    
    return choice

# Main Program
if __name__ == "__main__":
    # Launch main 
    main()
