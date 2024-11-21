import pdfplumber
from tkinter.filedialog import askopenfilename


# Extracts all text in a pdf file and displays returns it with page numbers.
def extract_pdf_text(pdf_path):
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


# Extracts all text (line by line) in a pdf file and returns with page numbers.
def extract_pdf_lines(pdf_path):
    with pdfplumber.open(pdf_path) as book:
        lines = []
        c = 0
        l = 0
        for page in book.pages:
            page_lines = page.extract_text_lines()
            for line_info in page_lines:
                text = line_info['text']
                lines.append({
                    'text': 'Page ' + str(c) + ", Line " + str(l) + "\n" + text,
                })
                l = l + 1
            c = c + 1
            l = 0

    return lines


'''
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


'''
# Example usage of extract_pdf_text
pdf_path = askopenfilename()
text = extract_pdf_text(pdf_path)
print(text)
'''