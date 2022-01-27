const playSound = filepath => {
  const audio = new Audio(filepath)
  audio.play()
}

const sendCommand = commandName => {
  const request = new XMLHttpRequest()
  request.open('POST', '/send-command/', true)
  request.setRequestHeader('X-CSRFToken', csrftoken);
  request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded')
  request.send(`command=${commandName}`)
}
