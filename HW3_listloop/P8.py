from typing import List
def P8(num_list: List[float]):
    ans_list = []
    ##### Modify code Here #####
    
    for i in range(len(num_list)):
        if num_list[i] > 0:
            ans_list.append(num_list[i])

    ##### End of your code #####
    return ans_list
    

