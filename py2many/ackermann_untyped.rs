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

pub fn A<T0, T1>(m: T0, n: T1) -> i32 {
    if (m as i32) == 0 {
        return ((n as i32) + 1);
    }
    if (n as i32) == 0 {
        return A(((m as i32) - 1), 1);
    }
    return A(((m as i32) - 1), A(m, ((n as i32) - 1)));
}

pub fn check_a() {
    for m in (0..4) {
        for n in (0..5) {
            println!("{} {} {}", m, n, A(m, n));
        }
    }
}
