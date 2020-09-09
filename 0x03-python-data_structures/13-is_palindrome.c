#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: Pointer to the head.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 **/
int is_palindrome(listint_t **head)
{
	listint_t *run1, *run2;
	int i = 0, count = 0, j = 0;

	if (!*head && !head)
	{
		return (1);
	}
	run1 = *head, run2 = *head;
	while (run2)
	{
		run2 = run2->next;
		count++;
	}
	for (i = (count / 2); i >= 0; i--)
	{
		run2 = *head;
		j = count - 1;
		while (j > 0)
		{
			run2 = run2->next;
			j--;
		}
		if (run1->n != run2->n)
		{
			return (0);
		}
		run1 = run1->next;
		count--;
	}
	return (1);
}
