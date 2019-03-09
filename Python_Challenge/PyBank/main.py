# import os
# import csv

# meses = 0
# importe = 0
# increase = []
# importe2 = 0
# increase2 = []


# archivo = 'c:/Users/cvargas/Desktop/Python_Challenge/PyBank/budget_data.csv'

# with open(archivo, newline='') as csvfile:
#     budget_data = csv.reader(csvfile, delimiter=',')
#     header = next(budget_data)
#     #print(header)
#     for row in budget_data:
#         meses = meses + 1
#         importe = int(row[1]) + importe
#         increase.append(int(row[1]))

# for x, y in zip(increase[:], increase[1:]):
#     increase2.append(y - x)


#print(increase)
# print(meses)
# print(importe)
# print(max(increase2))
# print(min(increase2))

import csv


file = 'c:/Users/cvargas/Desktop/Python_Challenge/PyBank/budget_data.csv'
text = 'c:/Users/cvargas/Desktop/Python_Challenge/Pybank/texto.txt'


month = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
money = 0
prev_net = 0

with open(file) as budget_data:
    reader = csv.reader(budget_data)

    header = next(reader)

    for row in reader:
        month = month + 1
        money = money + int(row[1])
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

net_monthly_avg = sum(net_change_list) / len(net_change_list)


print(f"Total Months: {month}")
print(f"Total: ${money}")
print(f"Average  Change: ${net_monthly_avg:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")

# Export the results to text file
with open(text, "w") as txt_file:
    txt_file.write(f"Total Months: {month} \n" 
                    f"Total: ${money} \n"
                    f"Average  Change: ${net_monthly_avg:.2f} \n"
                    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]}) \n")