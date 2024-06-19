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

pub struct Foo {
    pub _value: i32,
}

impl Foo {
    pub fn __init__(&self, value: i32) {
        self._value = value;
    }

    pub fn __add__(&self, other: Foo) -> Foo {
        return Foo {
            _value: (self._value + other._value),
        };
    }

    pub fn __str__(&self) -> &str {
        return ("*" * self._value);
    }
}
