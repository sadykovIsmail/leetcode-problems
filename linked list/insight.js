/* 
1) Linked List Two-Pointer Quick Insights

2) Check for null before moving:
while (fast && fast.next) ✅

3)Use dummy node to handle head changes easily.

4)End condition matters — think when the loop should stop.

5)Slow & Fast moves:
fast = fast.next.next
slow = slow.next

6)Middle: when fast hits end, slow is middle.

7)Cycle: if slow === fast → cycle found.

8)Nth from end: move fast n ahead, then move both.

9)Time: O(N) — each node visited once.

10)Space: O(1) — only pointers used.

11)Visualize small examples to catch mistakes.


*/