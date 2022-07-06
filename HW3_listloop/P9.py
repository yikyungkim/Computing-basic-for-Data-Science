def P9(nested_list: list) -> list:    
    ans_list = []
    ##### Modify code Here #####
    
    l = len(nested_list[1])-1
    
    ans_list.append(nested_list[0][0])
    ans_list.append(nested_list[1][l])

    ##### End of your code #####
    return ans_list

