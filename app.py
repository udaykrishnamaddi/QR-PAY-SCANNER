from src.Database_Scripts.check_balance import sufficient_balance
from src.Database_Scripts.validate_user import is_user_valid
from src.Database_Scripts.validate_qr import is_qr_valid
from src.Python_Scripts.decode_password import decryptPassword
from src.Python_Scripts.qr_scanner import start_scanner
from src.Database_Scripts.validate_prices import generate_bill
from src.Database_Scripts.accept_order import complete_transaction


def initialize_data(data):

    global userData 
    userData = data["userData"]
    global metaData
    metaData = data["metaData"]
    global foodData
    foodData = data["foodData"]
    global foodPrices
    foodPrices = data["foodPrices"]
    global stallData
    stallData = data["stallData"]

    # decrypt password
    userData['decryptedPassword'] = int(decryptPassword(userData['encryptedPassword']))


def home():

    # start qr scanner
    data = start_scanner()
    print()
    print(data, end='\n')

    if isinstance(data, dict):

        # initialize data components
        initialize_data(data)

        # validate qr code
        qr_status, message = is_qr_valid(userData, metaData)

        print(message)
        valid_user=False

        if qr_status:

            # validate user

            valid_user = is_user_valid(userData)

            if valid_user:
                print('Valid User')

            else:
                print('Invalid User')

        bill_status=False
        balance_status=False

        if valid_user:

            # compute bill by comparing prices in database and qr code
            bill_status, message = generate_bill(userData, stallData, foodData, foodPrices)

            if bill_status:
                print(userData['bill'], message)

                # verify sufficient balance in user account
                balance_status = sufficient_balance(userData)

                if balance_status:
                    print('Sufficient Balance')

                    transaction_status, message = complete_transaction(userData, metaData, stallData, foodData)

                    if transaction_status:
                        print(message)

                    else:
                        print(message)

                else:
                    print('Insufficient Balance')

            else:
                print(message)

    else:
        print("Didn't scan the QR perfectly!\nRestarting the QR Scanner")
        home()

    
if __name__=='__main__':
    home()