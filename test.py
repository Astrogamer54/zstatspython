from zstatspython import zstatspy
import time
login=False
user=False
while login==False:
    try:
        print("MySQL Login: ")
        host=input("Host: ")
        username=input("Username: ")
        password=input("Password: ")
        database=input("Database: ")
        db=zstatspy.connect(host,username,password, database)
        login=True
    except:
        print("Failed To Login")
print("Login Succeded")
print("Get Stats")
while user==False:
    try:
        
        username=input("MC Username: ")
        userstats=zstatspy.getStats(username,db)
        user=True
    except:
        print("Failed To Get Player/ No Player Found?")
        
for x in userstats:
    print(x)
time.sleep(10)



