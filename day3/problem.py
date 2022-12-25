with open('input.txt', 'r') as f:
    lines = f.readlines()
    diagnostics = [entry.strip() for entry in lines]

gamma = ""
epsilon = ""


for i in range(len(diagnostics[0])):
    stringOfPosi = []
    for j in range(len(diagnostics)):
        stringOfPosi.append(diagnostics[j][i])
    if(stringOfPosi.count('0') > stringOfPosi.count('1')):
        gamma += '0'
        epsilon += '1'
    else:
        epsilon += '0'
        gamma += '1'
    

print(int(epsilon, 2) * int(gamma, 2))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

oxygen = co2 = diagnostics
for i in range(len(oxygen[0])):
    while len(oxygen) != 1:
        if(oxygen.count('1') > oxygen.count('0') | oxygen.count('1') == oxygen.count('0')):
            for item in oxygen:
                if item[i] == '0':
                    oxygen.remove(item)
        else:
            for item in oxygen:
                if item[i] == '1':
                    oxygen.remove(item)
        if(oxygen.count('1') > oxygen.count('0') | oxygen.count('1') == oxygen.count('0')):
            for item in oxygen:
                if item[i] == '0':
                    oxygen.remove(item)
        else:
            for item in oxygen:
                if item[i] == '1':
                    oxygen.remove(item)

print(int(co2[0], 2) * int(oxygen[0], 2))