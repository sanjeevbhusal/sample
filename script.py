def get_file_headers(f):
    file_header_list = [f.readline() for _ in range(5)]
    header_with_line_endings = ["Postal", "FIPS"]
    file_header_list = [item for string in file_header_list for item in string.split()]
    result = []

    index = 0
    while index < len(file_header_list):
        value = file_header_list[index]

        if value in header_with_line_endings:
            index += 1
            next_value = file_header_list[index]
            if value + next_value not in result:
                result.append(value + next_value)
        else:
            if value not in result:
                result.append(value)
        index += 1
    return result


def main():
    with open("data.txt", "r") as f:
        file_header_list = get_file_headers(f)
        file_data = [state_info.strip() for line in f.readlines() for state_info in line.split("    ")]
        state_detail_list = []

        index = 0
        while index < len(file_data) - 1:
            state_info = {}
            for header in file_header_list:
                state_info[header] = file_data[index]
                index += 1
            state_detail_list.append(state_info)

        return state_detail_list


if __name__ == "__main__":
    with open("state_detail.txt", "w") as f:
        f.write(str(main()))







