from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os

def search (list, target):
    for i in range(len(list)):
        if (list[i] == target):
            return 1

    return 0

pdfs = "pdfs/07.pdf"

pages = convert_from_path(pdfs, 350)

i = 1

for page in pages:
    image_name = "page_" + str(i) + ".jpg"
    page.save(image_name, "JPEG")
    i = i+1

filelimit = i - 1

outfile = "out_text.txt"

f = open(outfile, "a")

keyWord = "1-BOVESPA"

for i in range(1, filelimit + 1):
    filename = "page_" + str(i) + ".jpg"
    text = str(((pytesseract.image_to_string(Image.open(filename)))))


    f.write(text)


    # Joga o texto para uma lista
    arr = text.split('\n')

    # Percorre a lista em busca da lista de ativos negociados
    for line in arr:
        if line != "" and line.find(keyWord, 0, 20) != -1:
            stock = line.split(' ')

            sizeLine = len(stock)

            x = range(sizeLine)
            newList = {}
            for j in x:
                #ativo = ''.join(stock[2:sizeLine - 5])
                ativo = stock[2:sizeLine - 5]


                if search(ativo, 'FRACIONARIO') == 1:
                    ativo.remove('FRACIONARIO')
                elif search(ativo, 'VISTA'):
                    ativo.remove('VISTA')
                elif search(ativo, 'WSTA'):
                    ativo.remove('WSTA')
                elif search(ativo, 'WISTA'):
                    ativo.remove('WISTA')

                newList["lado"] = stock[sizeLine - 1]
                newList["total"] = stock[sizeLine - 2]
                newList["unit"] = stock[sizeLine - 3]
                newList["qtde"] = stock[sizeLine - 4]
                newList["ativo"] = ' ' . join(ativo)

                typeOperation = 'SWING TRADE'
                if stock[sizeLine - 5] == 'D':
                    typeOperation = 'DAY TRADE'

                newList["tipo"] = typeOperation

            print(newList)


    print('\n')


    # Remove a imagem
    os.unlink(filename)



f.close()
    #print(arr)
    #print(text)
    #exit(22)



