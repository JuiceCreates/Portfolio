// Corey Williams
// COP2220
// 02/22/2023
// List applicants in Application Order, and Alphabetical Order

#include <stdio.h>
#define STRSIZ 30
#define MAXAPP 50

int alpha_first(char *list[], int min_sub, int max_sub);
void select_sort_str(char *list[], int n);

int main(void)
{
    char applicants[MAXAPP][STRSIZ];
    char *alpha[MAXAPP];
    int num_app, i;
    char one_char;

    printf("Enter number of applicants (0 . . %d)\n> ", MAXAPP);
    scanf("%d", &num_app);
    do
        scanf("%c", &one_char);
    while (one_char != '\n');

    printf("Enter names of applicants on separate lines of less than\n");
    printf(" 30 characters in the order in which they applied\n");
    for (i = 0; i < num_app; ++i)
        gets(applicants[i]);

    for (i = 0; i < num_app; ++i)
        alpha[i] = applicants[i];
    select_sort_str(alpha, num_app);

    printf("\n\n%-30s%5c%-20s\n\n", "Application Order", ' ', "Alphabetical Order");
        for(i = 0; i < num_app; ++i)
            printf("%-30s%5c%-30s\n", applicants[i], ' ', alpha[i]);

    return(0);

}

int alpha_first(char *list[], int min_sub, int max_sub)
{
    int first, i;

    first = min_sub;
    for (i = min_sub + 1; i <= max_sub; ++i)
        if (strcmp(list[i], list[first]) < 0)
            first = i;

    return(first);
}

void select_sort_str(char *list[], int n)
{
    int fill, index_of_min;
    char *temp;

    for (fill = 0; fill < n - 1; ++fill) {
        index_of_min = alpha_first(list, fill, n - 1);

        if (index_of_min != fill) {
            temp = list[index_of_min];
            list[index_of_min] = list[fill];
            list[fill] = temp;
        }
    }
}