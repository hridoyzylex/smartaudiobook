import pyttsx3 # importing python text to speech version 3
import PyPDF2 # importing python PDF version 2
book = open('The Alchemist.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages # output total number of pages
print(pages)
friend = pyttsx3.init()
for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    friend.say(text)
    friend.runAndWait()