a = [1,2,3,4,5,6,7,8,9,10]
def add ():
    print(sum(a))
add()
def mul():
    multi = 1
    for i in a:
            multi = multi * i
    print(multi)
mul()
def largest():
    print(max(a))
largest()
def lowest():
    print(min(a))
lowest()

def match_count(words):
     count = 0
     for word in words:
         if len(word)>1 and word[0] == word[-1]:
             count += 1
     return count
print(match_count(['abc','xyz','aba','1221']))
b=[1,1,2,2,3,3,4,5,5,6,7,7,8,9,9]
def rem_dup():
    print(list(set(b)))

rem_dup()
z = []
def check_empty():
    if len(z)>0:
        print("not empty")
    else:
        print("empty")
check_empty()

def clone():
    f = a.copy()
    print(f)
clone()

def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))
