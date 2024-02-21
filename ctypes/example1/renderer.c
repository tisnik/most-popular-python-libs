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
