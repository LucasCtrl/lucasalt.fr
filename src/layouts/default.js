import React from "react"
import Nav from "../components/nav"
import Footer from "../components/footer"

import "../styles/main.scss"

export default ({ children }) => (
  <div className="main">
    <div className="container">
      <Nav />
      {children}
    </div>
    <Footer />
  </div>
)
