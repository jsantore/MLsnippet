

def read_data(file_name:str)->list[tuple]:
    datafile = open(file_name)
    all_lines = datafile.readlines()
    data_vector = []
    for line in all_lines:
        data_tuple = line.split(':')
        if not data_tuple[1].isnumeric():
            continue  # the first line is the file format
        data_vector.append(data_tuple)
    return data_vector





