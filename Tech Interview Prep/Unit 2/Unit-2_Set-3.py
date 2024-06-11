"""
A mountain list is defined as a list that has at least three elements, where there exists some i with 0 < i < len(lst)-1 such that lst[0] < lst[1] < ... lst[i-1] < lst[i] and lst[i] > lst[i+1] > ... > lst[len(lst)-1].

Given such a mountain list lst as a parameter, write a function that finds and returns the highest peak (the index i of the maximum element).

Hint: This is a lists problem
"""
def peak_index_in_mountain_list(mountain_lst) :
    # for i in mountain_lst : print(i) = 0 3 8 0
    output = 0
    for i in mountain_lst :
        if i < mountain_lst[i-1] :
            return i
    
    
mountain_lst = [0,3,8,0]
peak = peak_index_in_mountain_list(mountain_lst)
print(peak)