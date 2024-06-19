# -*- coding: utf-8 -*-
"""UPI QR creator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JUMom7bZyhqS8prG18DxU08E13r3DDMu

**UPI QR Creator by Mr.Devashish Tambade.**

---


Do give me a  follow and connect... [linkdin](https://in.linkedin.com/in/devashish-tambade-228010196)
"""

# Only one time setup : please only run this for first time
!pip install qrcode[pil]

# Only one time setup : Input for Payee Name, Payee ID, Currency, and Auto-Download Toggle

# Function to set up the initial details
def setup_payee_details():
    global payee_name, payee_id, currency, auto_download
    payee_name = input("Enter the Payee Name : ")
    payee_id = input("Enter the Payee ID (e.g., xxxxxxx@paytm): ")
    currency = input("Enter the Currency (default is INR): ")
    if not currency:
        currency = 'INR'
    auto_download = input("Do you want to auto-download the QR code? (yes/no): ").strip().lower() == 'yes'

# Run the function to set up payee details
setup_payee_details()

# Display the entered details for confirmation
print(f"Payee Name: {payee_name}")
print(f"Payee ID: {payee_id}")
print(f"Currency: {currency}")
print(f"Auto-Download QR Code: {'Yes' if auto_download else 'No'}")

import qrcode
from IPython.display import Image, display
from google.colab import files

# Reusable Cell : Input for Amount and Generate UPI Link

# Function to generate the UPI QR
def generate_upi_link(amount):
    base_link = "upi://pay"
    customized_link = f"{base_link}?pa={payee_id}&pn={payee_name}&am={amount}&cu={currency}"
    return customized_link
def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Amount input
amount = input("Enter the Amount (e.g., 999): ")

new_upi_link = generate_upi_link(amount)
qr_image = generate_qr_code(new_upi_link)

# Save the QR code image
qr_image_file = "upi_qr_code.png"
qr_image.save(qr_image_file)

display(Image(filename=qr_image_file))

# Auto-download based on user input
if auto_download:
    files.download(qr_image_file)
else:
    print("You can download the QR code using the button in the next cell.")

from google.colab import files

# A button to download the QR code image manually.
def download_qr_code():
    files.download(qr_image_file)

if not auto_download:
    download_qr_code()