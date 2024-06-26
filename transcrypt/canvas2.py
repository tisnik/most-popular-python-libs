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

context.fillStyle = "darkblue"
context.beginPath()
context.moveTo(75, 50)
context.lineTo(100, 75)
context.lineTo(100, 25)
context.fill()

context.fillStyle = "darkred"
context.beginPath()
context.moveTo(225, 50)
context.lineTo(200, 75)
context.lineTo(200, 25)
context.fill()

context.strokeStyle = "darkgreen"
context.lineWidth = 10
context.beginPath()
context.moveTo(75, 125)
context.quadraticCurveTo(25, 125, 25, 162.5)
context.quadraticCurveTo(25, 200, 50, 200)
context.quadraticCurveTo(50, 220, 30, 225)
context.quadraticCurveTo(60, 220, 65, 200)
context.quadraticCurveTo(125, 200, 125, 162.5)
context.quadraticCurveTo(125, 125, 75, 125)
context.stroke()
