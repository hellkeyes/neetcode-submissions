class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} 

        for word in strs:
            key = tuple(sorted(word)) #here we use sorted() but it returns list so we convert it to tuple. tuple is immutable and can be used in dict
            if key not in groups:   #if that key is not in dict we create a list 
                groups[key] = []

            groups[key].append(word) #we append that word to its family list

        return list(groups.values())

# this is the optimal solution - this didnt even come up in my brain. But whatever. 