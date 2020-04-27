import React from "react"
import { Link } from "gatsby"
import logo from "../images/logo.svg"

export default () => (
  <div className="nav">
    <div className=" brand">
      <Link to="/">
        <img src={logo} alt="Logo"/>
      </Link>
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
