#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>

/**
 * insert_node - inserts a number into a singly linked list
 * @head: head pointer
 * @number: number to store new node
 * Return: address of new node, NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *a;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (0);
	new->n = number;
	a = *head;
	if (*head == NULL || number < a->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (a)
	{
		if (a->next == NULL)
		{
			a->next = new;
			new->next = NULL;
			return (new);
		}
		else if (number >= a->n && number <= a->next->n)
		{
			new->next = a->next;
			a->next = new;
			return (new);
		}
		a = a->next;
	}
	return (NULL);
}
