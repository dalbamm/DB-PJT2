#print theater table
printTheater = '''SELECT * FROM theater;'''

#print play table
printPlay = '''SELECT * FROM play;'''

#print audience table
printAudience = '''SELECT * FROM audience;'''

#Create table theater
crtTheater = '''CREATE TABLE theater (
                id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name varchar(200) COLLATE utf8_bin NOT NULL,
                location varchar(200) COLLATE utf8_bin NOT NULL,
                capacity INT UNSIGNED NOT NULL
        );
'''
#Create table play
crtPlay = '''CREATE TABLE play (
                id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name varchar(200) COLLATE utf8_bin NOT NULL,
                genre varchar(200) COLLATE utf8_bin NOT NULL,
                price INT UNSIGNED NOT NULL,
                theater INT UNSIGNED
        );
'''
#Create table audience
crtAudience = '''CREATE TABLE audience (
                id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name varchar(255) COLLATE utf8_bin NOT NULL,
                sex varchar(1) COLLATE utf8_bin NOT NULL,
                age INT UNSIGNED NOT NULL
        );
'''
#Create table booking
crtBooking = '''CREATE TABLE booking (
                id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                playId INT UNSIGNED NOT NULL,
                seatNum INT UNSIGNED NOT NULL,
                audienceId INT UNSIGNED NOT NULL                
        );
'''
#delete theater table
deleteTheater = '''DELETE FROM theater where id=%s;'''

#delete play table
deletePlay = '''DELETE FROM play where id=%s;'''

#delete audience table
deleteAudience = '''DELETE FROM audience where id=%s;'''

#delete in booking table
deleteBookingUsingPlayId = '''DELETE FROM booking where playId=%s;'''

#delete in booking table
deleteBookingUsingAudienceId = '''DELETE FROM booking where audienceId=%s;'''



#drop table theater
dropTheater = '''DROP TABLE theater;'''

#drop table play
dropPlay = '''DROP TABLE play;'''

#drop table audience
dropAudience = '''DROP TABLE audience;'''

#drop table audience
dropBooking = '''DROP TABLE booking;'''
                                           
#Insert row in table
def insertTheater(name, location, capacity):
  return templateinsertTheater

#template
templateinsertTheater = '''INSERT INTO 
                theater(name, location, capacity)
                VALUES
                (%s,%s,%s);'''

#template
templateinsertPlay = '''INSERT INTO 
                play(name, genre, price)
                VALUES
                (%s,%s,%s);'''
                #template

templateinsertAudience = '''INSERT INTO 
                audience(name, sex, age)
                VALUES
                (%s,%s,%s);'''

templateinsertBooking = '''INSERT INTO 
                booking(playId, seatNum, audienceId)
                VALUES
                (%s,%s,%s);'''


#print an element table template
selectTheaterInPlay = '''SELECT theater FROM play where id=%s;'''

updateTheaterInPlay = '''UPDATE play SET theater=%s where id=%s;'''

countTheaterInPlay = '''SELECT count(theater) FROM play where theater=%s;'''

selectInPlayUsingTheater = '''SELECT * FROM play where theater=%s;'''

selectCapacityInTheater = '''SELECT capacity FROM theater where id=%s;'''

selectInPlay = '''SELECT * FROM play where id=%s;'''

checkDuplicationInBooking = '''SELECT * FROM booking where playId=%s AND seatNum=%s;'''

selectAgeInAudience = '''SELECT age FROM audience where id=%s;'''

selectInBookingUsingPlayId = '''SELECT seatNum, audienceId FROM booking where playId=%s;'''

selectAudienceIdInBookingUsingPlayId = '''SELECT distinct(audienceId) FROM booking where playId=%s;'''

selectInAudience = '''SELECT * FROM audience where id=%s ORDER BY id, name, sex, age desc;'''

selectIdInPlayUsingTheater = '''SELECT id FROM play where theater=%s;'''

