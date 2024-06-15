//! ```cargo
//! [package]
//! edition = "2018"
//! [dependencies]
//!
//! ```

#![allow(clippy::collapsible_else_if)]
#![allow(clippy::double_parens)] // https://github.com/adsharma/py2many/issues/17
#![allow(clippy::map_identity)]
#![allow(clippy::needless_return)]
#![allow(clippy::print_literal)]
#![allow(clippy::ptr_arg)]
#![allow(clippy::redundant_static_lifetimes)] // https://github.com/adsharma/py2many/issues/266
#![allow(clippy::unnecessary_cast)]
#![allow(clippy::upper_case_acronyms)]
#![allow(clippy::useless_vec)]
#![allow(non_camel_case_types)]
#![allow(non_snake_case)]
#![allow(non_upper_case_globals)]
#![allow(unused_imports)]
#![allow(unused_mut)]
#![allow(unused_parens)]

pub fn bubble_sort<T0>(size: T0) {
    let mut a = (0..size)
        .map(|i| random.randrange(0, 10000))
        .collect::<Vec<_>>();
    for i in (((size as i32) - 1)..0).step_by(-1) {
        for j in (0..i) {
            if a[j] > a[((j as i32) + 1)] {
                ({
                    let (__tmp1, __tmp2) = (a[((j as i32) + 1)], a[j]);
                    a[j] = __tmp1;
                    a[((j as i32) + 1)] = __tmp2;
                });
            }
        }
    }
    println!("{}", a);
}
