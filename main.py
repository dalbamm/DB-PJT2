import pymysql, sys
import sqlStatementVundle as sqlv
import dataType as d

#run query statement input as argument
def runQuery(statement):
        cursor.execute(statement)
        result=cursor.fetchall()
        print('result: {0}'.format(result))

def runQuery(statement, str1, str2, str3):
        cursor.execute(statement, (str1, str2, str3))
        result=cursor.fetchall()
        print('result: {0}'.format(result))

def truncateString(rawString):
        return rawString[:200]
def checkDB():
        cursor.execute('''show tables;''')
        dbTuples = cursor.fetchall()
        print('result: {0}'.format(dbTuples))
        
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
        print('result: {0}'.format(dbTuples))
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
                1
        elif queUser=='2':
                2
        elif queUser=='3':
                3
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
                
                runQuery(sqlv.templateinsertTheater, tmp.name, tmp.location, str(tmp.capacity))
                #check whether insertion is operated or not
                print('A building is successfully inserted')

        elif queUser=='5':
                5
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
                
                runQuery(sqlv.templateinsertPlay, playName, playGenre, str(playPrice))
                
                #check whether insertion is operated or not
                print('A performance is successfully inserted')

        elif queUser=='7':
                7
        elif queUser=='8':
                audienceName=''
                audienceSex=''
                audienceAge=0
                
                print('Audience name:', end=' ')
                playName=truncateString(input())
                print('Audience type:', end=' ')
                playGenre=truncateString(input())
                print('Audience age:', end=' ')
                playPrice=int(input())
                
                if(playPrice < 0):
                        print('Price should be 0 or more')
                        return
                
                runQuery(sqlv.templateinsertPlay, playName, playGenre, str(playPrice))
                
                #check whether insertion is operated or not
                print('An audience is successfully inserted')
                
        elif queUser=='9':
                9
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
                resetDB()
        else:
                print('Invalid action')
        
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
