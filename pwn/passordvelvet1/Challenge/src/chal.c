#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_flag(void)
{
    FILE *fp;
    char c;
    fp = fopen("./flag.txt", "r");
    if(fp == NULL)
    {
        printf("Kunne ikke finne flagget. Kontakt CTF adm!\n");
        exit(1);
    }
    while(1)
    {
        c = fgetc(fp);
        if(c == EOF) break;
        printf("%c", c);
    }
    fclose(fp);
    exit(0);
}

void main(void)
{
    volatile int *lesflag = (volatile int *)0x1337; // Hack for at gcc skal oppføre seg :(
    volatile char passord[32] = "";
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    printf("Du har 3 forsøk på å låse opp flagget! :)\n");
    for(int i=0; i<3; i++)
    {
        printf("Forsøk %d av 3\n", i);
        printf("Skriv passordet: ");
        gets(passord);
        if(lesflag == 0x646167656e)
        {
            int result = strncmp(passord, "sikkerhets", 10);
            if(result == 0)
            {
                print_flag();
            }
            else
            {
                printf("Beklager, feil passord :(\n");
            }
        }
        else
        {
            printf("Beklager, sikkerhetslåsen %p er ikke riktig satt :(\n", lesflag);
        }
    }
    printf("Brukt alle forsøk, prøv igjen senere...");
}

