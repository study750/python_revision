with open ('nyc_weather.csv','r') as f:
    next(f)
    dict={}
    for line in f:
        tokens=line.split(',')
        dict[tokens[0]]=int(tokens[1])

    avg=0
    sum=0
    count=0
    for i in dict:
        if(count==7):
            break
        sum+=dict[i]
        count+=1
    avg=float(sum/7)

    maxi=0
    for i in dict:
        maxi=max(maxi,dict[i])

    print(avg)
    print(maxi)
    print(dict['Jan 9'])