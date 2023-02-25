from PyPDF2 import PdfReader
from os.path import join as p_join
import os
import re


def check_files_presence_kw(files: list, list_kw: list):
    result = dict()
    for kw in list_kw:
        exp = re.compile(kw, re.IGNORECASE)
        for doc in files:
            if any(pg for pg in PdfReader(doc).pages if exp.search(pg.extract_text())):
                result.setdefault(kw, [])
                result[kw].append(doc)
    return result


def get_files_only_pdf(path: str, extensions='.pdf') -> list:
    pdf_files = list()
    for root, folders, files in os.walk(path):
        pdf_files.extend(p_join(root, f) for f in files if f.endswith(extensions))
    return pdf_files


if __name__ == '__main__':
    files = get_files_only_pdf(r'../files')
    list_kw = ['USB', 'example']
    print(check_files_presence_kw(files, list_kw))


