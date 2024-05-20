static int __pyx_f_17mandelbrot_cython_calc_mandelbrot(int __pyx_v_width, int __pyx_v_height, int __pyx_v_maxiter, unsigned char *__pyx_v_palette) {
  double __pyx_v_zx;
  double __pyx_v_zy;
  double __pyx_v_zx2;
  double __pyx_v_zy2;
  double __pyx_v_cx;
  double __pyx_v_cy;
  unsigned char __pyx_v_r;
  unsigned char __pyx_v_g;
  unsigned char __pyx_v_b;
  int __pyx_v_i;
  int __pyx_v_index;
  CYTHON_UNUSED long __pyx_v_y;
  CYTHON_UNUSED long __pyx_v_x;
  int __pyx_r;
  int __pyx_t_1;
  int __pyx_t_2;
  long __pyx_t_3;
  int __pyx_t_4;
  int __pyx_t_5;
  long __pyx_t_6;
  int __pyx_t_7;

  (void)(printf(((char const *)"P3\n%d %d\n255\n"), __pyx_v_width, __pyx_v_height));

  __pyx_v_cy = -1.5;
  __pyx_t_1 = __pyx_v_height;
  __pyx_t_2 = __pyx_t_1;
  for (__pyx_t_3 = 0; __pyx_t_3 < __pyx_t_2; __pyx_t_3+=1) {
    __pyx_v_y = __pyx_t_3;
    __pyx_v_cx = -2.0;
    __pyx_t_4 = __pyx_v_width;
    __pyx_t_5 = __pyx_t_4;
    for (__pyx_t_6 = 0; __pyx_t_6 < __pyx_t_5; __pyx_t_6+=1) {
      __pyx_v_x = __pyx_t_6;
      __pyx_v_zx = 0.0;
      __pyx_v_zy = 0.0;
      __pyx_v_i = 0;
      while (1) {
        __pyx_t_7 = (__pyx_v_i < __pyx_v_maxiter);
        if (!__pyx_t_7) break;
        __pyx_v_zx2 = (__pyx_v_zx * __pyx_v_zx);
        __pyx_v_zy2 = (__pyx_v_zy * __pyx_v_zy);
        __pyx_t_7 = ((__pyx_v_zx2 + __pyx_v_zy2) > 4.0);
        if (__pyx_t_7) {
          goto __pyx_L8_break;
        }
        __pyx_v_zy = (((2.0 * __pyx_v_zx) * __pyx_v_zy) + __pyx_v_cy);
        __pyx_v_zx = ((__pyx_v_zx2 - __pyx_v_zy2) + __pyx_v_cx);
        __pyx_v_i = (__pyx_v_i + 1);
      }
      __pyx_L8_break:;
      __pyx_v_index = (__pyx_v_i * 3);
      __pyx_v_r = (__pyx_v_palette[__pyx_v_index]);
      __pyx_v_g = (__pyx_v_palette[(__pyx_v_index + 1)]);
      __pyx_v_b = (__pyx_v_palette[(__pyx_v_index + 2)]);
      (void)(printf(((char const *)"%d %d %d\n"), __pyx_v_r, __pyx_v_g, __pyx_v_b));
      __pyx_v_cx = (__pyx_v_cx + (3.0 / ((double)__pyx_v_width)));
    }
    __pyx_v_cy = (__pyx_v_cy + (3.0 / ((double)__pyx_v_height)));
  }
  __pyx_r = 0;
  return __pyx_r;
}
