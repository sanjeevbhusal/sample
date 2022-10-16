with open("data.txt", "r") as f:
    data_set = f.readlines()
    state_detail_list = []

    for data in data_set:
        two_state_detail = data.split("    ")
        first_state_detail = two_state_detail[:3]
        state_detail_list.append(first_state_detail)

        second_state_detail = two_state_detail[3:]
        state_detail_list.append(second_state_detail) if len(second_state_detail) > 3 else None

print(state_detail_list)



