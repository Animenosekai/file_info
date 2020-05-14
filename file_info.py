#                                  File Info
#
# for Python 3
# ©Anime no Sekai - 2020
#


# Imports
import os
import mimetypes
import data.ext_to_human_readable
import data.extension_desc
import data.type

########## TOOLS ##########
def get_size(bytes, suffix="B"):
    """
    Credit to PythonCode for this function.
    > https://www.thepythoncode.com/article/get-hardware-system-information-python
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_correct_path(path):
    indexes_of_slash = [i for i, ltr in enumerate(path) if ltr == "\\"]
    number_of_iterations = 0
    for index in indexes_of_slash:
        character_after_slash = path[index + 1 - number_of_iterations]
        print(character_after_slash)
        if character_after_slash == ' ' or character_after_slash == '/':
            path = path[:index - number_of_iterations] + path[index + 1 - number_of_iterations:]
            number_of_iterations += 1
    return path


########## INDIVIDUAL ##########

def exists(file):
    correct_path = get_correct_path(file)
    return(os.path.exists(correct_path))

def isdir(file):
    correct_path = get_correct_path(file)
    return(os.path.isdir(correct_path))

def isfile(file):
    correct_path = get_correct_path(file)
    return(os.path.isfile(correct_path))

def mimetype(file):
    mimetype = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        mimetype_tuple = mimetypes.guess_type(correct_path)
        mimetype = mimetype_tuple[0]
    else:
        mimetype = 'An error occured while getting the file'
    return(mimetype)

def base(file):
    file_base = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_base = os.path.basename(correct_path)
    else:
        file_base = 'An error occured while getting the file'
    return(file_base)

def path(file):
    file_path = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_path = os.path.abspath(correct_path)
    else:
        file_path = 'An error occured while getting the file'
    return(file_path)

def name(file):
    file_base = ''
    filename = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_base = os.path.basename(correct_path)
        filename, file_extension = os.path.splitext(file_base)
    else:
        filename = 'An error occured while getting the file'
    return(filename)

def extension(file):
    file_base = ''
    file_extension = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_base = os.path.basename(correct_path)
        filename, file_extension = os.path.splitext(file_base)
    else:
        file_extension = 'An error occured while getting the file'
    return(file_extension)

def size(file):
    size = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        size_in_bytes = os.path.getsize(correct_path)
        size = get_size(size_in_bytes)
    else:
       size = 'An error occured while getting the file'
    return(size)

def size_in_bytes(file):
    size_in_bytes = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        size_in_bytes = os.path.getsize(correct_path)
    else:
       size_in_bytes = 'An error occured while getting the file'
    return(size_in_bytes)

def file_stat(file):
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
    else:
        file_stat = 'An error occured while getting the file'
    return(file_stat)

def last_access(file):
    last_access = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_access = file_stat.st_atime
    else:
       last_access = 'An error occured while getting the file'
    return(last_access)

def last_access_nanoseconds(file):
    last_access_nanoseconds = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_access_nanoseconds = file_stat.st_atime_ns
    else:
       last_access_nanoseconds = 'An error occured while getting the file'
    return(last_access_nanoseconds)

def last_modification(file):
    last_modification = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_modification = file_stat.st_mtime
    else:
       last_modification = 'An error occured while getting the file'
    return(last_modification)

def last_modification_nanoseconds(file):
    last_modification_nanoseconds = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_modification_nanoseconds = file_stat.st_mtime_ns
    else:
       last_modification_nanoseconds = 'An error occured while getting the file'
    return(last_modification_nanoseconds)

def last_metadata_change(file):
    last_metadata_change = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_metadata_change = file_stat.st_ctime
    else:
       last_metadata_change = 'An error occured while getting the file'
    return(last_metadata_change)

def last_metadata_change_nanoseconds(file):
    last_metadata_change_nanoseconds = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_metadata_change_nanoseconds = file_stat.st_ctime_ns
    else:
       last_metadata_change_nanoseconds = 'An error occured while getting the file'
    
    return(last_metadata_change_nanoseconds)

def type(file):
    type = ''
    correct_path = get_correct_path(file)
    file_extension = extension(file)
    if os.path.isdir(correct_path):
        type = 'Folder/Directory'
    elif file_extension in data.type.archive():
        type = 'Archive'
    elif file_extension in data.type.audio():
        type = 'Audio'
    elif file_extension in data.type.backup():
        type = 'Backup'
    elif file_extension in data.type.book():
        type = 'eBook'
    elif file_extension in data.type.database():
        type = 'Database File'
    elif file_extension in data.type.developer():
        type = 'Developer'
    elif file_extension in data.type.disk_image():
        type = 'Disk Image'
    elif file_extension in data.type.encoded():
        type = 'Encoded File'
    elif file_extension in data.type.executable():
        type = 'Application/Executable'
    elif file_extension in data.type.developer():
        type = 'Developer'
    elif file_extension in data.type.font():
        type = 'Font'
    elif file_extension in data.type.image_3d():
        type = '3D Image'
    elif file_extension in data.type.plugin():
        type = 'Plugin'
    elif file_extension in data.type.preset():
        type = 'Preset/Settings'
    elif file_extension in data.type.raster_image():
        type = 'Image'
    elif file_extension in data.type.raw_image():
        type = 'Raw Image'
    elif file_extension in data.type.rom():
        type = 'ROM/Game File'
    elif file_extension in data.type.spreadsheet():
        type = 'Spreadsheet'
    elif file_extension in data.type.system():
        type = 'System File'
    elif file_extension in data.type.text():
        type = 'Text File'
    elif file_extension in data.type.vector_image():
        type = 'Vector Image'
    elif file_extension in data.type.video():
        type = 'Video'
    elif file_extension in data.type.web():
        type = 'Web Document'
    else:
        type = 'unknown'
    return type

def extension_to_human_readable(file_ext):
    result = data.ext_to_human_readable.file_extension_to_human_readable(file_ext)
    return result

def extension_info(file_ext):
    result = data.extension_desc.extension_info(file_ext)
    return result

def extension_description(file_ext):
    result = data.extension_desc.extension_description(file_ext)
    return result

def extension_usage(file_ext):
    result = data.extension_desc.extension_usage(file_ext)
    return result


########## GROUPS ##########

def get_path_info(file):
    path_info = {}
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        #FILENAME, EXTENSTION AND LOCATION
        try:
            file_base = os.path.basename(correct_path)
            file_path = os.path.abspath(correct_path)
            filename, file_extension = os.path.splitext(file_base)
            path_info['file_base'] = file_base
            path_info['file_path'] = file_path
            path_info['filename'] = filename
            path_info['file_extension'] = file_extension
        except:
            print("An error occured while getting this file's name")
            path_info['file_base'] = 'Error'
            path_info['file_path'] = 'Error'
            path_info['filename'] = 'Error'
            path_info['file_extension'] = 'Error'
    else:
       path_info['information'] = 'An error occured while searching for your file.'

    return(path_info)

def get_size_info(file):
    size_info = {}
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        #SIZE
        try:
            size_in_bytes = os.path.getsize(correct_path)
            size_info['size_in_bytes'] = size_in_bytes
            size_info['size'] = get_size(size_in_bytes)
        except:
            print("An error occured while getting this file's size")
            size_info['size_in_bytes'] = 'Error'
            size_info['size'] = 'Error'
    else:
       size_info['information'] = 'An error occured while searching for your file.'

    return(size_info)

def get_timestamps(file):
    timestamps_info = {}
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        #TIMESTAMPS
        try:
            file_stat = os.stat(correct_path)
            last_access = file_stat.st_atime
            last_access_nanoseconds = file_stat.st_atime_ns
            last_modif = file_stat.st_mtime
            last_modif_nanoseconds = file_stat.st_mtime_ns
            last_metadata_change = file_stat.st_ctime
            last_metadata_change_nanoseconds = file_stat.st_ctime_ns
            
            timestamps_info['file_stat'] = file_stat
            timestamps_info['last_access'] = last_access
            timestamps_info['last_access_nanoseconds'] = last_access_nanoseconds
            timestamps_info['last_modification'] = last_modif
            timestamps_info['last_modification_nanoseconds'] = last_modif_nanoseconds
            timestamps_info['last_metadata_change'] = last_metadata_change
            timestamps_info['last_metadata_change_nanoseconds'] = last_metadata_change_nanoseconds
        except:
            print("An error occured while getting timestamps for this file")
            timestamps_info['file_stat'] = 'Error'
            timestamps_info['last_access'] = 'Error'
            timestamps_info['last_access_nanoseconds'] = 'Error'
            timestamps_info['last_modification'] = 'Error'
            timestamps_info['last_modification_nanoseconds'] = 'Error'
            timestamps_info['last_metadata_change'] = 'Error'
            timestamps_info['last_metadata_change_nanoseconds'] = 'Error'
    else:
       timestamps_info['information'] = 'An error occured while searching for your file.'

    return(timestamps_info)







########## EVERYTHING ##########

def info(file):
    file_info = {}
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_info['exists'] = exists(file)
        file_info['isdir'] = isdir(file)
        file_info['isfile'] = isfile(file)
        file_info['mimetype'] = mimetype(file)
        file_info['base'] = base(file)
        file_info['given_path'] = file
        file_info['usable_path'] = correct_path
        file_info['name'] = name(file)
        file_info['extension'] = extension(file)
        file_info['size'] = size(file)
        file_info['size_in_bytes'] = size_in_bytes(file)
        file_info['full_file_stat'] = file_stat(file)
        file_info['last_access'] = last_access(file)
        file_info['last_access_nanoseconds'] = last_access_nanoseconds(file)
        file_info['last_modification'] = last_modification(file)
        file_info['last_modification_nanoseconds'] = last_modification_nanoseconds(file)
        file_info['last_metadata_change'] = last_metadata_change(file)
        file_info['last_metadata_change_nanoseconds'] = last_metadata_change_nanoseconds(file)
        file_info['type'] = type(file)
        file_info['human_readable_extension'] = extension_to_human_readable(file_info['extension'])
        file_info['extension_info'] = extension_info(file_info['extension'])
        file_info['extension_description'] = extension_description(file_info['extension'])
        file_info['extension_usage'] = extension_usage(file_info['extension'])
    else:
       file_info['information'] = 'An error occured while searching for your file.' 
    return file_info


"""
# Testing

os.system('cls' if os.name == 'nt' else 'clear')
file = input('File: ')
os.system('cls' if os.name == 'nt' else 'clear')
results = info(file)
print('{')
for info in results:
    print(info + ': ' + str(results[info]))
print('     }')
"""