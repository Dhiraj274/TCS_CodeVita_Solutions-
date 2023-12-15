# This function is use to toggle bits in a binary string
def toggle_bits(binary_string):
  toggled_bits = ""
  for bit in binary_string:
    toggled_bits += str(int(bit,2) ^ 1)
  return toggled_bits

# Function to play game and determine the winner
def game(arr,k, rahul_ab_values, rupesh_ab_values):
    turn = 0
    select_of_rahul = []
    select_of_rupesh = []
    winner = None

    # Continue playing until the array is empty
    while len(arr) != 0:
        max_element = max(arr)
        index_of_max = arr.index(max_element)

        # Rahul's turn
        if turn == 0: 
            left_index = index_of_max - k
            right_index = index_of_max + k
            if left_index < 0 :
                left_index = 0
            if right_index > len(arr):
                right_index = len(arr)
            select_of_rahul.extend(arr[left_index:right_index + 1])
            del arr[left_index:right_index + 1]
            turn = 1
        # Rupesh"s turn
        else:
            left_index = index_of_max - k
            right_index = index_of_max + k
            if left_index < 0 :
                left_index = 0
            if right_index > len(arr):
                right_index = len(arr)
            select_of_rupesh.extend(arr[left_index:right_index + 1])
            del arr[left_index:right_index + 1]
            turn = 0

    # Calculate the sums of selected elements for each player
    sum_of_rahul = sum(select_of_rahul)
    sum_of_rupesh = sum(select_of_rupesh)

    #toggle bits based on the winner's sums
    if turn == 1 :
        rahul_ab_values[0] = toggle_bits(rahul_ab_values[0])
    else:
        rupesh_ab_values[0] = toggle_bits(rupesh_ab_values[0])

    if sum_of_rahul > sum_of_rupesh :
        rahul_ab_values[1] = toggle_bits(rahul_ab_values[1])
    elif sum_of_rupesh > sum_of_rahul:
        rupesh_ab_values[1] = toggle_bits(rupesh_ab_values[1])
    else:
        rahul_ab_values[1] =  toggle_bits(rahul_ab_values[1])
        rupesh_ab_values[1] = toggle_bits(rupesh_ab_values[1])
    
    # Perform XOR on the toggled binary values and determine the winner
    if int(rahul_ab_values[0], 2) ^ int(rahul_ab_values[1],2) > int(rupesh_ab_values[0], 2) ^ int(rupesh_ab_values[1], 2):
        return "Rahul"
    elif int(rahul_ab_values[0], 2) ^ int(rahul_ab_values[1],2) < int(rupesh_ab_values[0], 2) ^ int(rupesh_ab_values[1], 2):
        return "Rupesh"
    else:
        return "Both"

# Main function to take input and call the game function
def main():
    # Input array of values
    arr_values = input()
    arr = arr_values.split()
    arr = [int(i) for i in arr]
    
    # Input Rahul's A and B values
    rahul_A_and_B = input()
    rahul_AB_values = rahul_A_and_B.split()
    rahul_AB_values = [i for i in rahul_AB_values]

    # Input Rupesh's A and B values
    rupesh_A_and_B = input()
    rupesh_AB_values = rupesh_A_and_B.split()
    rupesh_AB_values = [i for i in rupesh_AB_values]

    # Input k value
    k = int(input())

    # Call the game function and print the winner
    winner = game(arr,k, rahul_AB_values, rupesh_AB_values)
    print(winner)


if __name__ == "__main__":
    main()