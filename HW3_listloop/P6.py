from typing import List
def P6(n1: int, n2: int) -> List[int]:
    ans_list = []
    ### Modify code here ###
    
    m1 = max(n1, n2)
    m2 = min(n1, n2)
    
    for i in range(m1-m2+1):
        ans_list.append(m1)
        m1 -= 1

    ### End of your code ###
    return ans_list

