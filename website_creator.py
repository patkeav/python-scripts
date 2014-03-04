'''
This is a script that creates a basic website
Patrick Keaveny , 2014
'''

import argparse

'''
Function for creating index page
    @file_path = the directory/folder where the index should go
    @contents = contents to fill the index page with
'''
def _create_index_page(file_path, contents):
    file1 = file_path + '/index.php'
    with open(file1, 'w+') as out_file:
        out_file.write(contents)

'''
Function for creating the contents of the index
    @file_path = file to read as a template
'''
def _contents(file_path):
    file1 = open(file_path, 'r')
    template = ''
    with file1 as in_file:
        for line in in_file:
            template += line + '\n'
    return template
        
'''
The main method
'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="This argument specifies the file path where the outputted web page will go.")
    parser.add_argument("-t", "--template_file", help="This argument specifies the file path where the template is drawn from.")
    args = parser.parse_args()
    path = args.file_path
    if args.template_file:
        contents = str(_contents(args.template_file))
    else:
        contents = 'Hello World!'
    _create_index_page(path, contents)
 #   _create_css(contents)
