import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=2)

qr.add_data("https://www.youtube.com/channel/UCA27hbZOwxa4e5OYwrKmCnQ")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("youtube.png")