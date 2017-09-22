def no_comma(column):
    new = []
    for i in range(len(column)):
        new.append(column[i].replace(',', ''))
    return new
