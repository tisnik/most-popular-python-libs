canvas = document.getElementById('canvas')
context = canvas.getContext('2d')

context.font = '60pt Arial'
context.fillStyle = 'darkblue'
context.strokeStyle = 'navyblue'

context.fillText('Hello Canvas', canvas.width / 2 - 210, canvas.height / 2 + 15)
context.strokeText('Hello Canvas', canvas.width / 2 - 210, canvas.height / 2 + 15)
