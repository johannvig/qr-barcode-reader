from barcode import EAN13 

number = '5901234123457' #put a random number

my_code = EAN13(number) #EAN13 is the international standart

my_code.save("new_code.png") #save with name that you want for your barcode
