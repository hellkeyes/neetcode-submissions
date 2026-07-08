class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []     # final empty group

        for i in range(len(strs)):           
            res = count_freq(strs[i])         #we get character freq of that string
            found_family = False

            for j in range(len(groups)):       # now we compare if that string family is in the groups or not
                if res == groups[j][0]:       
                    groups[j].append(strs[i])
                    print('found family')
                    found_family = True
                    break
                    
            if found_family == False:          #if not we create new list and add it 
                temp_list = []
                temp_list.append(res)
                temp_list.append(strs[i])
                groups.append(temp_list)
                print('made family')

            if groups == []:                 # in start when the list is empty
                temp_list = []
                temp_list.append(res)
                temp_list.append(strs[i])
                groups.append(temp_list)

            
        for k in range(len(groups)):       # to remove the freq count we added that helped in comparison
            groups[k].remove(groups[k][0])

        return groups

def count_freq(my_string):    # just a function to get freq count of a string (you can use Counter)
    freq = {}
    for ch in my_string:
        if ch not in freq:
            freq[ch] = 1
        else:
            value = freq.get(ch) + 1
            freq[ch] = value
    return freq