friends=["kala","dhola","kauwa","pota"]
num=[2,4,5,6,2,13,5,4,5]

friends.extend(num)
print(friends)

friends=["kala","dhola","kauwa","pota"]
num=[2,4,5,6,2,13,5,4,5]

friends.append("lili")
print(friends)

kala=friends.pop()
print(friends)
print("poped one is "+kala)

friends.insert(2,"chocho dodo")
print(friends)

friends.sort()
print(friends)

num.sort()
print(num)

num.reverse()
print(num)

num.remove(2)
print(num)

friends=["kala","dhola","kauwa","pota"]
num=[2,4,5,6,2,13,5,4,5]

print(friends.index("kala"))

print(friends.index("dhola"))

print(num.count(2))
