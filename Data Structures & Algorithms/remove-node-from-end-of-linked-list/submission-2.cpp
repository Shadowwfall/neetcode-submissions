/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(!head) return nullptr;
        if(!head->next && n == 1) return nullptr;
        ListNode* dummy = new ListNode();
        dummy->next = head;
        ListNode* temp = head;
        for(int i=0; i<n; i++){
            temp = temp->next;
        }
        while(temp){
            temp=temp->next;
            dummy = dummy->next;
        }
        if(dummy->next == head){
            return head->next;
        }
        dummy->next = dummy->next->next;
        return head;
    }
};
