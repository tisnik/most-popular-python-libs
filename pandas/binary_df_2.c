#include <stdio.h>

char* names[] = {
    "odd ",
    "even"
};

int main(void) {
    FILE *fout;
    int i;

    fout = fopen("binary_df_2.bin", "w");
    if (!fout) {
        return 1;
    }
    for (i=1; i<11; i++) {
        float x = 1.0/i;
        fwrite(&i, sizeof(int), 1, fout);
        fwrite(&x, sizeof(float), 1, fout);
        fwrite(names[i%2], 4, 1, fout);
    }
    fclose(fout);
    return 0;
}
