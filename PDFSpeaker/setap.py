import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def pdf_to_lists():
    input_path = 'input/'
    output_path = 'output/'
    fil_list = os.listdir(input_path)
    for fill in fil_list:
        if fill[4:].lower() != '.pdf': continue
        input_pdf = PdfFileReader(open(f'{input_path}/{fill}', 'rb'))
        for i_list in range(0, input_pdf.numPages):
            output_pdf = PdfFileWriter()
            output_pdf.addPage(input_pdf.getPage(i_list))
            fill_pdf = open(f'{output_path}/{i_list}-{fill}', 'wb')
            output_pdf.write(fill_pdf)


if __name__ == '__main__':
    pdf_to_lists()