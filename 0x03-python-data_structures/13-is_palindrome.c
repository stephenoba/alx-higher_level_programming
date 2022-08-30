#include "lists.h"
#include <stdio.h>

/**
 * add_to_start - add node to start of a linked list
 * @head: head of linked list
 * @n: data to be added
 *
 * Return: address of newly created node
 */
listint_t *add_nodeint_start(listint_t **head, const int n)
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
 * get_len - get length of singly linked list
 * @h: head of list
 *
 * Return: length
 */
size_t get_len(listint_t **h)
{
    size_t length = 0;
    listint_t *temp;

    temp = *h;
    while (temp)
    {
        length++;
        temp = temp->next;
    }
    return (length);
}

/**
 * split_list - splits a list int two even parts
 * @head: head of list to split
 * @head_one: first new list
 * @head_two: second new list
 * @length: length of original list
 *
 * Return: new list
 */
int split_list_even(listint_t **head, listint_t **head_one, listint_t **head_two, size_t length)
{
    listint_t *temp, *temp2, *temp3;
    size_t mid = length / 2;
    size_t c = 1;
    size_t second_half_start = length % 2 == 0 ? mid : mid + 1;

    temp = *head;
    temp2 = *head_one;
    temp3 = *head_two;
    while (c <= length)
    {
        /* don't add the middle of an odd len */
        if (length % 2 != 0 && c == mid + 1)
        {
            temp = temp->next;
            c++;
            continue;
        }
        else if (c <= second_half_start)
        {
            /* adding to the begining would reverse the list */
            temp2 = add_nodeint_start(&temp2, temp->n);
        }
        else
        {
            add_nodeint_end(&temp3, temp->n);
        }
        temp = temp->next;
        c++;
    }
    *head_one = temp2;
    *head_two = temp3;
    return (c);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of list
 *
 * Return: 0 if false or 1 if true
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *temp2, *temp3, *head1, *head2;
	int flag = 0;
	size_t len;

    head1 = NULL;
    head2 = NULL;
	if (!head)
	{
        return (0);
    }
	temp = *head;
	len = get_len(&temp);
    if (len < 2)
        return (0);
    split_list_even(&temp, &head1, &head2, len);
    temp2 = head1;
    temp3 = head2;
    while (temp2)
    {
        if (temp2->n == temp3->n)
        {
            flag = 1;
        }
        else
        {
            flag = 0;
            
        }
        temp2 = temp2->next;
        temp3 = temp3->next;
    }
    free_listint(head1);
    free_listint(head2);
    return (flag);
}
