import * as React from 'react'

import './Editor.scss'


export default function Header() {
  const [content, saveContent] =
    React.useState('Using Python as backenlowed in Javascript, for example disk access. Click button below to save this content to hard drive.')

  return (
    <div className='editor-container'>
      Gulshans
      <textarea className='textarea' value={content} onChange={(e) => {
        saveContent(e.target.value)
      }}/><br/>

      <button className='button' onClick={() => {
        window.pywebview.api.save_content(content)
      }}>Save</button>
    </div>
  )
}
