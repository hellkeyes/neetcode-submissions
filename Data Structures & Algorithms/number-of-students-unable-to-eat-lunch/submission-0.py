class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        x = len(students)
        student_prefer = Counter(students)

        for i in sandwiches:
            if student_prefer[i] == 0:
                break
            else:
                x -= 1
                student_prefer[i] -= 1

        return x

# obj = Solution()
# students = [1,1,0,1]
# sandwiches = [0,1,0,1]

# print(obj.countStudents(students, sandwiches))