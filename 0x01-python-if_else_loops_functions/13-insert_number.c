#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node in a sorted list
 * @head: head
 * @number: data of the node
 *
 * Return: address of the inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp;

	temp = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (*head == NULL || temp->n > number)
	{
		*head = new;
		new->next = temp;
	}
	else
	{
		while (temp->next)
		{
			if (temp->next->n > number)
			{
				new->next = temp->next;
				temp->next = new;
				return (new);
			}
			temp = temp->next;
		}
		new->next = temp->next;
		temp->next = new;
	}
	return (new);
}
