import pytest
from PyPDF2.errors import EmptyFileError
from my_pack.search_keywords_in_pdf_files import *


files = [file for file in get_files_only_pdf("../tests/files/work_dir/") if file.endswith('.pdf')]


def test_get_files_pdf_empty():
    empty_files = list()
    assert get_files_only_pdf("../tests/files/empty_dir") == empty_files


def test_get_files_pdf():
    global files
    assert get_files_only_pdf("../tests/files/work_dir/") == files


def test_check_files_presence_empty():
    global files
    list_kw = ['no-key-words']
    assert check_files_presence_kw(files, list_kw) == dict()


def test_check_files_presence():
    global files
    list_kw = ['USB']
    assert check_files_presence_kw(files, list_kw) == {'USB': ['../tests/files/work_dir/example.pdf']}


def test_check_files_empty_exceptions():
    with pytest.raises(EmptyFileError) as e:
        files = get_files_only_pdf("../tests/files/empty_file")
        check_files_presence_kw(files, ['kw'])
    assert "Cannot read an empty file" == e.value.args[0]

