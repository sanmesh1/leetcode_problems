from typing import List
#assume snake starting position is 0, and it takes 1 second to go right or left. find the minimum time to eat "minimum_number_of_apples_to_eat"
class SnakePosition:
    def __init__(self, pos, left = None, right = None):
        self.pos = pos
        self.left = left
        self.right = right

def find_minimum_time_for_snake_to_eat_k_apples(list_of_coordinates_with_apples: List, minimum_number_of_apples_to_eat: int):
    #no logic other than trying every combination
    # state = (position, number_of_steps, num_of_apples_eaten)
    # find_minimum_time_for_snake_to_eat_k_apples((position, number_of_steps, num_of_apples_eaten)) = min(
    #     find_minimum_time_for_snake_to_eat_k_apples((left_pos, number_of_steps+abs(left_pos - position), num_of_apples_eaten-1)) if left_pos exists else float("inf"),
    #     find_minimum_time_for_snake_to_eat_k_apples((right_pos, number_of_steps+abs(right_pos - position), num_of_apples_eaten-1)) if left_pos exists else float("inf")
    #     )
    def convert_apple_coordinates_into_linked_list_and_return_0_root(list_of_coordinates_with_apples):
        head = SnakePosition(-float("inf"))
        node = head
        sorted_list_of_coordinates_with_apples = sorted(list_of_coordinates_with_apples)
        have_we_inserted_zero = False
        zero_root = None
        for coord in sorted_list_of_coordinates_with_apples:
            if not have_we_inserted_zero and node.pos < 0 <= coord:
                node.right = SnakePosition(0, node)
                zero_root = node.right
                have_we_inserted_zero = True
                node = node.right
            node.right = SnakePosition(coord, node)
            node = node.right
        head.right.left = None
        return zero_root
    
    def find_minimum_time_for_snake_to_eat_k_apples_from_node(node, number_of_steps_taken, num_of_apples_left):
        if num_of_apples_left == 0:
            return number_of_steps_taken
        save_current_node = node
        left_node = node.left
        right_node = node.right
        if save_current_node.left:
            save_current_node.left.right = save_current_node.right
        if save_current_node.right:
            save_current_node.right.left = save_current_node.left
        minimum_time_for_snake_to_eat_k_apples_from_left_node =  find_minimum_time_for_snake_to_eat_k_apples_from_node(
            left_node, 
            number_of_steps_taken+abs(save_current_node.pos-left_node.pos),
            num_of_apples_left-1
            ) if left_node else float('inf')
        minimum_time_for_snake_to_eat_k_apples_from_right_node =  find_minimum_time_for_snake_to_eat_k_apples_from_node(
            right_node, 
            number_of_steps_taken+abs(save_current_node.pos-right_node.pos),
            num_of_apples_left-1
            ) if right_node else float('inf')
        save_current_node.left = left_node
        save_current_node.right = right_node
        if left_node:
            left_node.right = save_current_node
        if right_node:
            right_node.left = save_current_node
        return min(minimum_time_for_snake_to_eat_k_apples_from_left_node, minimum_time_for_snake_to_eat_k_apples_from_right_node)
    zero_root = convert_apple_coordinates_into_linked_list_and_return_0_root(list_of_coordinates_with_apples)
    minimum_time_for_snake_to_eat_k_apples_from_left_node =  find_minimum_time_for_snake_to_eat_k_apples_from_node(
            zero_root, 
            0,
            minimum_number_of_apples_to_eat
            )
    return minimum_time_for_snake_to_eat_k_apples_from_left_node

if __name__ == "__main__":
    print(find_minimum_time_for_snake_to_eat_k_apples([-20,5,10], 3))
    print(find_minimum_time_for_snake_to_eat_k_apples([-40, -20,5,10], 3))
    print(find_minimum_time_for_snake_to_eat_k_apples([-40, -20,5,10, 15], 3))
    print(find_minimum_time_for_snake_to_eat_k_apples([-31, -20,-5,5,100], 3))

    # 5, 10, -20 = 30
    # -20, 5, 10 = 35
    # time complexity = 2^minimum_number_of_apples_to_eat
    # space complexity = minimum_number_of_apples_to_eat