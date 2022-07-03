from src.Database_Scripts import connect_to_db as db_connector


# verify prices in qr code and database and generate bill if prices are match
def generate_bill(userData, stallData, foodData, foodPrices):

    bill = 0

    mydb = db_connector.get_db_obj()
    mycursor = mydb.cursor()

    stallName = stallData['stallName']

    print(stallName)

    query = 'SELECT * FROM '+stallName
    mycursor.execute(query)

    myresult = mycursor.fetchall()

    for row in myresult:
        db_price = row[1]
        # if data base price matches with qr price and 
        # quantity of that item selected is greater than 0
        # add it to bill
        if db_price == foodPrices[row[0]] and foodData[row[0]]>=0:
            bill+=db_price*foodData[row[0]]

        else:
            return [False, 'Update your local app for new prices\n'+row[0]+' :'+str(db_price)+'Rs']

    userData['bill']=bill
    return [True, 'Bill Generated Successfully']