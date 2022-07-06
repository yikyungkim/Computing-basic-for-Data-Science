from typing import List
def P3(num_list: List[int]) -> List[int]:
    ans_list = []
    ### Modify code here ###
    
    for i in range(len(num_list)):
        if num_list[i] != 0:
            ans_list.insert(i, -num_list[i])
        else:
            ans_list.insert(i, 0)
        
    ### End of your code ###   
    return ans_list
    