##https://leetcode.com/discuss/interview-question/5950077/Amazon-SDE-I-or-OA-or-10212024

# from typing import List
# # #assume snake starting position is 0, and it takes 1 second to go right or left. find the minimum time to eat "minimum_number_of_apples_to_eat"
# class SnakePosition:
#     def __init__(self, pos, left = None, right = None):
#         self.pos = pos
#         self.left = left
#         self.right = right

# def find_minimum_time_for_snake_to_eat_k_apples(list_of_coordinates_with_apples: List, minimum_number_of_apples_to_eat: int):
#     #no logic other than trying every combination
#     # state = (position, number_of_steps, num_of_apples_eaten)
#     # find_minimum_time_for_snake_to_eat_k_apples((position, number_of_steps, num_of_apples_eaten)) = min(
#     #     find_minimum_time_for_snake_to_eat_k_apples((left_pos, number_of_steps+abs(left_pos - position), num_of_apples_eaten-1)) if left_pos exists else float("inf"),
#     #     find_minimum_time_for_snake_to_eat_k_apples((right_pos, number_of_steps+abs(right_pos - position), num_of_apples_eaten-1)) if left_pos exists else float("inf")
#     #     )
#     def convert_apple_coordinates_into_linked_list_and_return_0_root(list_of_coordinates_with_apples):
#         head = SnakePosition(-float("inf"))
#         node = head
#         sorted_list_of_coordinates_with_apples = sorted(list_of_coordinates_with_apples)
#         have_we_inserted_zero = False
#         zero_root = None
#         for coord in sorted_list_of_coordinates_with_apples:
#             if not have_we_inserted_zero and node.pos < 0 <= coord:
#                 node.right = SnakePosition(0, node)
#                 zero_root = node.right
#                 have_we_inserted_zero = True
#                 node = node.right
#             node.right = SnakePosition(coord, node)
#             node = node.right
#         head.right.left = None
#         return zero_root
    
#     def find_minimum_time_for_snake_to_eat_k_apples_from_node(node, number_of_steps_taken, num_of_apples_left):
#         if num_of_apples_left == 0:
#             return number_of_steps_taken
#         save_current_node = node
#         left_node = node.left
#         right_node = node.right
#         if save_current_node.left:
#             save_current_node.left.right = save_current_node.right
#         if save_current_node.right:
#             save_current_node.right.left = save_current_node.left
#         minimum_time_for_snake_to_eat_k_apples_from_left_node =  find_minimum_time_for_snake_to_eat_k_apples_from_node(
#             left_node, 
#             number_of_steps_taken+abs(save_current_node.pos-left_node.pos),
#             num_of_apples_left-1
#             ) if left_node else float('inf')
#         minimum_time_for_snake_to_eat_k_apples_from_right_node =  find_minimum_time_for_snake_to_eat_k_apples_from_node(
#             right_node, 
#             number_of_steps_taken+abs(save_current_node.pos-right_node.pos),
#             num_of_apples_left-1
#             ) if right_node else float('inf')
#         save_current_node.left = left_node
#         save_current_node.right = right_node
#         if left_node:
#             left_node.right = save_current_node
#         if right_node:
#             right_node.left = save_current_node
#         return min(minimum_time_for_snake_to_eat_k_apples_from_left_node, minimum_time_for_snake_to_eat_k_apples_from_right_node)
#     zero_root = convert_apple_coordinates_into_linked_list_and_return_0_root(list_of_coordinates_with_apples)
#     minimum_time_for_snake_to_eat_k_apples_from_left_node =  find_minimum_time_for_snake_to_eat_k_apples_from_node(
#             zero_root, 
#             0,
#             minimum_number_of_apples_to_eat
#             )
#     return minimum_time_for_snake_to_eat_k_apples_from_left_node

# if __name__ == "__main__":
#     print(find_minimum_time_for_snake_to_eat_k_apples([-20,5,10], 3))
#     print(find_minimum_time_for_snake_to_eat_k_apples([-40, -20,5,10], 3))
#     print(find_minimum_time_for_snake_to_eat_k_apples([-40, -20,5,10, 15], 3))
#     print(find_minimum_time_for_snake_to_eat_k_apples([-31, -20,-5,5,100], 3))

#     # 5, 10, -20 = 30
#     # -20, 5, 10 = 35
#     # time complexity = 2^minimum_number_of_apples_to_eat
#     # space complexity = minimum_number_of_apples_to_eat

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
class Solution:
	def findMinimumTime(self, k: int, position: list[int]) -> int:
		position.sort()
		n = len(position)
		min_time = float('inf')
		for i in range(n - k + 1):
			left_most = position[i]
			right_most = position[i + k - 1]

			time_to_left_first = abs(left_most) + (right_most - left_most)
			time_to_right_first = abs(right_most) + (right_most - left_most)
			
			min_time = min(min_time, time_to_left_first, time_to_right_first)
		return min_time

	def findMinimumTime_Sanmesh(self, k: int, position: list[int]) -> int:
		position.sort()
		minimum_time = float('inf')
		for i in range(len(position)-k+1):
			test = 1
			minimum_time_left_end_to_right_end = abs(position[i+k-1]) + abs(position[i+k-1] - position[i])
			minimum_time_right_end_to_left_end = abs(position[i]) + abs(position[i+k-1] - position[i])
			minimum_time = min(minimum_time, minimum_time_left_end_to_right_end, minimum_time_right_end_to_left_end)
		return minimum_time

			
	def run_tests(self):
		test_cases = [
			{"input": (3, [-20, 5, 10]), "expected": 40},
			{"input": (1, [-10]), "expected": 10},
			{"input": (1, [10]), "expected": 10},
			{"input": (2, [-10, 10]), "expected": 30},
			{"input": (2, [-30, -20, -10]), "expected": 20},
			{"input": (2, [10, 20, 30]), "expected": 20},
			{"input": (4, [-50, -20, 5, 30]), "expected": 110},
			{"input": (3, [-109, -110, -111, -113, 60, -50, -40, 5]), "expected": 60},
			{"input": (2, [-1000, -9999, -9998, -9997, -9996, -9995, 2, 1]), "expected": 2},
			{"input": (3, [-109, -110, -111, -113, 30, -50, -40, 5]), "expected": 60},
			{"input": (1, [-999, -998, -997, -1, 100]), "expected": 1},
			{"input": (2, [-5000, -2000, 0, 1000, 5000]), "expected": 1000},
			{"input": (2, [99999, 100000, 99998, -1, -2, -3]), "expected": 2},
			{"input": (3, [-31, -20,-5,5,100]), "expected": 30},
		]

		total_tests = len(test_cases)
		passed_tests = 0

		for idx, case in enumerate(test_cases):
			k, position = case["input"]
			expected = case["expected"]
			# result = self.findMinimumTime(k, position)
			result = self.findMinimumTime_Sanmesh(k, position)
			if result == expected:
				print(f"Test case {idx + 1} passed!")
				passed_tests += 1
			else:
				print(f"Test case {idx + 1} failed: expected {expected}, got {result}, k: {k}, position: {position}")
		
		print(f"Tests passed: {passed_tests} out of {total_tests}")
		print(f"Percentage: {passed_tests / total_tests * 100:.2f}%")

if __name__ == "__main__":
	s = Solution()
	s.run_tests()