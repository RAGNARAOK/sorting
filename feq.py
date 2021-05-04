def most_frequent(s):
    r=s
    dict={}
    for i in r:
        if i in dict:
            dict[i]+=1
        else:
              dict[i]=1
    print(sorted(dict.items(),key=lambda x :x[1],reverse = True ))
s=input("please enter the string : ")
most_frequent(s)
