from database import db_setup
from pdf_parser import PdfParser


def main():
    pdf_path = '/Users/mak/WebstormProjects/front/halykTEST/pdf_docs/attachment-2.pdf'

    pdf_parser = PdfParser()
    database = db_setup()

    parsed_text = pdf_parser.parse_pdf(pdf_path)
    database.save_pdf_data(pdf_path, parsed_text)


if __name__ == '__main__':
    main()
