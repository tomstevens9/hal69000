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

const playRandomSound = tagName => {
  const request = new XMLHttpRequest()
  request.open('POST', '/play-random-sound/', true)
  request.setRequestHeader('X-CSRFToken', csrftoken);
  request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded')
  request.send(`tag_name=${tagName}`)
}

const disco = () => {
  document.body.classList.add('disco');
  const headerElement = document.getElementById('image-header');
  headerElement.classList.add('header-disco');
}
