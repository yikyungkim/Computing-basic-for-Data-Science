def P2(L1: list, L2: list, L3: list) -> int:
    ans = 0
    ### Modify code here ###

    lengths = [len(L1), len(L2), len(L3)]
    ans += max(lengths)
    
    ### End of your code ###
    return ans