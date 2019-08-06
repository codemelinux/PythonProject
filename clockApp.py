
###Student ID: B1202330 ######
###Date: 30/04/2019 #####
###Student Name: Ugbaja Benedict #####

### importing time ######
from datetime import datetime


class Clock():
    def __init__(self, name, time, priority, displayType):

        self.name = str(name)
        time = int(time)
        #### converting time to 12hr #######
        d = datetime.strptime(str(time), "%H%M%S") 
        self.time = d.strftime("%I:%M %p").strip("0") 
        self.priority = str(priority) 
        self.displayType = str(displayType)

    ##### getter function #######
    def get_name(self):
        return self.name
    
    def get_time(self):
        return self.time
    
    def get_priority(self):
        return self.priority
    
    def get_displayType(self):
        return self.displayType

    ##### Setter function #####
    def set_name(self, nm):
        self.name = nm
    
    def set_time(self, tm):
        
        self.time = tm

    def set_priority(self, prior):
        self.priority = prior

    def set_displayType(self, dType):
        self.displayType = dType

    ##### Alarm Display ######

    def alarmDisplay(self, bgColor):
        return bgColor

    ##### equal function #####
    def __eq__(self, other):
        
        return self.displayType == other.displayType

    ##### less than function #####
    def __lt__(self, other):
        
        return self.time < other.time

    def __str__(self):        
          
        return "{} is set to {}. This alarm has {} priority and will be displayed in {} form.".format(self.name, self.time, self.priority, self.displayType)



##### defining a clockList class #####
class ClockList:
    def __init__(self, userName):
        self.userName = userName
        self.clock_list = []

    def get_userName(self): ## getter 
        return self.userName

    def get_clockList(self): ## getter
        return self.clock_list

    def set_userName(self, userName): ## setter
        self.userName = userName

    ### add clock ###
    def add_clock(self, newAlarm):
        self.clock_list.append(newAlarm)

    ###### remove clock #####
    def removeClock(self, rmClock):
       
        for i in self.clock_list:
            #### if user input is greater than or equals zero #####
            if rmClock >= 0:
                rmClock -= 1 ### subtract 1 from user input

                #### getting clocklist row based on user input ####
                remvDetails = self.clock_list[rmClock]
                if remvDetails == self.clock_list[rmClock]:
                    #### return removed clock information to user ##### 
                    clkDetails = (str(i.get_displayType())+" clock "+ str(i.get_name())+ " "+\
                         str(i.get_time())+" "+ str(i.get_priority())+" priority ")
        
        #### deletes clock based on users index input #####
        del self.clock_list[rmClock]
        return clkDetails

       
    #### number Of Clock #####
    def noOfClock(self):
        return len(self.clock_list)
    
    ###### display clock ######
    def displayClock (self):
        for i in self.clock_list:
           
            print(i.__str__())
           

    ##### checking numbers of each clock by Priority #####
    def totalClock(self):
        mid = []
        low = []
        high = []
        for i in self.clock_list:
            if i.get_priority() == "medium":
                mid.append(i.get_priority())

            elif i.get_priority() == "high":
                high.append(i.get_priority())

            elif i.get_priority() == "low":
                low.append(i.get_priority())

        totClock = {"low" : len(low), "medium" : len(mid), "high" : len(high)}
           
        return totClock
   

    ##### find clock by priority #######
    def findClockByPriority(self, findPrior):
        findClockList = []

        for i in self.clock_list:
            ###### comparing priority to users input ######
            if i.get_priority() == findPrior:
                ####### retrieve clock details #####
                convertedTime = datetime.strptime(str(i.get_time()), "%I:%M %p")
                convertedTime = datetime.strftime(convertedTime, "%H%M%S ")

                retrieveClk = (str(i.get_name())+" " + convertedTime +" " + str(i.get_displayType()))
                findClockList.append(retrieveClk)
                #### formating clock details #######
                clk = ("\n".join("".join(str(element) for element in row) for row in findClockList))
            else:
                clk =("not found")
                
        return clk

    ####### getting latest clock #######
    def latestClock(self):
        laTestClkList = []
        for i in self.clock_list:
            clkList = self.clock_list
            Clk = min(clkList) ### sorting clock by Max #####
            #### comparing time with clock max value ####
            if i.get_time() == Clk.get_time():
                ##### retrieving clock with latest value ###
                latstClk = (str(i.get_name())+", " + str(i.get_time())+", " +  str(i.get_priority()) + " priority, " + str(i.get_displayType())+" form.")
                laTestClkList.append(latstClk)
                ###### formating output ####
                clk = ("\n".join("".join(str(element) for element in row) for row in laTestClkList))

        return clk

    ##### Total clock by display type #########
    def totalClockByDisplay(self, clkType):
        dspTypeList = []
        for i in self.clock_list:
            ### comparing display type with user input ####
            if i.get_displayType() == clkType:
                dspTypeList.append(self.clock_list)
               
        return len(dspTypeList)


    ###### Save clock list ######
    def saveToFile(self, saveFile):
        svgFileList = []
        ### getting input from user ####
        userInput = open(saveFile, 'w')
        for i in self.clock_list:
            ### retrieving clocklist save format #####
            clkLst = (str(i.get_name()),str(i.get_time()), str(i.get_priority()),str(i.get_displayType()))
            svgFileList.append(clkLst)
        #### formating txt file output #####
        userInput.writelines("\n".join(",".join(str(element) for element in row) for row in svgFileList))


     
    ###### Load from file ######
    def loadFromFile(self, retrieveFile):
        userInput = open(retrieveFile, 'r')
        for i in userInput:
            nwClk = (i.split(","))
            #### passing the retrieved file to clock class #######
            convertedTime = datetime.strptime(nwClk[1], "%I:%M %p")
            convertedTime = datetime.strftime(convertedTime, "%H%M%S ")
            alarm = Clock(nwClk[0],int(convertedTime), nwClk[2], nwClk[3])
            ##### adding clock to list #######
            self.clock_list.append(alarm)
            
               
              

