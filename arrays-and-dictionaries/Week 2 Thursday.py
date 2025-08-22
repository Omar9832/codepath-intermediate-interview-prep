def is_symmetrical_title(title):
    left_pointer=0
    title.lower().strip()
    i=0
    title=title.replace(" ", "")
    title=title.lower()
    
    print(title)
    right_pointer=len(title)-1
    while left_pointer<right_pointer:
        if title[left_pointer]!=title[right_pointer]:
            return False
        print(left_pointer)
        print(right_pointer)
        left_pointer=left_pointer+1
        right_pointer=right_pointer-1
    return True
        #if title[left_pointer]==" " and title[right_pointer]==" ":
            #left_pointer=left_pointer+1
            #right_pointer=right_pointer-1
        #elif title[left_pointer]==" ":
            #left_pointer=left_pointer+1
        
        


print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 




def post_compare(draft1, draft2):
   pass




print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 