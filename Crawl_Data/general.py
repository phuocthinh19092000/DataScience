import os

import pandas


#Each website you crawl is a seperate project (folder)
def create_project_direction(directory):
    if not os.path.exists(directory):
        print('Creating project '+ directory)
        os.makedirs(directory)

#create_project_direction('thenewboston')

#Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    data = project_name + '/data.csv'
    col = ['Giá', 'DT', 'Đường', 'Phường-Xã', 'Quận-Huyện', 'Thành Phố', 'Hướng', 'Phòng ăn', 'Loại tin',
           'Đường trước nhà', 'Nhà bếp', 'Loại BDS', 'Pháp lý', 'Sân thượng', 'Chiều ngang', 'Số lầu',
           'Chổ để xe hơi', 'Chiều dài', 'Số phòng ngủ', 'Chính chủ']
    d = pandas.DataFrame(columns=col)
    d.to_csv(data)
    if not os.path.isfile(queue):
        write_file(queue , '')
    if not os.path.isfile(crawled):
        write_file(crawled , '')
    if not os.path.isfile(data):
        write_file(data, '')



#Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

#create_data_files('thenewboston', 'https://thenewboston.com/')

#Add data onto an existing file
def append_to_file(path,data):
    with open(path, 'a') as file:
        file.write(data + '\n')

#Delete the contents of a file
def delete_file_contents(path):
    with open(path,'w'):
        pass

# Read a file and convert each line to set items
def file_to_set(file_name):
    result = set()
    with open(file_name, 'rt') as f:
        for line in f:
            result.add(line.replace('\n', ''))
    return result

#Iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link )


