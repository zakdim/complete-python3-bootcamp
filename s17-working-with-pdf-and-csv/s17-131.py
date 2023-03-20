import PyPDF2


def s17_131():
    f = open('Working_Business_Proposal.pdf','rb')
    pdf_reader = PyPDF2.PdfReader(f)
    print(len(pdf_reader.pages))

    page_one = pdf_reader.pages[0]
    page_one_text = page_one.extract_text()
    # print(page_one_text)

    f.close()

    # Add page to PDF
    f = open('Working_Business_Proposal.pdf','rb')
    pdf_reader = PyPDF2.PdfReader(f)
    page_one = pdf_reader.pages[0]

    pdf_writer = PyPDF2.PdfWriter()
    # print(type(page_one))
    pdf_writer.add_page(page_one)

    pdf_output = open('Some_BrandNew_Doc.pdf', 'wb')
    pdf_writer.write(pdf_output)
    f.close()
    pdf_output.close()

    # Grab all the text from pdf file
    f = open('Working_Business_Proposal.pdf','rb')
    pdf_text = []
    pdf_reader = PyPDF2.PdfReader(f)
    for num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[num]
        pdf_text.append(page.extract_text())

    f.close()

    print(pdf_text[1])


if __name__ == '__main__':
    s17_131()
