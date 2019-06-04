#todo: implement cascading deletion
 #todo: implement labeling point in price number

import pymysql, sys, math
import sqlStatementVundle as sqlv
import dataType as d

#run query statement input as argument
def runQuery(statement):
        cursor.execute(statement)
        result=cursor.fetchall()
        #print('result: {0}'.format(result))
        return result

def runQuery1Arg(statement, str1):
        cursor.execute(statement, (str1))
        result=cursor.fetchall()
        #print('result: {0}'.format(result))
        return result

def runQuery2Arg(statement, str1, str2):
        cursor.execute(statement, (str1,str2))
        result=cursor.fetchall()
        #print('result: {0}'.format(result))
        return result

def runQuery3Arg(statement, str1, str2, str3):
        cursor.execute(statement, (str1, str2, str3))
        result=cursor.fetchall()
        #print('result: {0}'.format(result))
        return result

def truncateString(rawString):
        return rawString[:200]

def addCommas(val):
        return format(val,",")

def checkDB():
        cursor.execute('''show tables;''')
        dbTuples = cursor.fetchall()
        #print('result: {0}'.format(dbTuples))
        
        theaterExist=False
        playExist=False
        audienceExist=False
        bookingExist=False
        
        for dbName in dbTuples:                
                if 'theater' in dbName:
                        theaterExist = True
                elif 'play' in dbName:
                        playExist = True
                elif 'audience' in dbName:
                        audienceExist = True
                elif 'booking' in dbName:
                        bookingExist = True
        if theaterExist is False:
                runQuery(sqlv.crtTheater)
        if playExist is False:
                runQuery(sqlv.crtPlay)
        if audienceExist is False:
                runQuery(sqlv.crtAudience)
        if bookingExist is False:
                runQuery(sqlv.crtBooking)
        
def resetDB():
        cursor.execute('''show tables;''')
        dbTuples = cursor.fetchall()
        #print('result: {0}'.format(dbTuples))
        for dbName in dbTuples:
                        
                if 'theater' in dbName:
                        #drop table theater
                        runQuery(sqlv.dropTheater)
                if 'play' in dbName:
                        #drop table play
                        runQuery(sqlv.dropPlay)
                if 'audience' in dbName:
                        #drop table audience
                        runQuery(sqlv.dropAudience)
                if 'booking' in dbName:
                        #drop table booking
                        runQuery(sqlv.dropBooking)
        
        #create theater table
        runQuery(sqlv.crtTheater)
        
        #create play table
        runQuery(sqlv.crtPlay)
        
        #create audience table
        runQuery(sqlv.crtAudience)
        
        #create booking table
        runQuery(sqlv.crtBooking)
        
def sortTuple(tuple1):
        x=list(tuple1)
        x.sort()
        return tuple(x)
                
def printQuery():
       que = '============================================================\n1. print all buildings\n2. print all performances\n3. print all audiences\n4. insert a new building\n5. remove a building\n6. insert a new performance\n7. remove a performance\n8. insert a new audience\n9. remove an audience\n10. assign a performance to a building\n11. book a performance\n12. print all performances which assigned at a building\n13. print all audiences who booked for a performance\n14. print ticket booking status of a performance\n15. exit\n16. reset database\n============================================================\nSelect your action:'
       print(que, end=' ')

def discountRate(age):
        if age <= 7:
                return 0.0
        elif age <= 12:
                return 0.5
        elif age <= 18:
                return 0.8
        else:
                return 1.0

def doCommand(queUser):
        if queUser=='1':
                tmp1=runQuery(sqlv.printTheater)
                print("--------------------------------------------------------------------------------")
                lineIndex = 'id'.ljust(5) + 'name'.ljust(20) + 'location'.ljust(30) + 'capacity'.ljust(10) + 'assigned'.ljust(10)
                print(lineIndex)
                print("--------------------------------------------------------------------------------")        
                for theaterRecord in tmp1:
                        word=theaterRecord
                        tmp1_1=runQuery1Arg(sqlv.countTheaterInPlay, str(word[0]))
                        lineNew = str(word[0]).ljust(5) + word[1].ljust(20) + word[2].ljust(30) + str(word[3]).ljust(10) + str(tmp1_1[0][0]).ljust(10)

                        print(lineNew)

                        
                print("--------------------------------------------------------------------------------")                

        elif queUser=='2':
                tmp2=runQuery(sqlv.printPlay)
#                print(tmp2)
                print("--------------------------------------------------------------------------------")
                lineIndex = 'id'.ljust(5) + 'name'.ljust(30) + 'type'.ljust(20) + 'price'.ljust(10) + 'booked'.ljust(10)
                print(lineIndex)
                print("--------------------------------------------------------------------------------")        
                for playRecord in tmp2:
                        word=playRecord
                        tmp2_1=runQuery1Arg(sqlv.selectAudienceIdInBookingUsingPlayId,str(word[0]))
                        lineNew = str(word[0]).ljust(5) + word[1].ljust(30) + word[2].ljust(20) + str(word[3]).ljust(10) + str(len(tmp2_1)).ljust(10)
                        print(lineNew)
                        
                print("--------------------------------------------------------------------------------")

                # Need additional manipulation for loading the number of booked audience

        elif queUser=='3':
                tmp3=runQuery(sqlv.printAudience)
                #print(tmp3)
                print("--------------------------------------------------------------------------------")
                lineIndex = 'id'.ljust(5) + 'name'.ljust(30) + 'gender'.ljust(20) + 'age'.ljust(10)
                print(lineIndex)
                print("--------------------------------------------------------------------------------")        
                for audienceRecord in tmp3:
                        word=audienceRecord
                        lineNew = str(word[0]).ljust(5) + word[1].ljust(30) + word[2].ljust(20) + str(word[3]).ljust(10)
                        print(lineNew)
                        
                print("--------------------------------------------------------------------------------")


        elif queUser=='4':
                print('Building name:', end=' ')
                buildingName=truncateString(input())
                print('Building location:', end=' ')
                buildingLocation=truncateString(input())
                print('Building capacity:', end=' ')
                buildingCapacity=int(input())

                tmp=d.Theater(buildingName, buildingLocation, buildingCapacity)
                
                if(buildingCapacity <= 0):
                        print('Capacity should be more than 0')
                        return
                
                runQuery3Arg(sqlv.templateinsertTheater, tmp.name, tmp.location, str(tmp.capacity))
                #check whether insertion is operated or not
                print('A building is successfully inserted')

        elif queUser=='5':
                wantDelete=int(input("Building ID: "))
                idExist=False

                tmp5=runQuery(sqlv.printTheater)
                for theaterRecord in tmp5:
                        id=theaterRecord[0]
                        if id is wantDelete:
                                idExist=True
                                break
                if idExist is True:
                        tmp5=runQuery1Arg(sqlv.deleteTheater, str(wantDelete))
                        print("A building is 7successfully removed")
                        
                else:
                        print("Building {0} doesn't exist".format(str(wantDelete)))
                #Need cascading deletion implementation

                
        elif queUser=='6':
                playName=''
                playGenre=''
                playPrice=0
                
                print('Performance name:', end=' ')
                playName=truncateString(input())
                print('Performance type:', end=' ')
                playGenre=truncateString(input())
                print('Performance price:', end=' ')
                playPrice=int(input())
                
                if(playPrice < 0):
                        print('Price should be 0 or more')
                        return
                
                runQuery3Arg(sqlv.templateinsertPlay, playName, playGenre, str(playPrice))
                
                #check whether insertion is operated or not
                print('A performance is successfully inserted')

        elif queUser=='7':
                wantDelete=int(input("Performance ID: "))
                idExist=False

                tmp7=runQuery(sqlv.printPlay)
                for playRecord in tmp7:
                        id=playRecord[0]
                        if id is wantDelete:
                                idExist=True
                                break
                if idExist is True:
                        tmp7=runQuery1Arg(sqlv.deletePlay, str(wantDelete))
                        print("A performance is successfully removed")
                        
                else:
                        print("Performance {0} doesn't exist".format(str(wantDelete)))
                #Need cascading deletion implementation


        elif queUser=='8':
                audienceName=''
                audienceSex=''
                audienceAge=0
                
                print('Audience name:', end=' ')
                audienceName=truncateString(input())

                print('Audience gender:', end=' ')
                audienceSex=truncateString(input())
                
                if(audienceSex is not 'M' and audienceSex is not 'F'):
                        print("Gender should be 'M' or 'F'")
                        return
                
                
                print('Audience age:', end=' ')
                audienceAge=int(input())
                
                if(audienceAge < 1):
                        print('Age should be more than 0')
                        return
                
                runQuery3Arg(sqlv.templateinsertAudience, audienceName, audienceSex, str(audienceAge))
                
                #check whether insertion is operated or not
                print('An audience is successfully inserted')

        elif queUser=='9':
                wantDelete=int(input("Audience ID: "))
                idExist=False

                tmp9=runQuery(sqlv.printAudience)
                for audienceRecord in tmp9:
                        id=audienceRecord[0]
                        if id is wantDelete:
                                idExist=True
                                break
                if idExist is True:
                        tmp9=runQuery1Arg(sqlv.deleteAudience, str(wantDelete))
                        print("An audience is successfully removed")
                        
                else:
                        print("Audience {0} doesn't exist".format(str(wantDelete)))
                #Need cascading deletion implementation

        elif queUser=='10':
                bdId=int(input("Building ID: "))
                PfId=int(input("Performance ID: "))
                rst10=runQuery1Arg(sqlv.selectTheaterInPlay, str(PfId))
                if rst10[0][0] is None:
                        rst10=runQuery2Arg(sqlv.updateTheaterInPlay, str(bdId), str(PfId) )
                        print("Successfully assign a performance")
                else:
                        print("Performance {0} is already assigned".format(PfId))

        elif queUser=='11':
                PfId=int(input("Performance ID: "))
                AdId=int(input("Audience ID: "))
                RawSeatNumList=truncateString(input("Seat number: "))
                tmp11_1=runQuery1Arg(sqlv.selectInPlay, str(PfId))
                # print(tmp11_1)
                BdId=tmp11_1[0][4]
                capacity=0
                if BdId is not None:
                        tmp11_1_1=runQuery1Arg(sqlv.selectCapacityInTheater, str(BdId))
                        capacity=tmp11_1_1[0][0]
                else:
                        print("Performance {0} isn't assigned".format(PfId))
                        return



                RawSeatNumList = RawSeatNumList.replace(' ','').split(',')
                SeatNumList=list()
                try:
                        for seatNum in RawSeatNumList:
                                #check if the number is not out of range
                                if int(seatNum) > capacity or int(seatNum) < 1:
                                        print('Seat number out of range')
                                        return
                                #check if the number is not in booking table
                                tmp11_2=runQuery2Arg(sqlv.checkDuplicationInBooking, str(PfId), str(seatNum))
                                if tmp11_2 is not ():
                                        print('The seat is already taken')
                                        return
                                
                                tmp11_2 = runQuery3Arg(sqlv.templateinsertBooking, str(PfId), str(seatNum), str(AdId))
                                SeatNumList.append(int(seatNum))
                                #print(tmp11_2)

                #Catch unacceptable input
                except ValueError:
                        print("Error: Input seat number as number type")
                        return
                
                #Calculate total price of the reservation
                price = tmp11_1[0][3]
                tmp11_3 = runQuery1Arg(sqlv.selectAgeInAudience, str(AdId))
                age = tmp11_3[0][0]
                dc = discountRate(age)
                
                # rounding up from ONLY first fractional number(truncate below fractional numbers).
                print("Successfully book a performance")
                rst11=math.ceil( int( price*len(SeatNumList) * dc * 10)/10.0    )
                rst11=addCommas(rst11)
                print( "Total ticket price is {0}".format(rst11))
                
        elif queUser=='12':
                bdId=int(input("Building ID: "))
                idExist=False
                tmp12=runQuery(sqlv.printTheater)
                for theaterRecord in tmp12:
                        id=theaterRecord[0]
                        if id is bdId:
                                idExist=True
                                break
                if idExist is True:
                        rst12=runQuery1Arg(sqlv.selectInPlayUsingTheater, str(bdId))
                        #print(rst12)
                        print("--------------------------------------------------------------------------------")
                        lineIndex = 'id'.ljust(5) + 'name'.ljust(30) + 'type'.ljust(20) + 'price'.ljust(10) + 'booked'.ljust(10)
                        print(lineIndex)
                        print("--------------------------------------------------------------------------------")        
                        for playRecord in rst12:
                                word=playRecord
                                tmp12_1=runQuery1Arg(sqlv.selectAudienceIdInBookingUsingPlayId,str(word[0]))
                                lineNew = str(word[0]).ljust(5) + word[1].ljust(30) + word[2].ljust(20) + str(word[3]).ljust(10) + str(len(tmp12_1)).ljust(10)

                                # lineNew = str(word[0]).ljust(5) + word[1].ljust(30) + word[2].ljust(20) + str(word[3]).ljust(10) + 'NULL'.ljust(10)
                                print(lineNew)
                        print("--------------------------------------------------------------------------------")

                else:
                        print("Building {0} doesn't exist".format(str(bdId)))

        elif queUser=='13':
                PfId=int(input("Performance ID: "))

                tmp13=runQuery1Arg(sqlv.selectAudienceIdInBookingUsingPlayId, PfId)

                #Print the result of the search
                tmp13=sortTuple(tmp13)
                #print(tmp13)
                        
                print("--------------------------------------------------------------------------------")
                lineIndex = 'id'.ljust(5) + 'name'.ljust(30) + 'gender'.ljust(20) + 'age'.ljust(10)
                print(lineIndex)
                print("--------------------------------------------------------------------------------")        
                for bookingRecord in tmp13:
                        tmp13_1=runQuery1Arg(sqlv.selectInAudience, str(bookingRecord[0]))
                        for audienceRecord in tmp13_1:
                                word=audienceRecord
                                lineNew = str(word[0]).ljust(5) + word[1].ljust(30) + word[2].ljust(20) + str(word[3]).ljust(10)
                                print(lineNew)                        
                print("--------------------------------------------------------------------------------")
                

        elif queUser=='14':
                PfId=int(input("Performance ID: "))
                
                tmp14=runQuery1Arg(sqlv.selectInPlay, PfId)
                
                #Check if PfId exists in play table.
                if tmp14 is ():
                        print("Performance {0} doesn't exist".format(PfId))
                        return

                #Check if the performance have assigned.
                if tmp14[0][4] is None:
                        print("Performance {0} isn't assigned".format(PfId))
                        return

                #Get capacity of the building
                BdId = tmp14[0][4]
                tmp14_1 = runQuery1Arg(sqlv.selectCapacityInTheater, str( BdId))
                print(tmp14_1)
                capa = tmp14_1[0][0]
                print(capa)
                #Print the result of the search
                tmp14=runQuery1Arg(sqlv.selectInBookingUsingPlayId, PfId)
                tmp14 = sortTuple(tmp14)
                print("--------------------------------------------------------------------------------")
                lineIndex = 'seat_number'.ljust(20) + 'audience_id'.ljust(20)
                print(lineIndex)
                print("--------------------------------------------------------------------------------")        
                for bookingRecord in tmp14:
                        word=bookingRecord
                        lineNew = str(word[0]).ljust(20) + str(word[1]).ljust(20)
                        print(lineNew)                        
                print("--------------------------------------------------------------------------------")
                

        elif queUser=='15':
                cntn.close()
                print('Bye!')
                sys.exit()

        elif queUser=='16':
                ansReset = input("Do you want to reset whole data? input 'y' or 'n': ")

                if(ansReset is 'y'):
                        resetDB()
                else:
                        return
        else:
                print('Invalid action')
                return

        cntn.commit()
        return

# Make connection btw mysql and python
cntn = pymysql.connect(host='s.snu.ac.kr', port=3306, user='DB2011_12141', password='DB2011_12141', charset='utf8', db='DB2011_12141')
# get cursor from connection.
cursor = cntn.cursor()
#Create tables if they do not exist
checkDB()

# input SQL 
#sql = crtTheater

# execution
#cursor.execute(sql)
#result=cursor.fetchall()
#print(result)

printQuery()
while(True):
        queUser=input()
        doCommand(queUser)
        print('\nSelect your action: ', end='')

cntn.close()

# commit
#cntn.commit()

#template
'''#CREATE TABLE hello (
                   id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
            );
'''
