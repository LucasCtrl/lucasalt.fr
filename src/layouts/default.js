import React from "react"
import { Helmet } from "react-helmet"

import Nav from "../components/nav"
import Footer from "../components/footer"

import config from "../../data/siteConfig"
import favicon from "../../static/favicon.ico"

import "../styles/main.scss"

export default ({ children }) => (
  <>
    <Helmet>
      <meta name="description" content={config.siteDescription} />
      <link rel="shortcut icon" type="image/x-icon" href={favicon} />
    </Helmet>
    <div className="main">
      <div className="container">
        <Nav />
        {children}
      </div>
      <Footer />
    </div>
  </>
)
