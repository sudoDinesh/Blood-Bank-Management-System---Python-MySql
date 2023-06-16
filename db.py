import mysql.connector as mc
import random

class Database:
    def __init__(self, db,user,password):
        self.con = mc.connect(host='localhost',user = user,password = password,database = db)
        self.cur = self.con.cursor()
    # Insert Function
    def insert(self,donorID,name,bType,dob,age,gender,address,contact,date,companion,relation):

        self.cur.execute("insert into donors values(%s,%s)",(donorID,date))
        
        self.cur.execute("insert into donor_info values (%s,%s,%s,%s,%s,%s,%s,%s)",
                         (donorID,name,bType,contact,dob,age,gender,address))

        self.cur.execute("insert into companion values(%s,%s,%s)",(donorID,companion,relation))
        
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT d.donor_id,di.name,di.blood_type,di.phone_no,di.dob,di.age,di.sex,di.address,\
                            d.date_of_donation,c.companion_name,c.relationship\
                            from companion c inner join donor_info di on c.donor_id = di.donor_id inner join donors d on di.donor_id=d.donor_id")
        rows = self.cur.fetchall()
        # print(rows)
        return rows
    # Delete a Record in DB
    def remove(self, did):
        self.cur.execute(f"delete from companion where donor_id='{did}'")        
        self.cur.execute(f"delete from donor_info where donor_id='{did}'")
        self.cur.execute(f"delete from donors where donor_id='{did}'")

        self.con.commit()

    # Update a Record in DB
    def update(self,donorID,name,bType,dob,age,gender,address,contact,date,companion,relation):
        self.cur.execute(f"update donor_info set name='{name}', blood_type='{bType}', phone_no='{contact}',dOB='{dob}',age='{age}',sex='{gender}',address='{address}' where donor_id='{donorID}'")

        self.cur.execute(f"update companion set companion_name='{companion}',relationship='{relation}' where donor_id='{donorID}'")

        self.cur.execute(f"update donors set date_of_donation='{date}'  where donor_id='{donorID}'")

        self.con.commit()

        
    def fetch1(self):
        self.cur.execute("SELECT emp_id, name, dob, gender, phone_no, salary, address from staff")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    def insert1(self,Eid,Ename,contact1,dob1,gender1,sal,address1):
        self.cur.execute("insert into staff values(%s,%s,%s,%s,%s,%s,%s)",(Eid,Ename,gender1,address1,contact1,sal,dob1)) 
        self.con.commit()

    def update1(self,Eid,Ename,contact1,dob1,gender1,sal,address1):
        self.cur.execute(f"update staff set name='{Ename}', dob='{dob1}', gender='{gender1}', phone_no='{contact1}', salary='{sal}', address='{address1}' where emp_id='{Eid}'")
        self.con.commit()

    def remove1(self, Eid):
        self.cur.execute(f"delete from staff where emp_id='{Eid}'")        
        self.con.commit()
        
'''

donorID,name,bType,dob,age,gender,address,contact,date,companion,relation



'''
