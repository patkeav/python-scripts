'''
This is a script that takes two files and determines whether they are the same
If not, the deviant values are written to an output file
Patrick Keaveny , 2014
'''

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="This argument specifies the file to read")
    parser.add_argument("file_path_two", help="This argument specifies the file to write to")
    parser.add_argument("file_path_three", help="This argument specifies the file to compare")
    args = parser.parse_args()
    path_one = args.file_path
    path_three = args.file_path_three
    file_one = open(path_one, 'r')
    path_two = args.file_path_two
    file_three = open(path_three, 'r')
    all_users = file_one.readlines()
    written_users = file_three.readlines()
    with open(path_two, 'w') as out_file:
        for user in all_users:
            if user not in written_users:
                out_file.write(str(user))


        
        
