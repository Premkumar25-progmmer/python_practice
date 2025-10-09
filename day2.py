import mysql.connector as mc
con=mc.connect (
    host=localhost,
    username=root,
    password=prem,
    database=student
    )
print("database connected")
