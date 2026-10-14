#Example: Generate all possible subset (the power set) of a list.
# Example input: [1,2,3]
#expected output:
# [[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3],[]]

def subsets(nums):
    result = []
    def backtrack(index, path):
#Path: Current subset being built
        if index == len(nums):
            result.append(path)
            return
        backtrack(index + 1, path + [nums[index]])
        backtrack(index + 1, path)
    backtrack(0,[])
    return result

print(subsets([1,2,3]))