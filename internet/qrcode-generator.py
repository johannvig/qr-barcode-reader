import qrcode



qr = qrcode.QRCode(
    version=1, #between 1 and 40 choose the complexity of youe qrcode
    error_correction=qrcode.constants.ERROR_CORRECT_M, #About 15% or less errors can be corrected
    box_size=10, #box size that contain the qrcode
    border=4, #border size
)
qr.add_data('https://github.com/johannvig')#put the internet link here
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white") #choose the color of the qrcode

img.save("some_file.png")#type the name of your image
