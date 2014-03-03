import argparse

def _create_index(file_path, contents):
    file1 = file_path + '/index.php'
    with open(file1, 'w+') as out_file:
        out_file.write(contents)

def _contents(file_path):
    file1 = open(file_path, 'r')
    template = ''
    with file1 as in_file:
        for line in in_file:
            template += line + '\n'
    return template
        

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
    _create_index(path, contents)
