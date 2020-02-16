import * as React from 'react'

import './Ticker.scss'
import logo from '../../assets/logo.png'


export default function Ticker() {
  const [ticker, setTicker] = React.useState('')

  React.useEffect(() => {
    window.addEventListener('pywebviewready', function() {
      // Expose setTicker in order to call it from Python
      window.pywebview.setTicker = setTicker
  })
  }, [])

  return (
    <div className='ticker-container'>
      <h1>Welcome to pywebview!</h1>

      <em>You can freely communicate between Javascript with Python without a HTTP server. This value, for example, is being updated by Python code:</em>
      <strong>{ ticker }</strong>
    </div>
  )
}
