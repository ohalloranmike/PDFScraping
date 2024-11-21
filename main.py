import pdfplumber
from tkinter.filedialog import askopenfilename


def extract_pdf_text(pdf_path):
    with pdfplumber.open(pdf_path) as book:
        text_all = ''
        for page in book.pages:
            text_all += page.extract_text()

    return text_all


def extract_page_text(pdf_path, page_number):
    with pdfplumber.open(pdf_path) as book:
        if 1 <= page_number <= len(book.pages):
            return book.pages[page_number - 1].extract_text()
        else:
            raise ValueError(f"Page number {page_number} is out of range.")


def extract_pdf_lines(pdf_path):
    with pdfplumber.open(pdf_path) as book:
        lines = []
        for page in book.pages:
            page_lines = page.extract_text_lines()
            for line_info in page_lines:
                text = line_info['text']
                lines.append({
                    'text': text,
                })

    return lines



# Example usage of extract_page_text
pdf_path = askopenfilename()
try:
    page_number = 5  # Replace with the desired page number
    text = extract_page_text(pdf_path, page_number)
    print(text)
except ValueError as e:
    print(e)



'''
# Example usage of extract_pdf_lines
pdf_path = askopenfilename()
lines = extract_pdf_lines(pdf_path)

for line in lines:
    print(f"Text: {line['text']}")



# Example usage of extract_pdf_text
pdf_path = askopenfilename()
text = extract_pdf_text(pdf_path)
print(text)


pdf_path = askopenfilename()
with pdfplumber.open(pdf_path) as book:
    page_details = book.pages[1].extract_text()
    print(f"{page_details}\n")
'''