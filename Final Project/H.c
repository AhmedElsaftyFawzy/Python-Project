#include <cs50.h>
#include <stdio.h>

bool valid(long card);

int main(void)
{
    long card = get_long("Number: ");
    bool x = valid(card);
    if (x)
    {
        printf("valid");
    }
    else
    {
        printf("INVALID\n");
    }
}

bool valid(long card)
{
    int sum = 0;
    int count = 0;
    while(card != 0)
    {
        card = card/10;
        count ++;
    }
    for (int i = 0; i < count; i++)
    {
        int last_digit = card % 10;
        card = card / 10;
        if ((i + 1) % 2 == 0)
        {
            sum += (last_digit *2);
        }
        else
        {
            sum += last_digit;
        }
    }
    if (sum % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}
