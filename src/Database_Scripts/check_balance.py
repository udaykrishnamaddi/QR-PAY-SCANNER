from src.Database_Scripts import connect_to_db as db_connector

def sufficient_balance(userData):

    mydb = db_connector.get_db_obj()
    mycursor = mydb.cursor()

    query = 'SELECT BALANCE FROM CUSTOMER_DETAILS WHERE USERNAME = %s'
    mycursor.execute(query, (userData['username'], ))

    myresult = mycursor.fetchall()

    for balance in myresult:

        if balance[0]>=userData['bill']:

            mycursor.close()
            mydb.close()

            return True

    else:

        mycursor.close()
        mydb.close()

        return False