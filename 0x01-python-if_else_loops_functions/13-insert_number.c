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
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (0);
	new_node->n = number;
	a = *head;
	if (*head == NULL || number < a->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (a)
	{
		if (a->next == NULL)
		{
			a->next = new_node;
			new_node->next = NULL;
			return (new_node);
		}
		else if (number >= a->n && number <= a->next->n)
		{
			new_node->next = a->next;
			a->next = new_node;
			return (new_node);
		}
		a = a->next;
	}
	return (NULL);
}
