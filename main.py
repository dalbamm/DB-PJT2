import pymysql, sys
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

def runQuery3Arg(statement, str1, str2, str3):
        cursor.execute(statement, (str1, str2, str3))
        result=cursor.fetchall()
        #print('result: {0}'.format(result))
        return result

def truncateString(rawString):
        return rawString[:200]
def checkDB():
        cursor.execute('''show tables;''')
        dbTuples = cursor.fetchall()
        #print('result: {0}'.format(dbTuples))
        
        theaterExist=False
        playExist=False
        audienceExist=False
        
        for dbName in dbTuples:                
                if 'theater' in dbName:
                        theaterExist = True
                elif 'play' in dbName:
                        playExist = True
                elif 'audience' in dbName:
                        audienceExist = True
        if theaterExist is False:
                runQuery(sqlv.crtTheater)
        if theaterExist is False:
                runQuery(sqlv.crtPlay)
        if theaterExist is False:
                runQuery(sqlv.crtAudience)
        
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
        
        #create theater table
        runQuery(sqlv.crtTheater)
        
        #create play table
        runQuery(sqlv.crtPlay)
        
        #create audience table
        runQuery(sqlv.crtAudience)
        
def printQuery():
       que = '============================================================\n1. print all buildings\n2. print all performances\n3. print all audiences\n4. insert a new building\n5. remove a building\n6. insert a new performance\n7. remove a performance\n8. insert a new audience\n9. remove an audience\n10. assign a performance to a building\n11. book a performance\n12. print all performances which assigned at a building\n13. print all audiences who booked for a performance\n14. print ticket booking status of a performance\n15. exit\n16. reset database\n============================================================\nSelect your action:'
       print(que, end=' ')

def doCommand(queUser):
        if queUser=='1':
                tmp1=runQuery(sqlv.printTheater)
#                print(tmp1)
                print("--------------------------------------------------------------------------------")
                lineIndex = 'id'.ljust(5) + 'name'.ljust(20) + 'location'.ljust(30) + 'capacity'.ljust(10) + 'assigned'.ljust(10)
                print(lineIndex)
                print("--------------------------------------------------------------------------------")        
                for theaterRecord in tmp1:
                        word=theaterRecord
                        lineNew = str(word[0]).ljust(5) + word[1].ljust(20) + word[2].ljust(30) + str(word[3]).ljust(10) + 'NULL'.ljust(10)
                        print(lineNew)
                        
                print("--------------------------------------------------------------------------------")

                # Need additional manipulation for loading the number of assigned play

        elif queUser=='2':
                tmp2=runQuery(sqlv.printPlay)
#                print(tmp2)
                print("--------------------------------------------------------------------------------")
                lineIndex = 'id'.ljust(5) + 'name'.ljust(30) + 'type'.ljust(20) + 'price'.ljust(10) + 'booked'.ljust(10)
                print(lineIndex)
                print("--------------------------------------------------------------------------------")        
                for playRecord in tmp2:
                        word=playRecord
                        lineNew = str(word[0]).ljust(5) + word[1].ljust(30) + word[2].ljust(20) + str(word[3]).ljust(10) + 'NULL'.ljust(10)
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
                wantDelete=input("Building ID: ")
                idExist=False

                tmp5=runQuery(sqlv.printTheater)
                for theaterRecord in tmp5:
                        id=theaterRecord[0]
                        if id is int(wantDelete):
                                idExist=True
                                break
                if idExist is True:
                        tmp5=runQuery1Arg(sqlv.deleteTheater, wantDelete)
                        print("A building is 7successfully removed")
                        
                else:
                        print("Building {0} doesn't exist".format(wantDelete))
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
                wantDelete=input("Performance ID: ")
                idExist=False

                tmp7=runQuery(sqlv.printPlay)
                for playRecord in tmp7:
                        id=playRecord[0]
                        if id is int(wantDelete):
                                idExist=True
                                break
                if idExist is True:
                        tmp7=runQuery1Arg(sqlv.deletePlay, wantDelete)
                        print("A performance is successfully removed")
                        
                else:
                        print("Performance {0} doesn't exist".format(wantDelete))
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
                wantDelete=input("Audience ID: ")
                idExist=False

                tmp9=runQuery(sqlv.printAudience)
                for audienceRecord in tmp9:
                        id=audienceRecord[0]
                        if id is int(wantDelete):
                                idExist=True
                                break
                if idExist is True:
                        tmp9=runQuery1Arg(sqlv.deleteAudience, wantDelete)
                        print("An audience is successfully removed")
                        
                else:
                        print("Audience {0} doesn't exist".format(wantDelete))
                #Need cascading deletion implementation

        elif queUser=='10':
                10
        elif queUser=='11':
                11
        elif queUser=='12':
                12
        elif queUser=='13':
                13
        elif queUser=='14':
                14
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
