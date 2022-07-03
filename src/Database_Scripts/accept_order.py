from email import message
from src.Database_Scripts import connect_to_db as db_connector

# for generating queries for stall orders as each stall order table has different no.of cols
def generate_stall_orders_query(stallName):

    global query

    if stallName=='BombayChat':
        query = 'INSERT INTO BombayChat_Orders VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    elif stallName=='ChillZone':
        query='INSERT INTO ChillZone_Orders VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    elif stallName=='FastFood':
        query='INSERT INTO FastFood_Orders VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    elif stallName=='Frankie_Orders':
        query='INSERT INTO Frankie_Orders VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'

    return query


# for stall orders table data insertion
def stall_orders(userData, metaData, stallData, foodData):

    stall_orders_db = db_connector.get_db_obj()
    stall_orders_cursor = stall_orders_db.cursor()

    # insert related data into that stall's orders table

    stallName = stallData['stallName']

    insert_into_stall_orders = generate_stall_orders_query(stallName)

    stall_orders_data = [
        userData['username'], 
        metaData['generatedDay'], 
        metaData['generatedTime'] 
    ]

    # append quantity of each product ordered by user
    for food_item in foodData.keys():
        food_quantity = foodData[food_item]
        stall_orders_data.append(food_quantity)

    stall_orders_data.append(userData['bill'])

    try:
        # we insert data but we didn't commit because we commit only when amount is transferred
        stall_orders_cursor.execute(insert_into_stall_orders, stall_orders_data)
        return [True, stall_orders_db, stall_orders_cursor]

    except:
        stall_orders_cursor.close()
        stall_orders_db.close()
        return [False, None, None]


# for user account balance deduction of bill amount
def deduct_amount_from_user(userData):

    user_db = db_connector.get_db_obj()
    user_cursor = user_db.cursor()

    # deduct bill amount from user account balance
    username = userData['username']

    # get balance
    get_balance_query = "SELECT BALANCE FROM CUSTOMER_DETAILS WHERE USERNAME = %s"
    user_balance = 0

    user_cursor.execute(get_balance_query, (username, ))
    for balance in user_cursor:
        user_balance = balance[0]

    # update user balance
    user_balance-=userData['bill']

    # query
    deduct_bill_amount_query = "UPDATE CUSTOMER_DETAILS SET BALANCE = %s WHERE USERNAME = %s"

    try:
        user_cursor.execute(deduct_bill_amount_query, (user_balance, username))
        return [True, user_db, user_cursor]

    except:
        user_cursor.close()
        user_db.close()
        return [False, None, None]


# credit amount to stall owner
def credit_amount_to_stall(userData, metaData, stallData):

    stall_credit_db = db_connector.get_db_obj()
    stall_credit_cursor = stall_credit_db.cursor()

    # check is stall_credit table has this particular stallname for this day
    # if so update the credit amount
    # else create a row on this stallname and present date insert amount as the first customer for this day

    query_for_existence = "SELECT * FROM STALLS_CREDITS WHERE STALL_NAME = %s AND DATE = %s"

    # execute query
    stall_credit_cursor.execute(query_for_existence, (stallData['stallName'], metaData['generatedDay']))

    result = stall_credit_cursor.fetchall()

    # row is present so we update credit amount
    if len(result)>0:

        credit_amount=0

        # get present credit amount
        for amount in result:
            credit_amount = amount[0]

        # update credit amount
        credit_amount+=userData['bill']

        update_credit_amount_query = "UPDATE STALLS_CREDITS SET AMOUNT = "+str(credit_amount)+" WHERE STALL_NAME = "+stallData['stallName']+" AND DATE = "+metaData['generatedDay']

        try:
            stall_credit_cursor.execute(update_credit_amount_query)
            return [True, stall_credit_db, stall_credit_cursor]

        except:
            stall_credit_cursor.close()
            stall_credit_db.close()
            return [False, None, None]

    else:

        # this user is the first user of the day
        credit_amount=userData['bill']

        # insert amount into the stalls credits table
        credit_amount_query = "INSERT INTO STALLS_CREDITS VALUES (%s, %s, %s)"
        credit_amount_data = (stallData['stallName'], metaData['generatedDay'], userData['bill'])

        try:
            # execute query
            stall_credit_cursor.execute(credit_amount_query, credit_amount_data)
            return [True, stall_credit_db, stall_credit_cursor]

        except:
            stall_credit_cursor.close()
            stall_credit_db.close()
            return [False, None, None]


# update qr records
def update_qr_records(userData, metaData, stallData):

    qr_records_db = db_connector.get_db_obj()
    qr_records_cursor = qr_records_db.cursor()

    # query to insert this qr code details into the qr records
    insert_qr_record = "INSERT INTO QR_RECORDS VALUES(%s, %s, %s, %s, %s)"
    qr_record_data = [userData['username'], stallData['stallName'], metaData['generatedDay'], metaData['generatedTime'], userData['bill']]

    try:
        # execute query
        qr_records_cursor.execute(insert_qr_record, qr_record_data)
        return [True, qr_records_db, qr_records_cursor]

    except:
        qr_records_cursor.close()
        qr_records_db.close()
        return [False, None, None]


# complete the whole transaction process by updating necessay tables with relevant data
def complete_transaction(userData, metaData, stallData, foodData):

    stall_orders_status, stall_orders_db, stall_orders_cursor = stall_orders(userData, metaData, stallData, foodData)
    deduct_amount_status, user_db, user_cursor = deduct_amount_from_user(userData)
    credit_amount_status, stall_credit_db, stall_credit_cursor = credit_amount_to_stall(userData, metaData, stallData)
    update_qr_records_status, qr_records_db, qr_records_cursor = update_qr_records(userData, metaData, stallData)


    # if all worked perfectly we commit the changes
    if stall_orders_status and deduct_amount_status and credit_amount_status and update_qr_records_status:
        # commit all transactions
        stall_orders_db.commit()
        user_db.commit()
        stall_credit_db.commit()
        qr_records_db.commit()

        # close all cursors
        stall_orders_cursor.close()
        user_cursor.close()
        stall_credit_cursor.close()
        qr_records_cursor.close()

        # close all database connections
        stall_orders_db.close()
        user_db.close()
        stall_credit_db.close()
        qr_records_db.close()

        return [True, 'Transaction Successful']

    # if any one  of the transaction didn't work well we rollback every other transaction to protect integrity
    else:
        message=''

        if stall_orders_cursor==None:
            message+='\nProblem in inserting order details into stall orders table'

        else:
            stall_orders_db.rollback()
            stall_orders_cursor.close()
            stall_orders_db.close()

        if user_db==None:
            message+='\nProblem in deducting bill amount from user account'

        else:
            user_db.rollback()
            user_cursor.close()
            user_db.close()

        if stall_credit_db==None:
            message = '\nProblem in crediting amount to stalls'

        else:
            stall_credit_db.rollback()
            stall_credit_cursor.close()
            stall_credit_db.close()

        if qr_records_db==None:
            message = '\nProblem in updating the QR Code Records'

        else:
            qr_records_db.rollback()
            qr_records_cursor.close()
            qr_records_db.close()

    return [False, message]