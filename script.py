def get_file_headers(f):
    header_full_name = {"Postal": "Postal Abbr", "FIPS": "FIPS Code"}
    headers_with_line_ending = list(header_full_name)
    headers_to_ignore = ["Abbr.", "Code"]
    cluttered_file_header_list = [f.readline() for _ in range(5)]
    header_list = []

    for headers_group_string in cluttered_file_header_list:
        headers_group__list = headers_group_string.split()
        for header in headers_group__list:
            header = header.strip()
            if header in headers_to_ignore or header in header_list:
                continue
            elif header in headers_with_line_ending:
                header = header_full_name[header]
                if header not in header_list:
                    header_list.append(header)
            else:
                header_list.append(header)

    return header_list


def merge_details(data, header_list):
    state_detail = {}
    for index, header in enumerate(header_list):
        state_detail[header] = data[index].strip()
    return state_detail


with open("data.txt", "r") as f:
    file_header_list = get_file_headers(f)
    file_data = f.readlines()
    state_detail_list = []

    for data in file_data:
        data_split = data.split("    ")
        length_of_data = len(data_split)

        if length_of_data == 6:
            first_state_detail = data_split[:3]
            second_state_detail = data_split[3:]
            state_detail_list.append(merge_details(first_state_detail, file_header_list))
            state_detail_list.append(merge_details(second_state_detail, file_header_list))
        else:
            state_detail_list.append(merge_details(data_split, file_header_list))


with open("state_detail.txt", "w") as f:
    f.write(str(state_detail_list))







