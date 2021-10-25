#include <stdio.h>

int main(void) {
    FILE *fout;
    int i;

    fout = fopen("binary_df_1.bin", "w");
    if (!fout) {
        return 1;
    }
    for (i=1; i<11; i++) {
        float x = 1.0/i;
        fwrite(&i, sizeof(int), 1, fout);
        fwrite(&x, sizeof(float), 1, fout);
    }
    fclose(fout);
    return 0;
}
