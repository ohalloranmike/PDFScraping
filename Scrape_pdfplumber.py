import pdfplumber
from tkinter.filedialog import askopenfilename



def count_pdf_pages(pdf_path):
    with pdfplumber.open(pdf_path) as book:
        page_count = len(book.pages)
        return page_count

# Extracts all text in a pdf file.
def extract_pdf_text(pdf_path):
    with pdfplumber.open(pdf_path) as book:
        text_all = ''
        for page in book.pages:
            text_all += page.extract_text()
    return text_all

# Extracts all text in a pdf file and returns it with page numbers.
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

# Extracts all text (line by line) in a pdf file and returns them with page & line numbers.
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

def get_image_info(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        image_info = pdf.images
    return image_info

if __name__ == "__main__":
    what_to_do = input("PageCount, AllText, TextP, PageText, Lines, LinesPL, ImageInfo: ")
    if what_to_do == "PageCount":
        #Returns the number of pages in a pdf file.
        pdf_path = askopenfilename()
        page_count = count_pdf_pages(pdf_path)
        print(page_count)
    elif what_to_do == "AllText":
        # Extracts all text in a pdf file.
        pdf_path = askopenfilename()
        text = extract_pdf_text(pdf_path)
        print(text)
    elif what_to_do == "TextP":
        # Extracts all text in a pdf file and returns it with page numbers.
        pdf_path = askopenfilename()
        text = extract_pdf_text_w_p(pdf_path)
        print(text)
    elif what_to_do == "PageText":
        # Extracts the text for a specific page, and returns an error if page is out of bounds.
        pdf_path = askopenfilename()
        try:
            page_number = int(input("Page Number: "))  # Replace with the desired page number
            text = extract_page_text(pdf_path, page_number)
            print(text)
        except ValueError as e:
            print(e)
    elif what_to_do == "Lines":
        # Extracts all text (line by line) in a pdf file.
        pdf_path = askopenfilename()
        lines = extract_pdf_lines(pdf_path)
        for line in lines:
            print(line['text'])
    elif what_to_do == "LinesPL":
        # Extracts all text (line by line) in a pdf file and returns them with page & line numbers.
        pdf_path = askopenfilename()
        lines = extract_pdf_lines_w_pl(pdf_path)
        for line in lines:
            print(line['text'])
    elif what_to_do == "ImageInfo":
        pdf_path = askopenfilename()
        image_info = get_image_info(pdf_path)
        for each in image_info:
            print(f"*  Page Number   : {each["page_number"]}\n")
            for key, value in each.items():
                print(f"{key}: {value}")
            print(f"\n")
        print(f"There are ({len(image_info)}) pages in the pdf file '{pdf_path}'")
