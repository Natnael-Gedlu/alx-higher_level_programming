#include <stddef.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *temp;

    if (*head == NULL || (*head)->next == NULL) {
        return 1;
    }

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    if (fast != NULL) {
        slow = slow->next;
    }

    while (slow != NULL) {
        if (slow->n != prev->n) {
            return 0;
        }
        slow = slow->next;
        prev = prev->next;
    }

    return 1;
}
