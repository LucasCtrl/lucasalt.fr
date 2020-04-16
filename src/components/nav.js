import React from "react"
import { Link } from "gatsby"

export default () => (
  <div className="nav">
    <div className=" brand">
      <Link to="/">Logo</Link>
    </div>
    <div className="links">
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
