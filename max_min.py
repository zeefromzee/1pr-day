power = [3,8,9,7]
mini = maxi = power[0]

    
for i in power:
    mini = min(mini, i)
    maxi = max(maxi , i)
    print(maxi,mini)
