import pdfplumber
from tkinter.filedialog import askopenfilename


# Extracts all text in a pdf file and displays returns it with page numbers.
def extract_pdf_text(pdf_path):
    with pdfplumber.open(pdf_path) as book:
        text_all = ''
        for page in book.pages:
            text_all += page.extract_text()
    return text_all


# Extracts all text in a pdf file and displays returns it with page numbers.
def extract_pdf_text_w_p(pdf_path):
    with pdfplumber.open(pdf_path) as book:
        text_all = ''
        c = 0
        for page in book.pages:
            text_all += "Page " + str(c) + ":\n" + page.extract_text() + "\n\n"
            c = c + 1
    return text_all


# Extracts the text for a specific page, and returns an error if page is out of bounds.
def extract_page_text(pdf_path, page_number):
    with pdfplumber.open(pdf_path) as book:
        if 1 <= page_number <= len(book.pages):
            return book.pages[page_number - 1].extract_text()
        else:
            raise ValueError(f"Page number {page_number} is out of range.")


# Extracts all text (line by line) in a pdf file and returns with page & line numbers.
def extract_pdf_lines_w_pl(pdf_path):
    with pdfplumber.open(pdf_path) as book:
        lines = []
        page = 0
        line = 0
        for each_page in book.pages:
            page_lines = each_page.extract_text_lines()
            for each_line in page_lines:
                text = each_line['text']
                lines.append({
                    'text': 'Page ' + str(page) + ", Line " + str(line) + "\n" + text,
                })
                line = line + 1
            page = page + 1
            line = 0
    return lines


# Extracts all text (line by line) in a pdf file.
def extract_pdf_lines(pdf_path):
    with pdfplumber.open(pdf_path) as book:
        lines = []
        for each_page in book.pages:
            page_lines = each_page.extract_text_lines()
            for each_line in page_lines:
                text = each_line['text']
                lines.append({
                    'text': text,
                })
    return lines


if __name__ == "__main__":
    what_to_do = input("AllText, TextP, PageText, Lines, LinesPL: ")
    if what_to_do == "AllText":
        # Example usage of extract_pdf_text
        pdf_path = askopenfilename()
        text = extract_pdf_text(pdf_path)
        print(text)
    elif what_to_do == "TextP":
        # Example usage of extract_pdf_text
        pdf_path = askopenfilename()
        text = extract_pdf_text_w_p(pdf_path)
        print(text)
    elif what_to_do == "PageText":
        # Example usage of extract_page_text
        pdf_path = askopenfilename()
        try:
            page_number = int(input("Page Number: "))  # Replace with the desired page number
            text = extract_page_text(pdf_path, page_number)
            print(text)
        except ValueError as e:
            print(e)
    elif what_to_do == "Lines":
        # Example usage of extract_pdf_lines
        pdf_path = askopenfilename()
        lines = extract_pdf_lines(pdf_path)
        for line in lines:
            print(line['text'])
    elif what_to_do == "LinesPL":
        # Example usage of extract_pdf_lines
        pdf_path = askopenfilename()
        lines = extract_pdf_lines_w_pl(pdf_path)
        for line in lines:
            print(line['text'])




