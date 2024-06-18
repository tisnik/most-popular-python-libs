#
#  (C) Copyright 2023  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

canvas = document.getElementById("canvas")
context = canvas.getContext("2d")

context.font = "60pt Arial"
context.fillStyle = "darkblue"
context.strokeStyle = "navyblue"

context.fillText("Hello Canvas", canvas.width / 2 - 210, canvas.height / 2 + 15)
context.strokeText("Hello Canvas", canvas.width / 2 - 210, canvas.height / 2 + 15)
