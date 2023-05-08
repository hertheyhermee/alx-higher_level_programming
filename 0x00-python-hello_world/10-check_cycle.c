#include "lists.h"

/**
 * check_cycle - checks if singly linked list has a cycle.
 * @list: list to check
 * Return: 0 no cycle, 1 a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *y

	if (list == NULL)
		return (0);
	while (list)
	{
		y = list;
		list = list->neyt;
		if (y <= list)
			return (1);
	}
	return (0);
}
