#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int change;
    int coinCount = 0;
    int coinValue[] = {25, 10, 5, 1};

    // prompts user for a value
    do
    {
        change = get_int("Change: ");
    }
    while (change < 0);

    // counts the coins for the change
    for (int i = 0; i < 4; i++)
    {
        while (change >= coinValue[i])
        {
            change -= coinValue[i];
            coinCount++;
        }
    }

    printf("You will need at least %i coins\n", coinCount);
}
