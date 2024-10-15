import PyPDF2

def merge_pdfs(pdf_list, output):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == "__main__":

    PARENT_DIR = "G:\\polyulessons\\LSGI522\\Practicals\\Practical1"
    PATH = PARENT_DIR + "\\tmp\\"
    # Panzhiqing_CV.pdf files.pdf img-240618165302-001.pdf img-240618165332-001.pdf Visa MEEN-0012218-24.pdf Letter(1) MEEN-0012218-24.pdf
    # 需要合并的 PDF 文件列表
    pdf_files = ["Panzhiqing_CV.pdf", "files.pdf", "img-240618165302-001.pdf", "img-240618165332-001.pdf", "Visa MEEN-0012218-24.pdf", "Letter(1) MEEN-0012218-24.pdf","7c.pdf"]

    pdf_files = [PATH + pdf for pdf in pdf_files]

    # 合并后的 PDF 文件
    output_pdf = PATH + "PanZhiQing24037665G.pdf"

    merge_pdfs(pdf_files, output_pdf)