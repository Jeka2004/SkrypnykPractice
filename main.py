def MySortFunction(order, field):
    data = [
        {"name": "A", "price": 1.1},
        {"name": "B", "price": 0.9},
        {"name": "C", "price": 0.8},
        {"name": "D", "price": 0.7},
        {"name": "E", "price": 0.6},
        {"name": "F", "price": 0.5},
        {"name": "G", "price": 0.4},
        {"name": "H", "price": 0.3},
        {"name": "I", "price": 0.2},
        {"name": "J", "price": 0.1},
    ]

    def compare_string_eng(str1, str2):
        len_str1 = len(str1)
        len_str2 = len(str2)
        min_len = min(len_str1, len_str2)

        for i in range(min_len):
            if ord(str1[i]) < ord(str2[i]):
                return -1
            elif ord(str1[i]) > ord(str2[i]):
                return 1

        if len_str1 < len_str2:
            return -1
        elif len_str1 > len_str2:
            return 1
        else:
            return 0

    def compare_values(value1, value2):
        if value1 < value2:
            return -1
        elif value1 > value2:
            return 1
        else:
            return 0

    n = len(data)
    for i in range(n-1):
        for j in range(n-i-1):
            if order == "asc":
                if field == "name":
                    if compare_string_eng(data[j][field], data[j+1][field]) > 0:
                        data[j], data[j+1] = data[j+1], data[j]
                elif field == "price":
                    if compare_values(data[j][field], data[j+1][field]) >0:
                        data[j], data[j+1] = data[j+1], data[j]
            elif order == "desc":
                if field == "name":
                    if compare_string_eng(data[j][field], data[j+1][field]) <0:
                        data[j], data[j+1] = data[j+1], data[j]
                elif field == "price":
                    if compare_values(data[j][field], data[j+1][field]) <0:
                        data[j], data[j+1] = data[j+1], data[j]
    return data

print(MySortFunction("asc", "name"))
print(MySortFunction("asc", "price"))
print(MySortFunction("desc", "name"))
print(MySortFunction("desc", "price"))
