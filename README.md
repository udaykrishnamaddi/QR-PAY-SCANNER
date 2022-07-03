# QRPS-QR-SCANNER

# Use .env file to store your db credentials
# folder structure for .env file

<h3>|-src</h3>
  <h3>  |-Database_Scripts</h3>
  <h3>  |-Python_Scripts</h3>
  <h3>  .env</h3>
  
# contents inside .env

MY_USERNAME = your_root_username_here
MY_PASSWORD = your_db_password_here
MYDB = your_local_database_name_here

*(dont enclose credentials in quotes)

What's happening at the back?

1. Verify qr in qr records.
2. Found send invalid qr page.
3. Not found validate qr by time.
4. If qr validates verify user and password.
5. If balance is sufficient add this qr data of username and his ordered food details and amount to that particular stall table orders.
6. Add this qr to qr orders.
7. Deduct user balance.
8. If the customer is the first customer of the day in stalls_credits table no row will be present on that particular stall name.
    1. So directly insert bill as credit amount.
9. Else the customer is not the first customer of the day so update credit amount for that stall name and that particular date.
10. So here stall name and date together are primary key (composite primary key).
