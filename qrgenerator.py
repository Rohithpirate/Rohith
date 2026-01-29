import qrcode

data = input("Enter text or link: ")
qr = qrcode.make(data)
qr.save("qrcode.png")

print("QR Code generated!")
