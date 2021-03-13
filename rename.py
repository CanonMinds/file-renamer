import os

""" 
Usage:
python rename.py
"""

def echo():
    line_signal = "-----------------"
    print(line_signal)

def open_directory():
    global path
    path = input(" Please provide target directory: ")
    return path

def list_pointfiles_in_folder():
    list_current_files = []
    print("\n UPDATED LIST OF FILES NOW IN THE FOLDER:")
    echo()
    filenames = os.listdir(path)
    for filename in filenames:
        if word_to_replace in filename:
            list_current_files.append(filename)
            print(filename)
    echo()
    print(" %s FILES NOW FOUND CONTAINING '%s'" % (len(list_current_files), word_to_replace))
    echo()
    print(" RENAMING SUCCESSFUL")

def renaming_pointfiles_withtif():
    echo()
    print(" HI! WELCOME TO RENAMING YOUR FILES by FRB")
    print(" PS: Still in beta-testing, please feel free to contact me for any feedback! Thank ya!")
    print(" HAPPY USING !")
    echo()

    path = open_directory()
    global word_to_replace

    try:
        filenames = os.listdir(path)
        if filenames:
            print(" YOUR TARGET DIRECTORY IS:\n", path)
            echo()
            total_count = len(filenames)
            print(" TOTAL FILES FOUND IN FOLDER: %s" % total_count)
            echo()
            word_to_change = input(" a.) Provide the sub-text you want to find and replace, (ex: '.tif'): \n FIND: ")
            echo()


            to_process = []
            for filename in filenames:
                if word_to_change in filename:
                    to_process.append(filename)
            print(" NO FILES FOUND CONTAINING THE EXACT SUB-TEXT")
            echo()

            if to_process:
                print("[%s out of %s] FOUND FILES CONTAINING '%s' :" % (len(to_process), total_count, word_to_change))
                echo()
                word_to_replace = input(" b.) Exact characters you would like it to become into: (ex: '.p1.tif.pointz'), \n RENAME INTO: ")
                echo()
                for file in to_process:
                    print(file)
                    os.rename(file, file.replace(word_to_change, word_to_replace))
                echo()
                list_pointfiles_in_folder()
            else:
                print(" RENAMING FAILED")

    except FileNotFoundError:
        echo()
        print(" OOPS SORRY, An invalid file path was given. Kindly check the path again.")
        echo()
        print(" NO FILES WERE PROCESSED")
        echo()
        print(" RENAMING FAILED")
    except OSError:
        print(" The filenae, directory name, or volume label syntax is incorrect.")
    except:
        raise

renaming_pointfiles_withtif()