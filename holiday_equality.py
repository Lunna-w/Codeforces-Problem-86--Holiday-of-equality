n = int(input())

w = list(map(int, input().split()))
max_num = max(w)



total_wealth_difference = 0
for i in w:
    wealth_difference = max_num - i
    total_wealth_difference += wealth_difference

print(total_wealth_difference)