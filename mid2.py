word="I study at Khazar Universty"
word.replace('U','u')
word.replace('I','i')
countofU=word.count('u')
countofI=word.count('i')
if countofU>countofI:
    print("Ularin sayi Iden coxdur")
else:
    print("Ilerin sayi coxdur")

