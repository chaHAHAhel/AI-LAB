names=["chahel","sangmi","yujin"]

search=input("search name: ")

for name in names:
    if name==search:
        print(name,"is here at index",names.index(name))
        break
else:
    print(search,"is not in the list")