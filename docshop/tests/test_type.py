from django.test import TestCase

from docshop.settings import BASE_DIR
from pdfshop.models import PDF
from pdfshop.models import Text
from pdfshop.views import mime_type


class MimeTestCase(TestCase):
    def setUp(self):
        """Setup test case"""

        PDF.objects.create(name="PDF1", path=BASE_DIR+"/tests/files/pdf.pdf")
        PDF.objects.create(name="PDF2", path=BASE_DIR+"/tests/files/pdf.txt")

        Text.objects.create(name="Text1", path=BASE_DIR+"/tests/files/text.txt")
        Text.objects.create(name="Text2", path=BASE_DIR+"/tests/files/text.pdf")

    def test_pdfs(self):
        """PDF file is a PDF file even if it has no .pdf extension"""

        pdf1 = PDF.objects.get(name="PDF1")
        pdf2 = PDF.objects.get(name="PDF2")

        self.assertEqual(mime_type(pdf1.path), "application/pdf")
        self.assertEqual(mime_type(pdf2.path), "application/pdf")

    def test_texts(self):
        """Text file is a text file even if it has no .txt extension"""

        text1 = Text.objects.get(name="Text1")
        text2 = Text.objects.get(name="Text2")

        self.assertEqual(mime_type(text1.path), "text/plain")
        self.assertEqual(mime_type(text2.path), "text/plain")