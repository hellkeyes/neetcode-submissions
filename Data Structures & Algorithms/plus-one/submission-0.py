class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_list = []
        for i in digits:
            str_list.append(str(i))
        number = "".join(str_list)

        list_number = int(number) + 1

        final_list = list(str(list_number))

        return final_list

