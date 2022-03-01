from PyPDF2 import PdfFileMerger
from tkinter.filedialog import askopenfilenames

import os

# get the path to the output file
def get_path(filepath=''):

    if not '/' in filepath:
        return ''

    last_oc = filepath.rindex('/')
    return filepath[:last_oc+1]

# returns the file extension
def check_extension(filename):

    if '.' in filename: 
        n_file = filename.rindex('.')

        return filename[n_file+1:]
    
    return ''

# Remove characters that aren't allowed in a filename
def fix_filename(filename: str):
    bad_chars = ['*', '/', '\\', ':', '\"', '<', '>', '|', '?']
    for c in bad_chars:
        filename = filename.replace(c, '')

    if check_extension(filename) != 'pdf':
        filename = filename + '.pdf'

    return filename


# get user defined file name or default
def get_file_name():

    fname = input("Enter output file name: ")

    # return default
    if not fname:
        return 'out.pdf'

    fname = fix_filename(fname)

    return fname

# main function
def main():
        
    # file paths
    files = ()
    
    # first path
    file = askopenfilenames(title='Select first pdf(s) to combine') # show dialog box
    while file:
        files += file # append to tuple
        file = askopenfilenames(title='Select more pdfs to combine (cancel if finished)')
    
    # if there are multiple files
    if files:
        # merge the files
        merger = PdfFileMerger()

        print('merging files...')
        for pdf in files:
            if check_extension(pdf) == 'pdf':
                try:
                    merger.append(pdf)
                    print(f'\tMerged: {pdf}')
                except:
                    print(f'Error occured with \'{pdf}\', skipping')
        
        print('done!')

        # get path to directory
        dir_path = get_path(files[0])

        # get output name
        out_name = get_file_name()
        print(f'Saving file \'{out_name}\' ')

        new_fname = os.path.join(dir_path, out_name)
        merger.write(new_fname)

        merger.close()
    else:
        print('no pdf files to combine.')


if __name__ == "__main__":
    main()