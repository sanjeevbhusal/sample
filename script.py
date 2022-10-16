with open("data.txt", "r") as f:
    data_set = f.readlines()
    state_detail_list = []

    for data in data_set:
        data_split = data.split("    ")
        length_of_data = len(data_split)

        if length_of_data == 6:
            first_state_detail = data_split[:3]
            second_state_detail = data_split[3:]
            state_detail_list.append([detail.strip() for detail in first_state_detail])
            state_detail_list.append([detail.strip() for detail in second_state_detail])
        else:
            state_detail_list.append([detail.strip() for detail in data_split])


with open("state_detail.txt", "w") as f:
    f.write(str(state_detail_list))





