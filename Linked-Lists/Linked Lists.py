
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        current1=headA
        current2=headB
        while current1 and current2:
            if current1.val==current2.val:
                return current1.val
            current1=current1.next
            current2=current2.next
        return None
    
        #iterate through each Node for both linked lists
        #By using .val I would chekc if the value in the first linke list is eqaul to the one in the second
        #return value of the node
        #return False