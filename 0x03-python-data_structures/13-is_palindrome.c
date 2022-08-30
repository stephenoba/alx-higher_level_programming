#include "lists.h"
#include <stdio.h>

/**
 * add_to_start - add node to start of a linked list
 * @head: head of linked list
 * @n: data to be added
 *
 * Return: address of newly created node
 */
listint_t *add_to_start(listint_t **head, int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

/**
 * reverse_list - reverses a singly linked list to a mid point
 * @head: head of list to reverse
 * @mid: mid point of list
 *
 * Return: new list
 */
listint_t *reverse_list(listint_t *head, size_t mid)
{
	listint_t *new_head;
	size_t i = 1;

	new_head = NULL;
	while (i <= mid)
    {
		new_head = add_to_start(&new_head, head->n);
        head = head->next;
		if (new_head == NULL)
			return (0);
		i++;
	}
	return (new_head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of list
 *
 * Return: 0 if false or 1 if true
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *temp2, *head2;
	int flag = 0;
	size_t len, mid, start;

	if (!head)
	{
		return (0);
	}
	temp = *head;
    if (temp->next == NULL)
    {
        return (0);
    }
	len = 1;
	while (temp->next)
	{
		len++;
		temp = temp->next;
	}
    mid = len / 2;
    temp = *head;
    head2 = reverse_list(temp, mid);
    for (start = 1; start < mid; start++)
    {
        temp = temp->next;
    }
    if (len % 2 == 0 && temp->n == temp->next->n)
        return (1);
    temp2 = head2;
    temp = temp->next->next;
    while (temp2)
    {
        if (temp2->n == temp->n)
            flag = 1;
        else
        {
            flag = 0;
            break;
        }
        temp2 = temp->next;
        temp = temp->next;
    }
    free_listint(head2);
    return flag;
}
