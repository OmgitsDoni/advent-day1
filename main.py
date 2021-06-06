result_of_sum = 2020

f = open('day1_input.txt', 'r')
first_list = [int(line) for line in f.readlines()]

for i in range(len(first_list)):
        for j in range(i + 1, len(first_list)):
            if (first_list[i] + first_list[j] == result_of_sum):
                print('The numbers:', first_list[i], ',', first_list[j],'. The result is:', (first_list[i] * first_list[j]))

f.close()
