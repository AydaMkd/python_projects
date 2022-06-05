from ntpath import join


def hello():
    print("greetings!")
hello()

def pack(a,b,c):
    return[a,b,c]
# x=pack("cat","kitty","kittyCat")
pack("kitty","cat","kittyCat")
print(pack("kitty","cat","kittyCat"))

def eat_lunch(list):
    if len(list)==0:
        print("My lunchbox is empty!")
    else:
        print("I first eat "+list[0])
        list1=list[1:(len(list)+1)]
    for i in range(len(list1)):
        print("Next I eat "+ list1[i])
       
eat_lunch(["oats", "salad", "soup"])