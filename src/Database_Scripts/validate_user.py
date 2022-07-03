from src.Database_Scripts import connect_to_db as db_connector


def is_user_valid(userData):

    username = userData['username']
    decryptedPassword = userData['decryptedPassword']

    mydb = db_connector.get_db_obj()
    mycursor = mydb.cursor()

    query = 'SELECT PIN FROM CUSTOMER_DETAILS WHERE USERNAME = %s'

    mycursor.execute(query, (username, ))
    myresult = mycursor.fetchall()

    for password in myresult:

        if password[0]==decryptedPassword:

            mycursor.close()
            mydb.close()

            return True

    else:

        mycursor.close()
        mydb.close()

        return False    