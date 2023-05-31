import qrcode

# Text or data to encode in the QR code
data = "https://testaventus-adityanawati.b4a.run/scan_qr/?uid=WEB01-03"

# Create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=4)

# Add data to the QR code
qr.add_data(data)

# Generate the QR code image
qr.make(fit=True)

# Get the QR code image as a PIL Image object
qr_image = qr.make_image(fill="black", back_color="white")

# Save the QR code image
qr_image.save("qr_code3.png")
