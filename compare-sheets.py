'''
This is a script that takes two files and determines whether they are the same
If not, the deviant values are written to an output file
User may specify an optional directory to place output file in
Patrick Keaveny , 2014
'''

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path_one",
                        help="This argument specifies the file to read")
    parser.add_argument("file_path_two",
                        help="This argument specifies the file to compare")
    parser.add_argument("--v", "--file_path_two",
                        help="This is an optional argument if you want to write the output to a specific directory")
    args = parser.parse_args()
    file_one = open(args.file_path_one, 'r')
    file_two = open(args.file_path_two, 'r')
    users_first_set = file_one.readlines()
    users_second_set = file_two.readlines()
    if args.v:
        output_file = args.v + '/output.txt'
    else:
        output_file = 'output.txt'
    with open(output_file, 'w+') as out_file:
        for user in users_first_set:
            if user not in users_second_set:
                out_file.write(str(user))


        
        
