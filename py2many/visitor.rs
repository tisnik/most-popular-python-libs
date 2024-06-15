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

pub struct Visitor {
    pub nest_level: i32,
}

impl Visitor {
    pub fn __init__(&self) {
        self.nest_level = 0;
    }

    pub fn on_visit<T0>(&self, text: T0) {
        pub const indent: &str = ((" " * self.nest_level) * 2);
        println!("{} {}", indent, text);
        self.nest_level += 1;
    }

    pub fn on_leave<T0>(&self, node: T0) {
        self.nest_level -= 1;
    }
}
