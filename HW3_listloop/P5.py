from typing import List
def P5(alphabet_list: List[str]) -> int:
    idx = 0
    ### Modify code here ###

    while alphabet_list[idx].islower():
        idx += 1
        if idx == len(alphabet_list):
            idx = -1
            break
            
    ### End of your code ###  
    return idx


