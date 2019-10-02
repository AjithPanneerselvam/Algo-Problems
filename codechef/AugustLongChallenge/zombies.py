T = int(input())
yes = "YES"
no = "NO"

for t in range(T): 
    n = int(input())
    radiations = list(map(int, input().split()))
    health = list(map(int, input().split()))
    healthMap = dict() 
    result = [0] * n

    currentRad = 0
    for i in range(len(radiations)):
        temp = currentRad 

        extent = i + radiations[i]
        if extent < n: 
            result[extent] += 1 

        currentRad = currentRad - result[i] + 1 
        result[i] = temp 

        if health[i] in healthMap: 
            healthMap[health[i]] += 1
        else: 
            healthMap[health[i]] = 1

    currentRad = 0
    debts = [0] * n 
    matches = 0

    for i in range(len(radiations)-1, -1, -1):
        result[i] += currentRad + 1

        extent = i - radiations[i]
        if extent > 0:
            debts[extent] += 1

        currentRad = currentRad - debts[i] + 1
        if result[i] in healthMap: 
            count = healthMap[result[i]]
            if count < 1: 
                break 
            else: 
                healthMap[result[i]] -= 1
                matches += 1
        else: 
            break

    if matches == n: 
        print(yes)
    else: 
        print(no)
    

