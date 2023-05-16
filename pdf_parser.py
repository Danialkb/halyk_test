import PyPDF2


class PdfParser:

    def parse_pdf(self, pdf_path) -> str:
        parsed_text = []

        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)

            for page in pdf_reader.pages:
                text = page.extract_text()
                parsed_text.append(text)

        return '\n'.join(parsed_text)
