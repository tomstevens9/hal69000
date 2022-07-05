import axios from 'axios';

import { getCookie } from './util'

const uploadSound = (commandName, commandFile) => {
  let formData = new FormData()
  formData.append("command", commandName)
  formData.append("file", commandFile)
  return axios({
    method: 'post',
    url: 'upload-sound/',
    data: formData,
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
      'Authorization': `Token ${getCookie('logintoken')}`,
      'Content-Type': 'multipart/form-data'
    }
  })
    .then(response => {
      console.log(response)
    })
    .catch(err => {
      console.log('Failed to upload sound')
      console.log(err)
    })
}

const getSounds = () => {
  return axios({
    method: 'get',
    url: 'sounds/',
    headers: {
      'Authorization': `Token ${getCookie('logintoken')}`
    }
  })
    .then(response => {
      return response.data.reverse()
    })
    .catch(err => {
      console.log('Failed to get sounds')
      return []

    })
}

const getPopularTags = () => {
  return axios({
    method: 'get',
    url: 'popular-tags/',
    headers: {
      'Authorization': `Token ${getCookie('logintoken')}`
    }
  })
    .then(response => {
      return response.data
    })
    .catch(err => {
      console.log('Failed to get tags')
      return []
    })
}

const sendCommand = commandName => {
  return axios({
    method: 'post',
    url: 'send-command/',
    data: `command=${commandName}`,
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
      'Authorization': `Token ${getCookie('logintoken')}`,
    }
  })
    .then(response => {
      console.log(response)
    })
    .catch(err => {
      console.log('Failed to send sound')
      console.log(err)
    })
}

const playRandomTag = tagName => {
  return axios({
    method: 'post',
    url: 'play-random-sound/',
    data: `tag_name=${tagName}`,
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
      'Authorization': `Token ${getCookie('logintoken')}`,
    }
  })
    .then(response => {
      console.log(response)
    })
    .catch(err => {
      console.log('Failed to send sound')
      console.log(err)
    })
}

export { uploadSound, getSounds, getPopularTags, sendCommand, playRandomTag };
