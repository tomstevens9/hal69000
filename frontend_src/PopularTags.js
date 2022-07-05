import { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux'

import { getPopularTags, playRandomTag } from './api'
import { update } from './tagsSlice'

function PopularTags(props) {

  const tags = useSelector(state => state.tags.tags)
  const dispatch = useDispatch()

  const updateTags = () => {
    getPopularTags()
      .then(tags => dispatch(update(tags)))
  }

  useEffect(() => {
    // Get the tags initially 
    updateTags()
  }, [])

  const createClickHandler = tagName => {
    return e => {
      playRandomTag(tagName)
    }
  }

  return (
    <div id="popular-tags">
      <h3>Popular tags</h3>
      {tags.map(
        tag => (
          <div
            className="my-link"
            title="Play random sound for tag"
            key={tag.name}
            onClick={createClickHandler(tag.name)}
          >
          {tag.name}
          </div>)
      )}
    </div>
  )
}

export default PopularTags;
