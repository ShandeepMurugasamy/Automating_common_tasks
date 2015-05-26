__author__ = 'shandeepkm'
import os, sys, re

print os.getcwd()
print os.path.expanduser('~')

pdf_list = []
doc_list = []

pdf_re = re.compile(r'.*Shandeep.*\.pdf')
doc_re = re.compile(r'.*Shandeep.*\.doc')

pdf_path = r'/Users/shandeepkm/Desktop/Networking materials/PDF'
doc_path = r'/Users/shandeepkm/Desktop/Networking materials/DOC'

out = sys.stdout
with open('outputfile.txt', 'w') as outputfile:
    for rdir, direc, dir_file in os.walk(r'/Users/shandeepkm/Desktop/Networking materials/'):
        for items in dir_file:
            pdf_match = re.findall(pdf_re, items)
            doc_match = re.findall(doc_re, items)

            # for PDF files in the directory
            if pdf_match:
                pdf_list.append(pdf_match)
                if os.path.isdir(pdf_path):
                    matched_pdf_path = os.path.join(rdir, items)
                    target_pdf_path = os.path.join(pdf_path, items)
                    os.rename(matched_pdf_path, target_pdf_path)
                else:
                    os.mkdir('/Users/shandeepkm/Desktop/Networking materials/PDF/')
                    matched_path = os.path.join(rdir, items)
                    target_path = os.path.join(pdf_path, items)
                    os.rename(matched_path, target_path)
                    # for DOC files in the directory
            if doc_match:
                    doc_list.append(doc_match)
                    if os.path.isdir(doc_path):
                        matched_doc_path = os.path.join(rdir, items)
                        target_doc_path = os.path.join(doc_path, items)
                        os.rename(matched_doc_path, target_doc_path)
                    else:
                        os.mkdir('/Users/shandeepkm/Desktop/Networking materials/DOC/')
                        matched_doc_path = os.path.join(rdir, items)
                        target_doc_path = os.path.join(doc_path, items)
                        os.rename(matched_doc_path, target_doc_path)
print len(doc_list)
print len(pdf_list)


