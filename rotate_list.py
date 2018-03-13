# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

	def size(head):
		length =1
		while(head.next!=None):
			head = head.next
			length = length +1
	return length

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l = size(head)
        print l


