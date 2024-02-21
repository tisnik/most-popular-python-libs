void render_test_rgb_image(unsigned int width, unsigned int height, unsigned char *pixels, unsigned char green)
{
    unsigned int i, j;
    unsigned char *p = pixels;

    for (j=0; j<height; j++) {
        for (i=0; i<width; i++) {
            *p++=i;
            *p++=green;
            *p++=j;
            p++;
        }
    }
}

void render_test_palette_image(unsigned int width, unsigned int height, const unsigned char *palette, unsigned char *pixels)
{
    unsigned int i, j;
    unsigned char *p = pixels;

    for (j=0; j<height; j++) {
        for (i=0; i<width; i++) {
            int color = i*3;
            *p++=palette[color];
            *p++=palette[color+1];
            *p++=palette[color+2];
            p++;
        }
    }
}
