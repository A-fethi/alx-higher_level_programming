#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int	is_palindrome(listint_t **head)
{
	listint_t	*fast = *head;
	listint_t	*slow = *head;
	listint_t	*next = NULL;
	listint_t	*prev = NULL;
	listint_t	*after;
	listint_t	*before;

	if (fast && fast->next)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	if (fast)
	{
		slow = slow->next;
	}
	while (slow)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	before = *head;
	after = prev;
	while (after)
	{
		if (before->n != after->n)
			return (0);
		before = before->next;
		after = after->next;
	}
	return (1);
}
