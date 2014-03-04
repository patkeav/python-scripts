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
Function for creating css file
    @file_path = the directory/folder where the index should go
    @contents = contents to fill the index page with
'''
def _create_css_page(file_path, contents):
    file1 = file_path + '/style.css'
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
            template += line 
    return template
        
'''
The main method
'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="This argument specifies the file path where the outputted web page will go.")
    parser.add_argument("--t", "--index_template",
                        help="This argument specifies the file path where the index template is drawn from.")
    parser.add_argument("--v", "--css_template",
                        help="This argument specifies the file path where the css template is drawn from.")
    args = parser.parse_args()
    path = args.file_path
    index_page = args.t
    css_page = args.v
    if index_page:
       index_contents = str(_contents(index_page))
    else:
        contents = 'Hello World!'
    if css_page:
        css_contents = str(_contents(css_page))
    else:
        contents = 'body { margin: 0; } '
    _create_index_page(path, index_contents)
    _create_css_page(path, css_contents)
