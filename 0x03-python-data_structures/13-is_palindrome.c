#include "lists.h"

/**
 * add_to_start - add node to start of a linked list
 * @head: head of linked list
 * @n: data to be added
 *
 * Return: address of newly created node
 */
listint_t *add_to_start(listint_t **head, int n)
{
	listint_t *temp, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return new;
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
	size_t i = 0;

	new_head = NULL;
	while (i != mid)
	{
		head = head->next;
		new_head = add_to_start(&new_head, head->n);
		if (new_head == NULL)
			exit(-1);
		i++;
	}
	return new_head;
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
	int flag;
	size_t len, mid;

	if (!head)
	{
		return (0);
	}
	temp = *head;
	len = 0;
	while (temp->next)
	{
		len++;
		temp = temp->next;
	}
	/* get mid point */
	mid = len / 2;
	head2 = reverse_list(*head, mid);
	temp2 = head2;
	while (temp2->next)
	{
		if (temp2->n == temp->n)
		{
			flag = 1;
		}
		else
		{
			flag = 0;
			break;
		}
		temp2 = temp2->next;
	}
}
