
import json
import base64
import pyqrcode
from pyqrcode import QRCode
import time
import png


# Using pyqrcode:
# Generate .svg file for HTML format
def QR_Gen_PyQrCode(encoded_data):
    # Generate QR code
    genQR = pyqrcode.create(encoded_data)
    
    # Create and save the svg file naming "invoice.svg" (H = W ~ 120)
    genQR.svg("invoice.svg", scale = 1.55844155844)

    # Create and save the png file naming "invoice_qr.png"
    genQR.png('invoice_qr.png', scale = 1.55844155844)
    


# Input Data fetched from Database Table:
hotel_code = 'AIZP209'
customer_id = 'A704'
checkin_date = '2023-04-12'
checkout_date = '2023-04-17'
room_no = '272'
total_adult = '2'
total_child = '1'
bill_paid_mode = 'upi'
paid_amount = '8762.0'

QR_Data = {
    'p01': hotel_code,
    'p02': customer_id,
    'p03': checkin_date,
    'p04': checkout_date,
    'p05': room_no,
    'p06': total_adult,
    'p07': total_child,
    'p08': bill_paid_mode,
    'p09': paid_amount
}

print("\nData in Dictionary format: ", QR_Data)

QRData_in_Json = json.dumps(QR_Data)

print("\nData in JSON format: ", QRData_in_Json)

encoded = base64.b64encode(QRData_in_Json.encode('utf-8'))

print("\n Data Encoded in base64: ",encoded, "\n")

QR_Gen_PyQrCode(encoded)




