#big o notation (time/ space complexity)
#how we measure and compare efficiency of algorithms
#Common Big o values:
#0(1) constant space/ time
#0(n) linear space/ time
#0(log n) logarithmic space/ time (merge and conquer)
#0(n^2) quadratic space/ time (nested loops)

#o(n) time example
list = [1, 2, 3]
for number in list:
    print(number)

#o(n^2) time example
nested_list = [[4, 5, 6], [7, 8, 9]]

for list in nested_list:
    for number in list:
        print(number)
