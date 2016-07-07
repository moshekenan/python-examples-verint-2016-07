import os
import sys

if len(sys.argv) > 2:

    min_size_to_delete = 0

    search_dir = sys.argv[1]
    try:
        min_size_to_delete = int(sys.argv[2])

        print "searching for files in '%s' bigger than %d bytes" % (search_dir,min_size_to_delete)

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


    except ValueError:
        print "second argument <min_size_to_delete> must be numeric"


else:
    program_name = sys.argv[0]
    print "Please pass 2 arguments, Usage: %s <search_dir> <min_size_to_delete>" % program_name
