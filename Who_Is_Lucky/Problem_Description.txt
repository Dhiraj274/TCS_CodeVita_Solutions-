- Problem Description
There are a set of operators called bitwise operators which are used to perform bitwise calculations. As the name "bitwise" itself implies that these operators compares each bit of the
first operand to the corresponding bit of second operand. XOR is one of the bitwise operators which is also known as Exclusive OR. Mathematically, it is represented as ^.

Rahul and Rupesh are twins. One day it was raining heavily and they are bored of playing the usual indoor games. So they asked their mother to introduce a new game. She thought for a
while and discovered a new game. They both are given a common array consisting of n integers, and an integer value k. There are two more factors called A and B, which are binary
numbers. The rules of the game are given below:

. They play the game alternatively. Rahul starts first.
. Every time they have to select the maximum number from the array along with the adjacent k values on the left and right side of that max value. They will own those values and
should be deleted from the array. If there are no sufficient elements, then go with the values that are left.

. The person who got the last turn have to toggle the value of A and the person who got the maximum value by adding all those selected values have to toggle the value of B.

. The next step is to perform the xor of A and B. After performing xor, the person who got maximum value will win the game.

Note: When we toggle a binary number, then all the Os becomes 1s and vice versa.

- Constraints

1 <= len(arr) <= 10^2
0 <= arr[i] <= 10^5
1 <= k <= 10^2
1 <= k <= 10^2
A and B holds only binary numbers.

- Input

The first line consists of array elements separated by space.
Second line consists of Rahul's initial A and B values.
Third line consists of Rupesh's initial A and B values.
Fourth line consists of an integer k.

- Output

Print the name of the person who wins the game. If both wins, print both.

- Time Limit (secs)

1

- Examples

Example 1

Input

6211 1 13 0 8 4 16 9 19 3
01010 10
1010 01101
1

Output

Rahul

Explanation

The possible rounds of the game are given below.
Rahul - [9,19,3]
Rupesh - [4,16]
Rahul - [1,13,0]
Rupesh - [2,11,8]
Rahul - [6]

The summation of Rahul's values is 51 and Rupesh's values is 41. Since Rahul got maximum sum, he toggles the value of B. The last round of the game was carried out by Rahul. So he
toggles the value of A. The XOR of Rahul's A and B is greater than Rupesh's A and B. Since Rahul is the winner.

Example 2

Input

0 15 36 2 4 25 32 19 39 5
10 010
011 00
2

Output

Rahul

Explanation

The possible rounds of the game are given below.
Rahul - [0,15,36,2,4]
Rupesh - [25,32,19,3]
Rahul - [9,5]

The summation of Rahul's values is 74 and Rupesh's values is 76. Since Rupesh got maximum sum, he toggles the value of A. The last round of the game was carried out by Rahul. So
he toggles the value of B. The XOR of Rahul's A and B is 111 and Rupesh's A and B is 100. Since 111>100, Rahul won the game.