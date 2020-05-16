import React, { Component } from "react"
import { Link } from "gatsby"

import * as eva from "eva-icons"

import logo from "../images/logo.svg"

export default class NavBar extends Component {
  componentDidMount() {
    eva.replace()
  }

  render() {
    return (
      <div className="nav">
        <div className=" brand">
          <Link to="/">
            <img src={logo} alt="Logo" />
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
            <li>
              <a
                href="https://github.com/LucasCtrl"
                target="_blank"
                rel="noreferrer noopener"
              >
                <i data-eva="github" />
              </a>
            </li>
          </ul>
        </div>
      </div>
    )
  }
}
