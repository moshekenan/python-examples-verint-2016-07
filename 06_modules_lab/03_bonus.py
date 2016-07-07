import os
import argparse

# Assign description to the help doc
parser = argparse.ArgumentParser(description='Script search directory to find and delete large files.')

# Add arguments
parser.add_argument('-d', '--directory', type=str, help='Directory path', required=True)
parser.add_argument('-s', '--size', type=int, help='minimum size to delete', required=True)

# Array for all arguments passed to script
args = parser.parse_args()

# Assign args to variables
search_dir = args.directory
min_size_to_delete = args.size

print "searching for files in '%s' bigger than %d bytes" % (search_dir, min_size_to_delete)

if os.path.exists(search_dir):
    for root, dirs, files in os.walk(search_dir):
        for name in files:
            #print "found file: %s/%s" % (root, name)

            full_path = "{}\{}".format(root,name)
            file_size = os.path.getsize(full_path)
            if file_size > min_size_to_delete:
                print "found file %s with size: %d bytes" % (full_path,file_size)
                print "if you want to delete this file enter 'd'"
                del_file = raw_input()
                if del_file == 'd':
                    os.remove(full_path)
else:
    print "The directory %s does not exists" % search_dir

