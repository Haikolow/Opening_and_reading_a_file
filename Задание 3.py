def file_reading():
    files = ['1.txt', '2.txt', '3.txt']
    str_files = []
    for file in files:
        with open(file, 'rt', encoding ="utf-8") as f:
            list_ = []
            for line in f:
                list_.append(line.strip())
            # print(tmp)
            list_.insert(0, str(len(list_)))
            print(list_)
            list_.insert(0, file)
            print(list_)
            str_files.append(list_)
    str_files.sort(key=len)
    print(str_files)

    file = '4.txt'
    with open(file, 'wt', encoding='utf-8') as f:
        for string in str_files:
            for j in string:
                f.writelines(j + '\n')
    return

file_reading()