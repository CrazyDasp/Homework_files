def merge_files_txt(files, new_file):
    file_info = []
    for file_name in files:
        with open(file_name, 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            file_info.append((file_name, len(lines), lines))
    
    file_info.sort(key=lambda x: x[1])
    
    with open(new_file, 'w', encoding='UTF-8') as result_file:
        for file_name, num_lines, lines in file_info:
            result_file.write(f"{file_name}\n{num_lines}\n")
            result_file.writelines(lines)

merge_files_txt(['1.txt', '2.txt', '3.txt'], 'new.txt')