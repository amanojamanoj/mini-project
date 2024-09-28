import mysql.connector

mydb = mysql.connector.connect (
  host="localhost",
  user="root",
  password="root@123"

)  
mycursor =mydb.cursor()
class Consultation:
    def _init_(self,consultation_id,name,email,phone,consultation_date,consultation_time):
        self.consultation_id=consultation_id
        self.name=name
        self.email=email
        self.phone=phone
        self.consultation_date=consultation_date
        self.consultation_time=consultation_time
class Scheduling:
    def _init_(self,consultation_id,consultation_date,consultation_time,consultation_Venue):
        self.consultation_id=consultation_id
        self.consultation_date=consultation_date
        self.consultation_time=consultation_time
        self.consultation_Venue=consultation_Venue
class Feedback:
  def _init_(self,feedback_id,feedback_rating,feedback_comments):
        self.feedback_id=feedback_id
        self.feedback_rating=feedback_rating
        self.feedback_comments=feedback_comments
class ConsultationDetails:
  def createdb():
      try:
          mycursor.execute("CREATE DATABASE MYDB")
      except Exception:
          print("Already Created DB")
  def useDB():
      try:
          mycursor.execute("use MYDB")
      except Exception:
          print("Already used  DB")
  def create_consultation():
       try:                                
          mycursor.execute("CREATE TABLE mytable(consultation_id int(15),name varchar(29), email varchar(25),phone int(10),consultation_date( int(10),consultation_time int (10)))")
       except Exception:
          print("Already created table")
  def insert_consultation():
      try:
          mycursor.execute("INSERT INTO mytable  values(24211,'naveen','xyz@gmail.com',123456789,27-9-2024,10.00.Am)")  
          mydb.commit()
          print("Inserted successfully")  
      except Exception:
          print("Already Inserted data into table")
  def update_consultation():
      try:
          mycursor.execute("UPDATE mytable set name='umesh' where consultation_id=24211")
          mydb.commit()
          print("updated successfully")
      except Exception:
          print("Already inserted dat into table")
  def Delete_consultation():
      try:
          mycursor.execute("delete from mytable where consultation_id=24211")
          mydb.commit()
          print("deleted successfully")
      except Exception:  
          print(" issue while deleting")      
cd=ConsultationDetails
cd.createdb()
cd.useDB()
cd.create_consultation()
cd.insert_consultation()
cd.update_consultation()