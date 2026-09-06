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
        ListNode* temp = head;
        int len = 0;
        while(temp){
            temp = temp->next;
            len++;
        }
        temp = head;
        int k = len - n;
        if(k==0){
            head = head->next;
            return head;
        }
        for(int i = 1; i<k; i++){
            temp = temp->next;
        }
        temp->next = temp->next->next;
        return head;
    }
};
