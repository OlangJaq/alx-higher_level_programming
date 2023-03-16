/**
 * struct dlistint_s - doubly linked list
 * @n: integer
 * @prev: points to the previous node
 * @next: points to the next node
 *
 * Description: doubly linked list node structure
 * 
 */

size_t print_dlistint(const dlistint_t *h)
{
    const dlistint_t *current = h;
    size_t count = 0;
    while (current != NULL)
    {
        printf("%d\n", current->n);
        current = current->next;
        count++;
    }
    return count;
}
