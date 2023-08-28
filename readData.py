

def read_data(file_name:str)->list[tuple]:
    datafile = open(file_name)
    all_lines = datafile.readlines()
    data_vector = []
    for line in all_lines:
        data_tuple = line.split(':')
        if not data_tuple[1].isnumeric():
            continue  # the first line is the file format
        data_item = (data_tuple[0], int(data_tuple[1]), int(data_tuple[2]))
        data_vector.append(data_item)
    return data_vector





