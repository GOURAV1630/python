import PyPDF2 as p

file = open ('D:/Computer%20Netwroks%20LAB%20FILE%20-%206th%20sem.pdf','rb')
pd = p.PdfFileReader(file)

x = pd.getPage(0)

print(x.extracttext())

