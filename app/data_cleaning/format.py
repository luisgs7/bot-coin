def data_format(data: list) -> list:
    count = 0
    for item in data:
        if item == None:
            data[count] = 0
        count+=1        
    return data