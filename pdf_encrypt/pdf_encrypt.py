from PyPDF2 import PdfWriter, PdfReader
from getpass import getpass

pdfwriter = PdfWriter()
pdfreader = PdfReader('file.pdf')

for page in range(len(pdfreader.pages)):
    pdfwriter.add_page(pdfreader.pages[page])

password = getpass(prompt='Введите пароль для шифровки: ')
pdfwriter.encrypt(password)

with open('protected.pdf', 'wb') as file:
    pdfwriter.write(file)