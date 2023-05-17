import qrcode as qr

userinput = input('Enter any string(url, name, small/large texts{anything textual}): ')

img = qr.make(userinput)
img.save('img2.png')