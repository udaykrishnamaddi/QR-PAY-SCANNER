import cv2
from pyzbar.pyzbar import decode

def start_scanner():

    decoded_data=''

    # creating the qr reader
    scanner = cv2.VideoCapture(0)

    while True:

        # reading a frame
        success, image = scanner.read()

        # if failure in opening camera
        if not success:
            print('Failed to open camera')
            break

        # showing the captured image frame
        cv2.imshow('QR CODE SCANNER', image)

        for qrcode in decode(image):
            decoded_data = qrcode.data.decode('utf-8')

        if cv2.waitKey(1) and len(decoded_data)>1:
            break

    scanner.release()
    cv2.destroyAllWindows()

    return eval(decoded_data)