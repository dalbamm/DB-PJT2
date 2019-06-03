import pymysql

def printQuery():
       que = '============================================================\n1. print all buildings\n2. print all performances\n3. print all audiences\n4. insert a new building\n5. remove a building\n6. insert a new performance\n7. remove a performance\n8. insert a new audience\n9. remove an audience\n10. assign a performance to a building\n11. book a performance\n12. print all performances which assigned at a building\n13. print all audiences who booked for a performance\n14. print ticket booking status of a performance\n15. exit\n16. reset database\n============================================================\nSelect your action:'
       print(que,end='')

#printQuery()
#queUser=input()
#print(queUser)
samvar='samvar'
for i in (('a',),('b',),('abcd',)):
       if 'a' in i:
              print('a is here')

class building:
       ba='a'
       bb='b'
       bc='c'
       def re(self, a, b, c):
              self.ba=a
              self.bb=b
              self.bc=c

# a = building()
# print(a.ba)
# a.re(1,2,3)
# print(a.ba)
a = 1
print("test {0}".format(a))
