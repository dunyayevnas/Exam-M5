import threading

import os
import pdfkit


def convert_to_pdf(url, pdf_filename, config, output_folder):
    pdfkit.from_url(url, output_folder+pdf_filename, configuration=config)


threads = []
path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
output_folder = os.path.join(os.getcwd(), "paronims\\")
os.makedirs(output_folder, exist_ok=True)


for i in range(1, 11):
    url = "https://tilshunos.com/paronims/?page=" + str(i)
    pdf_filename = str(i) + '.pdf'
    t = threading.Thread(target=convert_to_pdf, args=(url, pdf_filename, config, output_folder))
    threads.append(t)
    t.start()


for i in threads:
    t.join()