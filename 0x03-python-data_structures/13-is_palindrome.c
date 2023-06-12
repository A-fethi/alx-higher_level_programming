#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse_list - reverses a linked list
 * @head: first node in the list's pointer
 * Return: pointer to the 1st node in the new list
 */

listint_t	*reverse_list(listint_t *head)
{
	listint_t	*prev;
	listint_t	*next;

	prev = NULL;
	next = NULL;
	while (head != NULL)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}
	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int	is_palindrome(listint_t **head)
{
	listint_t	*fast = *head;
	listint_t	*slow = *head;
	listint_t	*prev = NULL;
	listint_t	*half = NULL;
	listint_t	*after;
	listint_t	*before;

	if (!head || !(*head) || !(*head)->next)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	if (fast)
	{
		half = slow;
		slow = slow->next;
	}
	before = *head;
	after = reverse_list(slow);
	while (after)
	{
		if (before->n != after->n)
			return (0);
		before = before->next;
		after = after->next;
	}
	reverse_list(after);
	if (half)
	{
		prev->next = half;
		half->next = after;
	}
	else
		prev->next = after;
	return (1);
}
