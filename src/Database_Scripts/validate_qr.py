from datetime import date, datetime
from src.Database_Scripts import connect_to_db as db_connector

def is_qr_valid(userData, metaData):

    global message

    mydb = db_connector.get_db_obj()
    mycursor = mydb.cursor()

    username = userData['username']
    generatedDay = metaData['generatedDay']
    generatedTime = metaData['generatedTime']

    query = "SELECT GENERATED_DAY, GENERATED_TIME FROM QR_RECORDS WHERE USERNAME = %s"

    mycursor.execute(query, (username, ))

    myresult =  mycursor.fetchall()

    for row in myresult:
        if row[0]==generatedDay and row[1]==generatedTime:

            message = 'Generate a new QR Code (as QR Code has been already used)'

            mycursor.close()
            mydb.close()
            return [False, message]

    # validate qr by generation time
    else:

        mycursor.close()
        mydb.close()

        today = date.today()
        current_date = today.strftime("%d/%m/%Y")
        
        now = datetime.now()

        if generatedDay==current_date:
            
            date_list = generatedDay.split('/')
            time_list = generatedTime.split(':')

            generated = datetime(int(date_list[2]), int(date_list[1]), int(date_list[0]), int(time_list[0]), int(time_list[1]), int(time_list[2]))

            difference = now - generated
            duration_in_seconds = difference.total_seconds()

            minutes = divmod(duration_in_seconds, 60)[0]
            
            if minutes<15.0:
                message='QR Code is Valid'
                return [True, message]

            else:
                message='QR Code is expired by exceeding time limit'
                return [False, message]

        else:
            message='QR Code is expired by exceeding time limit'
            return [False, message]
