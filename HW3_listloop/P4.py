from typing import List
def P4(word_num_list: List[list]) -> list:
    ans_list = []
    ### Modify code here ###
    
    for i in range(len(word_num_list)):
        ans_list.append(word_num_list[i][0])
        ans_list.sort()
        
    ### End of your code ###  
    return ans_list
    