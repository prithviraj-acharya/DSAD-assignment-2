Problem Statement
A landlord owns a few acres of his property and rents/leases it out to someone else.
Now he wants to invest in real estate as a source of financial profit. He decided to sell
up to ‘x’ acres of his land in different regions for huge profit. There are ‘n’ different
regions with given acres of land he wants to sell in that area and along with its profit
value, here your task would be to select the acres of land within ‘x’ limit, such that the
total profit is maximized.
Note: you can select the complete acres of land available in that region or part of it
according to the ‘x’ limit as assumed. If there are multiple regions with the same profit
value, first select the region with few acres of land and so on.
Requirements:
1. Formulate an efficient algorithm using the Greedy Method.
2. Analyze the time complexity of your algorithm.
3. Implement the above problem statement using Python 3.7 or above.
Sample Input
Input should be taken in through a file called inputPS05.txt which has the fixed format
mentioned below:
Number of regions (n): 10
Maximum Acres of land he wants to sell (x): 16
Using the “/” as a field separator: Add the data as given below.
<Region name> / < Land in acres > / < profit in crores>
Example:
R1 / 3 / 80
R2 / 2 / 30
R3 / 4 / 20
and so on ...
For example, if there are 10 different regions then land in acres and profit values are
given as shown:
Region Name
Land in acres
Profit in crores
R1
3
80
R2
2
30
R3
4
20
R4
1
40
R5
5
120
R6
4
60
R7
6
100
R8
3
60
R9
2
30
R10
2
50
Make sure the file is automatically read and no input is expected from the user.
The size of the input will increase in some of the test cases, please make sure you
have the most efficient algorithm possible
Note that the input/output data shown here is only for understanding and
testing, the actual file used for evaluation will be different.
Sample Output
The regions that to be selected is R4, R1, R10, R5, R9, R8
Total profit value: 390
Note that the input/output data shown here is only for understanding and
testing, the actual file used for evaluation will be different.
Display the output in outputPS05.txt.