#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: head pointer of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int	check_cycle(listint_t *list)
{
	listint_t	*once;
	listint_t	*twice;

	once = list;
	twice = list;
	while (twice && twice->next)
	{
		once = once->next;
		twice = twice->next->next;
		if (once == twice)
			return (1);
	}
	return (0);
}
