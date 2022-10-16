def merge_details(state_info, key_list):
    state_detail = dict.fromkeys(key_list)
    for index, detail in enumerate(state_info):
        detail = detail.strip()
        if index == 0:
            state_detail["State"] = detail
        elif index == 1:
            state_detail["Postal Abbr."] = detail
        else:
            state_detail["FIPS Code"] = int(detail)
    return state_detail


with open("data.txt", "r") as f:
    key_list = [key.strip() for key in f.readline().split("    ")]
    data_set = f.readlines()
    state_detail_list = []

    for data in data_set:
        data_split = data.split("    ")
        length_of_data = len(data_split)

        if length_of_data == 6:
            first_state_detail = data_split[:3]
            second_state_detail = data_split[3:]
            state_detail_list.append(merge_details(first_state_detail, key_list))
            state_detail_list.append(merge_details(second_state_detail, key_list))
        else:
            state_detail_list.append(merge_details(data_split, key_list))

with open("state_detail.txt", "w") as f:
    f.write(str(state_detail_list))
#
#
#
#
#


# print(dict.fromkeys([('Java', 14), ('Python', 3), ('JavaScript', 6)]))
# print(dict.fromkeys(["state", "postal", "id"]))