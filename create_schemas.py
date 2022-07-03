from src.Database_Scripts import connect_to_db as connector

mydb = connector.getDBObj()

mycursor = mydb.cursor()

# create customer_details table
# mycursor.execute('CREATE TABLE CUSTOMER_DETAILS (NAME VARCHAR(20), USERNAME VARCHAR(20) PRIMARY KEY, PIN INT, BALANCE INT)')

# insert_customers = 'INSERT INTO CUSTOMER_DETAILS (NAME, USERNAME, PIN, BALANCE) VALUES (%s, %s, %s, %s)'
# customer_details = [

#         ('Santhosh Kumar', '20071A6620', 111111, 1000),
#         ('Sai Ritish', '20071A6626', 654321, 1000),
#         ('Uday Krishna', '20071A6627', 999999, 1000),
#         ('Harikesh', '20071A6629', 123456, 1000)

#     ]

# mycursor.executemany(insert_customers, customer_details)

# mydb.commit()

#creating Stalls Tables

# stall-FastFood

# create_table = "CREATE TABLE FastFood (FOOD_ITEM VARCHAR(20), PRICE INT)"
# mycursor.execute(create_table)

# insert_food_data = "INSERT INTO FastFood (FOOD_ITEM, PRICE) VALUES(%s, %s)"
# food_data = [

#         ('Veg Manchuria', 40),
#         ('Egg Manchuria', 50),
#         ('Egg Fried Rice', 40),
#         ('Manchuria Rice',	50),
#         ('Egg Noodles',	40),
#         ('Manchuria Noodles', 50)
        
#     ]

# mycursor.executemany(insert_food_data, food_data)

# mydb.commit()


# mycursor.execute('ALTER TABLE CUSTOMER_DETAILS ADD BALANCE INT')

# create_table = "CREATE TABLE ChillZone (FOOD_ITEM VARCHAR(20), PRICE INT)"
# mycursor.execute(create_table)

# insert_food_data = "INSERT INTO ChillZone (FOOD_ITEM, PRICE) VALUES(%s, %s)"
# food_data = [

#         ('Snickers', 30),
#         ('Snickers Pista', 30),
#         ('Ice Cream', 60),
#         ('Coca Cola', 20),
#         ('Mountain Dew', 20),
#         ('Pastry',	40)
                
#     ]

# mycursor.executemany(insert_food_data, food_data)

# mydb.commit()


# create_table = "CREATE TABLE Frankie (FOOD_ITEM VARCHAR(20), PRICE INT)"
# mycursor.execute(create_table)

# insert_food_data = "INSERT INTO Frankie (FOOD_ITEM, PRICE) VALUES(%s, %s)"
# food_data = [

#         ('Veg Roll',	40),
#         ('Egg Roll',	50),
#         ('Paneer Frankie',	80),
#         ('Chicken Frankie',	70)
                
#     ]

# mycursor.executemany(insert_food_data, food_data)

# mydb.commit()

# create_table = "CREATE TABLE BombayChat (FOOD_ITEM VARCHAR(20), PRICE INT)"
# mycursor.execute(create_table)

# insert_food_data = "INSERT INTO BombayChat (FOOD_ITEM, PRICE) VALUES(%s, %s)"
# food_data = [

#         ('Pani Puri',	20),
#         ('Ragada Chat',	30),
#         ('Samosa Chat',	30),
#         ('Pav Bhaji',	60),
#         ('Masala Puri',	30),
#         ('Bhel Puri',	30) 

#     ]

# mycursor.executemany(insert_food_data, food_data)

# mydb.commit()

# mycursor.execute(
#         "CREATE TABLE QR_RECORD"+
#         "(USERNAME VARCHAR(20),"+
#         "STALL_NAME VARCHAR(20),"+ 
#         "GENERATED_DAY VARCHAR(10),"+ 
#         "GENERATED_TIME VARCHAR(10),"+
#         "AMOUNT INT)"
#     )

# create stall orders table

# mycursor.execute(
        
#         "CREATE TABLE FastFood_Orders"+
#         "(USERNAME VARCHAR(20),"+ 
#         "DAY VARCHAR(10),"+ 
#         "TIME VARCHAR(10),"+
#         "Veg_Manchuria INT,"+
#         "Egg_Manchuria INT,"+
#         "Egg_Fried_Rice INT,"+
#         "Manchuria_Rice INT,"+
#         "Egg_Noodles INT,"+
#         "Manchuria_Noodles INT,"+
#         "AMOUNT INT)"

#     )

# mycursor.execute(
        
#         "CREATE TABLE Frankie_Orders"+
#         "(USERNAME VARCHAR(20),"+ 
#         "DAY VARCHAR(10),"+ 
#         "TIME VARCHAR(10),"+
#         "Veg_Roll INT,"+
#         "Egg_Roll INT,"+
#         "Paneer_Frankie INT,"+
#         "Chicken_Frankie INT,"+
#         "AMOUNT INT)"

#     )
    
# mycursor.execute(
        
#         "CREATE TABLE ChillZone_Orders"+
#         "(USERNAME VARCHAR(20),"+ 
#         "DAY VARCHAR(10),"+ 
#         "TIME VARCHAR(10),"+
#         "Snickers INT,"+
#         "Snickers_Pista INT,"+
#         "Ice_Cream INT,"+
#         "Coca_Cola INT,"+
#         "Mountain_Dew INT,"+
#         "Pastry INT,"+
#         "AMOUNT INT)"

#     )

# mycursor.execute(
        
#         "CREATE TABLE BombayChat_Orders"+
#         "(USERNAME VARCHAR(20),"+ 
#         "DAY VARCHAR(10),"+ 
#         "TIME VARCHAR(10),"+
#         "Pani_Puri INT,"+
#         "Ragada_Chat INT,"+
#         "Samosa_Chat INT,"+
#         "Pav_Bhaji INT,"+
#         "Masala_Puri INT,"+
#         "Bhel_Puri INT,"+
#         "AMOUNT INT)"

#     )

mycursor.execute('CREATE TABLE STALLS_CREDITS (STALL_NAME VARCHAR(20), DATE VARCHAR(10), AMOUNT INT)')