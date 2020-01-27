from PyPDF2 import PdfFileReader
import os
import argparse
from corr_file_name import make_correct  #, is_correct_filename

forbidden = ['/', '\\', ':', '*', '?', '"', '>', '<', '|', '+', '%', '!', '@']


def rename_pdf_file(src, dest):
    if os.path.exists(src):
        os.rename(src, dest)
    else:
        print(f'Path {src} is not exist.')


def get_name_and_author(dict_):
    title = dict_.get('/Title', '')
    author = dict_.get('/Author', '')
    title = make_correct(title, forbidden)
    author = make_correct(author, forbidden)
    return title, author


def get_pdf_info(filename, path):
    if filename.lower().endswith('.pdf'):
        try:
            with open(os.path.join(path, filename), 'rb') as f:
                pdf = PdfFileReader(f)
                pdf_info = pdf.getDocumentInfo()
            return get_name_and_author(pdf_info)
        except:
            return ('', '')


def main():
    parser = argparse.ArgumentParser(description='Renames a pdffile according to metadata')
    parser.add_argument('indir', type=str, help='Input directory for files')
    parser.add_argument('outdir', type=str, help='Input directory for files')
    namespace = parser.parse_args()
    inp_path  = namespace.indir
    out_path = namespace.outdir
    for filename in os.listdir(inp_path):
        name = ''
        current_file_info = get_pdf_info(filename, inp_path) # returned (title, author)
        for i in current_file_info:
            if i:
                name += '_'+ str(i)
            else:
                pass
        if name:
            new_name = os.path.join(out_path, f'{name}.pdf')
            old_name = os.path.join(inp_path, filename)
            rename_pdf_file(old_name, new_name)
        else:
            pass


if __name__ == '__main__':
    main()