def zero_sum(numbers):
    # returns is_valid_solution_exist, solution
    def dfs(index=0, current_sum=0, current_solution=[]):
        if current_sum == 0 and len(current_solution) >= 1:
            # print(current_solution)
            return True, current_solution
        if index >= len(numbers):
            return False, []
        #solution where we include index
        if numbers[index] != 0:
            current_solution.append(numbers[index])
            is_valid_solution_exist_when_include_value_at_index, solution_when_include_value_at_index = dfs(index+1, current_sum+numbers[index], current_solution)
            if is_valid_solution_exist_when_include_value_at_index:
                return True,  solution_when_include_value_at_index
            current_solution.pop()
        #solution where we dont include index
        is_valid_solution_exist_when_dont_include_value_at_index, solution_when_dont_include_value_at_index = dfs(index+1, current_sum, current_solution)
        if is_valid_solution_exist_when_dont_include_value_at_index:
            return True,  solution_when_dont_include_value_at_index
        return False,[]

    return dfs()

if __name__ == "__main__":
    testcases = [[1,-2,6,7,1], [1,2,-1], [0,0,1,3,6,-4,-1]]
    for testcase in testcases:
        is_valid_solution_exist, solution =  zero_sum(testcase)
        print(f"solution for {testcase}: {solution}")

# index = 2
# current_sum = 0
# current_solution = [1, -1]