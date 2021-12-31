#COMPLETE VERSION OF OUR PROJECT

import datetime
import pyttsx3
import mysql.connector as mys
mycon=mys.connect(host="localhost",user="root",password="password",database="employeedbms")
mycursor=mycon.cursor()
print("""
""")

ans = True
while ans == True:
    
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',170)

    engine.say('WELCOME TO THE EMPLOYEE DATABASE MANAGEMENT SYSTEM')
    print("************** WELCOME TO EMPLOYEE DATABASE MANAGEMENT SYSTEM *****************")
    engine.runAndWait()
    engine.say('THE DATABASE CONSISTS THE CREDENTIALS OF ALL THE EMPLOYEES IN THE COMPANY')
    engine.runAndWait()
    engine.say('MAIN MENU')
    print("************  MAIN MENU ************".center(80))

    print("A) TO ACCESS ALL RECORDS OF EMPLOYEE".center(80))

    print("B) TO INSERT A NEW EMPLOYEE RECORD".center(80))

    print("C) TO VIEW PARTICULAR EMPLOYEE RECORD".center(80))

    print("D) TO UPDATE PARTICULAR EMPLOYEE RECORD".center(80))

    print("E) TO DELETE A EMPLOYEE RECORD".center(80))

    print("F) TO SORT A EMPLOYEE RECORD BY DESIGNATION".center(80))
    
    print("G) EXIT".center(80))
    
    print(""" ***************************************************************************** """)
    engine.runAndWait()

    engine.say('ENTER YOUR CHOICE')
    engine.runAndWait()

    userchoice=input("ENTER YOUR CHOICE: ").upper()
    print(""" **************************************************************************************************** """)
    


    if userchoice == 'A':
        engine.say('EMPLOYEE DETAILS')
        print("******************************** EMPLOYEE DETAILS*****************************************")
        engine.runAndWait()
        
        mycursor.execute("select * from empd")
        mydata = mycursor.fetchall()
        for row in mydata:
            print(row[0], ':', row[1], ':', row[2], ':', row[3], ':', row[4], ':', row[5], ':', row[6], ':', row[7], ':',
                  row[8], ':', row[9], ':', row[10], ':', row[11], ':', row[12])

        


    elif userchoice == 'B':
     try:   
        engine.say('WELCOME TO EMPLOYEE DATA ENTRY SCREEN')
        print("*********************** WELCOME TO EMPLOYEE DATA ENTRY SCREEN**********************")
        engine.runAndWait()
        EMPID=input("ENTER EMPLOYEE ID: ")
        NAME=input("ENTER EMPLOYEE NAME: ")
        GENDER= input("ENTER EMPLOYEE GENDER: ")
        AGE=int(input("ENTER EMPLOYEE AGE: "))
        DOB = input("ENTER YOUR DATE OF BIRTH(DD/MM/YY): ")
        day, month, year = list(map(int, DOB.split("/")))
        DOB = datetime.date(year, month, day)
        ADDRESS=input("ENTER EMPLOYEE ADDRESS: ")
        NATIONALITY=input("ENTER NATIONALITY: ")
        QUALIFICATION=input("ENTER EMPLOYEE QUALIFICATION DETAILS: ")
        WORKEXPERIENCE=input("ENTER EMPLOYEE PAST WORK EXPERIENCE: ")
        DESIGNATION=input("ENTER EMPLOYEE DESIGNATION IN COMPANY: ")
        ANNUALINCOME=input("ENTER EMPLOYEE ANNUAL INCOME: ")
        EMAILID=input("ENTER EMPLOYEE EMAIL-ID: ")
        MOBILENO=int(input("ENTER EMPLOYEE MOBILE NO:"))
        query="insert into empd values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')".format(EMPID,NAME,GENDER,AGE,DOB,ADDRESS,NATIONALITY,QUALIFICATION,WORKEXPERIENCE,DESIGNATION,ANNUALINCOME,EMAILID,MOBILENO)
        mycursor.execute(query)
        mycon.commit()
        print("********YOUR EMPLOYEE RECORD HAS BEEN SUCCESSFULLY SAVED********")
     except:
        engine.say("AN ERROR OCCURED IN ASSIGINING THE RESPECTIVE VALUE,TRY AGAIN ")
        print("********* AN ERROR OCCURED IN ASSIGING THE RESPECTIVE VALUES , TRY AGAIN *********")
        engine.runAndWait()

    elif userchoice == "C":
        engine.say('WELCOME TO EMPLOYEE DATABASE SCREEN')
        print("************ WELCOME TO EMPLOYEE DATABASE SCREEN ************")
        engine.runAndWait()

        EMPID=input("ENTER EMPLOYEE ID: ").upper()
        query = "SELECT * FROM EMPD WHERE EMPID='{}'".format(EMPID)
        mycursor.execute(query)
        data=mycursor.fetchone()
        if data!=None:
            engine.say("Record found")
            print("*************** RECORD FOUND ***************")
            engine.runAndWait()
            print(data)
            
        else:
            engine.say("sorry no such employee record found")
            print("*******************SORRY NO SUCH EMPLOYEE RECORD FOUND ! ! ! ! *************")
            engine.runAndWait()
            
    elif userchoice == "D":
        engine.say('TO UPDATE A PARTICULAR RECORD')
        print("********** TO UPDATE A PARTICULAR RECORD **********")
        engine.runAndWait()
        EMPID = input("ENTER EMPLOYEE ID: ").upper()
        query = "SELECT * FROM EMPD WHERE EMPID='{}'".format(EMPID)
        mycursor.execute(query)
        data = mycursor.fetchone()
        if data != None:
            print("*************** RECORD FOUND *************")
            print(data)
            print("****************************************************")
            print("""WHICH OF THE FOLLOWING YOU WANT TO UPDATE:
        A) NAME
        B) GENDER
        C) AGE
        D) DOB
        E) ADDRESS
        F) NATIONALITY
        G) QUALIFICATION
        H) WORK EXPERIENCE
        I) DESIGNATION
        J) ANNUAL INCOME
        K) EMAIL ID
        L) MOBILE NUMBER
            """.center(80))
        else:
            print("SORRY NO SUCH EMPLOYEE RECORD FOUND!!!!")
            print("*******************************************************")




        choice = input("ENTER YOUR CHOICE: ").upper()
        engine.say("enter your choice")
        engine.runAndWait()
            
        if choice == 'A':
            NAME = input("ENTER NEW NAME: ")
            query ="UPDATE EMPD SET NAME='{}' WHERE EMPID='{}'".format(NAME,EMPID)
            mycursor.execute(query)
            mycon.commit()
            print("*********************EMPLOYEE RECORD UPDATED********")
            engine.say("employee record updated successfully")
            engine.runAndWait()
            
        elif choice == 'B':
            GENDER = input("ENTER GENDER: ")
            query = "UPDATE EMPD SET GENDER='{}' WHERE EMPID='{}'".format(GENDER,EMPID)
            mycursor.execute(query)
            mycon.commit()
            print("**************EMPLOYEE RECORD UPDATED***************")
            engine.say("employee record updated successfully")
            engine.runAndWait()
            
        elif choice == 'C':
            AGE = input("ENTER AGE: ")
            query = "UPDATE EMPD SET AGE='{}' WHERE EMPID='{}'".format(AGE, EMPID)
            mycursor.execute(query)
            mycon.commit()
            print("***************EMPLOYEE RECORD UPDATED***************")
            engine.say("employee record updated successfully")
            engine.runAndWait()
            
        elif choice == 'D':
            DOB = input("ENTER YOUR DATE OF BIRTH(DD/MM/YY): ")
            day, month, year = list(map(int, DOB.split("/")))
            DOB = datetime.date(year, month, day)
            query = "UPDATE EMPD SET DOB='{}' WHERE EMPID='{}'".format(DOB, EMPID)
            mycursor.execute(query)
            mycon.commit()
            print("********************EMPLOYEE RECORD UPDATED************")
            engine.say("employee record updated successfully")
            engine.runAndWait()
            
        elif choice == 'E':
            ADDRESS = input("ENTER NEW ADDRESS: ")
            query = "UPDATE EMPD SET ADDRESS='{}' WHERE EMPID='{}'".format(ADDRESS, EMPID)
            mycursor.execute(query)
            mycon.commit()
            print("*****************EMPLOYEE RECORD UPDATED***************")
            engine.say("employee record updated successfully")
            engine.runAndWait()
            
        elif choice == 'F':
            NATIONALITY = input("ENTER NATIONALITY: ")
            query = "UPDATE EMPD SET NATIONALITY='{}' WHERE EMPID='{}'".format(NATIONALITY, EMPID)
            mycursor.execute(query)
            mycon.commit()
            print("***************EMPLOYEE RECORD UPDATED**********")
            engine.say("employee record updated successfully")
            engine.runAndWait()
            
        elif choice == 'G':
            QUALIFICATION = input("ENTER NEW QUALIFICATION DETAILS:")
            query = "UPDATE EMPD SET QUALIFICATION='{}' WHERE EMPID='{}'".format(QUALIFICATION, EMPID)
            mycursor.execute(query)
            mycon.commit()
            print("*****************EMPLOYEE RECORD UPDATED****************")
            engine.say("employee record updated successfully")
            engine.runAndWait()
            
        elif choice == 'H':
            WORKEXPERIENCE = input("ENTER WORK EXPERIENCE: ")
            query = "UPDATE EMPD SET WORKEXPERIENCE='{}' WHERE EMPID='{}'".format(WORKEXPERIENCE, EMPID)
            mycursor.execute(query)
            mycon.commit()
            print("*********************EMPLOYEE RECORD UPDATED****************")
            engine.say("employee record updated successfully")
            engine.runAndWait()
            
        elif choice == 'I':
            DESIGNATION = input("ENTER NEW DESIGNATION: ")
            query = "UPDATE EMPD SET DESIGNATION='{}' WHERE EMPID='{}'".format(DESIGNATION, EMPID)
            mycursor.execute(query)
            mycon.commit()
            print("********************EMPLOYEE RECORD UPDATED*****************")
            engine.say("employee record updated successfully")
            engine.runAndWait()

            
        elif choice == 'J':
            ANNUALINCOME = int(input("ENTER UPDATED ANNUAL INCOME: "))
            query = "UPDATE EMPD SET ANNUALINCOME='{}' WHERE EMPID='{}'".format(ANNUALINCOME, EMPID)
            mycursor.execute(query)
            mycon.commit()
            print("*****************EMPLOYEE RECORD UPDATED*****************")
            engine.say("employee record updated successfully")
            engine.runAndWait()
            
        elif choice == 'K':
            EMAILID = input("ENTER EMPLOYEE EMAIL-ID: ")
            query = "UPDATE EMPD SET EMAILID='{}' WHERE EMPID='{}'".format(EMAILID, EMPID)
            mycursor.execute(query)
            mycon.commit()
            print("*****************EMPLOYEE RECORD UPDATED*****************")
            engine.say("employee record updated successfully")
            engine.runAndWait()
            
        elif choice == 'L':
            MOBILENO = int(input("ENTER NEW MOBILE NUMBER: "))
            query = "UPDATE EMPD SET MOBILENO='{}' WHERE EMPID='{}'".format(MOBILENO, EMPID)
            mycursor.execute(query)
            mycon.commit()
            print("*********************EMPLOYEE RECORD UPDATED****************")
            engine.say("employee record updated successfully")
            engine.runAndWait()

    elif userchoice == 'E':
        engine.say(' TO DELETE THE RECORD')
        print("**********TO DELETE THE RECORD**********")
        engine.runAndWait()
        
        EMPID=input("ENTER EMPLOYEE ID: ").upper()
        query = "DELETE FROM EMPD WHERE EMPID= '{}' ".format(EMPID)
        mycursor.execute(query)
        mycon.commit()
        if query not in EMPID:
            engine.say("your employee record has been succesfully deleted")
            print(mycursor.rowcount,"Record Deleted")
            print("********YOUR EMPLOYEE RECORD HAS BEEN SUCCESSFULLY DELETED**********" )
            engine.runAndWait()
        else:
            engine.say("sorry no such employee records found")
            print("*****************SORRY NO SUCH EMPLOYEE RECORD FOUND!!!!**************")
            engine.runAndWait()

            
    elif userchoice == 'F':
        engine.say(' SORTING RECORDS BY DESIGNATION')
        print("********** SORTING RECORDS BY DESIGNATION**********")
        engine.runAndWait()
        
        DESIGNATION=input("ENTER DESIGNATION : ").upper()
        query = "SELECT EMPID,NAME,GENDER,AGE,DOB,ADDRESS,NATIONALITY,QUALIFICATION,WORKEXPERIENCE,DESIGNATION,ANNUALINCOME,EMAILID,MOBILENO FROM EMPD WHERE DESIGNATION = '{}' ".format(DESIGNATION)
        mycursor.execute(query)
        
        mycon.commit()
        if query not in DESIGNATION:
            print(mycursor.fetchall())
            print(mycursor.rowcount,"RECORD SORTED")
            engine.say("successfully sorted")
            print("******** SUCCESSFULLY SORTED **********" )
            engine.runAndWait()               
        

    elif userchoice == "G":
        ans = False
        engine.say('THANKS FOR USING OUR PROGRAM')
        print("****************************** THANKS FOR USING OUR POROGRAM ***************************")
        engine.runAndWait()

    else:
        engine.say("No Such Option Exists,Enter Valid Choice")
        engine.runAndWait()
        print("************ NO SUCH OPTION EXISTS.ENTER VALID CHOICE************".center(80))
    

        


