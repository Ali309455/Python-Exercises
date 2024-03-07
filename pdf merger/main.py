import PyPDF2
import os 
def MergePDFs ():
    mergefile = PyPDF2.PdfMerger()
    for file in os.listdir():
        name,ext = os.path.splitext(file)
        if (ext == '.pdf'):
            mergefile.append(PyPDF2.PdfReader(f'{file}', 'rb'))
            print(MergePDFs())
            exit()
    # # mergefile.append(PyPDF2.PdfReader('sample_page2.pdf', 'rb'))
    # # mergefile.append(PyPDF2.PdfReader('sample_page3.pdf', 'rb'))
    
    # mergefile.write('Merged_Files(All).pdf')
        
# print(os.getcwd())