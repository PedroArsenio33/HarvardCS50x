#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // asks user for name
    string name = get_string("What's your name? ");
    // prints hello message with name
    printf("hello, %s\n", name);
}
