#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // prompts user for a size
    int size;
    do
    {
        size = get_int("Size: ");
    }
    while (size < 1);

    // builds structure based on size
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            if (size - j - 1 > i)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("\n");
    }
}
