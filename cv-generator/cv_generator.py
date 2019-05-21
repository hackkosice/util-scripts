import os
from PyPDF2 import PdfFileReader, PdfFileWriter

special_chars = '%_&#$~^'
r_constant = 185

with open('cvs.txt', 'r', encoding='utf8') as f:
    arr = [x[:-1] for x in f.readlines()]

data = []
prev = 0
for i in range(len(arr)):
    if arr[i]=='%%%-----%%%':
        data.append(arr[prev:i])
        prev = i+1

for i in range(len(data)//2):
    with open(f'cv_{i+r_constant}.txt', 'w', encoding='utf8') as f:
        for line in data[2*i]:
            step = 0
            for j in range(len(line)):
                if line[j+step] in special_chars:
                    line = line[:j+step]+'\\'+line[j+step:]
                    step += 1
                elif line[j+step]=="´":
                    line = line[:j+step]+"'"+line[j+step+1:]
                elif 'I will go to ^^' in line:
                    k = line.find('^^')
                    line = line[:k]+'  '+line[k+2:]
            if 'part_time' in line:
                k = line.find('part_time')
                l = line[:k+4]+' '+line[k+5:]
            elif 'full_time' in line:
                k = line.find('full_time')
                l = line[:k+4]+' '+line[k+5:]
            else:
                l = line
            f.write(l+'\n')
    os.rename(f'cv_{i+r_constant}.txt', f'cv_{i+r_constant}.tex')
    os.system(f'pdflatex cv_{i+r_constant}.tex')

    r = data[2*i+1][0]
    s = r[r.find('cv=')+3:r.find('=cv')]

    print(i+r_constant)
    if s[-4:]=='.pdf':
        secure = True
    elif s:
        secure = False
        print(f'CV {i+r_constant} has wrong suffix')
        print(s[-4:])

    if s and secure:
        output = PdfFileWriter()

        pdfOne = PdfFileReader(open(f'cv_{i+r_constant}.pdf', 'rb'))
        pdfTwo = PdfFileReader(open(s, 'rb'))

        output.addPage(pdfOne.getPage(0))
        output.addPage(pdfTwo.getPage(0))

        outputStream = open(r'hacker_{}.pdf'.format(i+r_constant), 'wb')
        output.write(outputStream)
        outputStream.close()
    else:
        os.rename(f'cv_{i+r_constant}.pdf', f'hacker_{i+r_constant}.pdf')

    for p in ['aux', 'log', 'out', 'tex']:
        try:
            os.remove(f'cv_{i+r_constant}.{p}')
        except(FileNotFoundError):
            pass
