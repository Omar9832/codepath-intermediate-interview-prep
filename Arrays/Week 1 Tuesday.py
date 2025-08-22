
sum=0
def sum_honey(hunny_jars):
    global sum
    for x in hunny_jars:
        sum=sum+x
    return sum

print(sum_honey([2, 3, 4, 5]))



def print_todo_list(task):
    print("Pooh's To Dos:")
    count=0
    while count<len(task):
        print(count+1, ".", task[count], "\n")
        count=count+1
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

