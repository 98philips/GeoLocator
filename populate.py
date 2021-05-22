from connect import getConnection

mydb = getConnection()

mycursor = mydb.cursor()

sql = "INSERT INTO seller (name, lat, lon) VALUES (%s, %s, %s)"
s1 = ("s1", 11.309870, 75.755275)
s2 = ("s2", 11.306299, 75.764336)
s3 = ("s3", 11.330342, 75.768017)
mycursor.execute(sql, s1)
mycursor.execute(sql, s2)
mycursor.execute(sql, s3)
mydb.commit()