# main.py
from docx_utils import process_document


def process_all_documents(file_paths):
    for file_path in file_paths:
        process_document(file_path)


if __name__ == "__main__":
    files_to_process = ["1.docx", "2.docx", "3.docx", "4.docx", "5.docx"]
    process_all_documents(files_to_process)
