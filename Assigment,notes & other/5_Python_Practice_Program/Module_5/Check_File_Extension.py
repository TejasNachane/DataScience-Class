exe = ['gif', 'png', 'jpeg', 'jpg', 'svg', 'txt']

file_exe = input(" Insert file with extension: ").split('.')

if len(file_exe) >= 2:
    Extension = file_exe[-1].lower()

    if Extension in exe:
        print("File extension exist")
    else:
        print("Extension file does not exists")
else:
    print("File does not have an extension")