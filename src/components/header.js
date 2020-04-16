import React from "react"
import { Link } from "gatsby"

export default () => (
  <div>
    <div>
      <Link to="/">Home</Link>
    </div>
    <div>
      <ul>
        <li>
          <Link to="/work/">Work</Link>
        </li>
        <li>
          <Link to="/blog/">Blog</Link>
        </li>
        <li>
          <Link to="/contact/">Contact</Link>
        </li>
      </ul>
    </div>
  </div>
)
