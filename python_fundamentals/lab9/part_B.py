class Document:
    def __init__(self, title: str):
        self.title = title

    def describe(self):
        return "This is a document"

class PDFDocument(Document):
    def describe(self):
        return "This document is a PDF"

class TextDocument(Document):
    def describe(self):
        return "This document is a text document"

documents = [PDFDocument("pdf1"), TextDocument("text1"), PDFDocument("pdf2"), TextDocument("text2")]

for document in documents:
    print(f"{document.title}, {document.describe()}")