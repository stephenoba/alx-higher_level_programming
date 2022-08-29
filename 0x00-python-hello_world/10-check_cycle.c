#include "lists.h"

/**
 * check_cycle - checks if a linked list is a cycle
 * @list: Linked list
 *
 * Return: 0 if False and 1 if True
 */
int check_cycle(listint_t *list)
{
	/* listint_t **head_ptr; */
	listint_t *temp;

	if (!list)
		return (0);

	temp = list;
	/* head_ptr = &list; */
	while(temp->next)
	{
		if (temp->next == list)
			return (1);
		temp = temp->next;
	}
	return (0);
}
