#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from rich.console import Console, Text

paragraph = Text(
    """\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"""
)

console = Console()

console.rule("justify='left'")
console.print(paragraph, style="red")
console.print()

console.rule("justify='center'")
console.print(paragraph, style="green", justify="center")
console.print()

console.rule("justify='right'")
console.print(paragraph, style="blue", justify="right")
console.print()

console.rule("justify='full'")
console.print(paragraph, style="magenta", justify="full")
console.print()
