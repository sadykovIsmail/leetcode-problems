/* 
Linked List Two-Pointer Quick Insights

Check for null before moving:
while (fast && fast.next) ✅

Use dummy node to handle head changes easily.

End condition matters — think when the loop should stop.

Slow & Fast moves:

fast = fast.next.next

slow = slow.next

Middle: when fast hits end, slow is middle.

Cycle: if slow === fast → cycle found.

Nth from end: move fast n ahead, then move both.

Time: O(N) — each node visited once.

Space: O(1) — only pointers used.

Visualize small examples to catch mistakes.
*/