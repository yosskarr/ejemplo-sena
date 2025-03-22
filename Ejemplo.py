import qrcode
qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,

)
var="juan diego gay"
qr.add_data(var)
qr.make(fit=True)	

img= qr.make_image(fill_color = 'black', back_color='white')

img.save('archivo3.png')