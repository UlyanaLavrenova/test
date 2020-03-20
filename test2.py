import json


def main():
    with open("clients.txt") as clients:
        clients_list = json.load(clients)
    settings = read_settings()
    vendor_filter = settings['vendor']
    clients = apply_settings2(clients_list, vendor_filter, 'vendors', 'vendor', 'temp_vendors')
    print(clients)


def read_settings():
    try:
        with open("sett.txt") as settings_file:
            settings = json.load(settings_file)
            settings = settings[0]
    except FileNotFoundError:
        settings = "File not found"
    return settings


def apply_settings2(data, filter_list, filter_object1, filter_object2, filter_object3):
    data_temp = []
    if filter_list != []:
        for data_row in data:
            data_row[filter_object3] = data_row[filter_object1].copy()
            data_row[filter_object1] = []
            for row in data_row[filter_object3]:
                if row[filter_object2] in filter_list:
                    data_row[filter_object1].append(row)
            del data_row[filter_object3]
            if data_row[filter_object1] != []:
                data_temp.append(data_row)
        return data_temp
    else:
        return data


main()