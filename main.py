from fastapi import FastAPI
import mysql.connector

mydb = mysql.connector.connect(
  host="35.200.246.57",
  user="root",
  password="root",
)

connection = ''
# check if connection was successful
cursor = mydb.cursor()

sql = "INSERT INTO `hungry-test`.`users` (`Email`, `FirstName`, `LastName`) VALUES ('johndoe@example.com', 'John', 'Doe')"
success = ""
try:
    cursor.execute(sql)
    mydb.commit()
    success = "yeeees"
except:
    mydb.rollback()
    print("Error occurred while inserting data into employees table")
app = FastAPI()


@app.get("/")
def home():
    return {"message":"Hello World " +success}
