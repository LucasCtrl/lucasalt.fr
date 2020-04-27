import React from "react"

import Layout from "../layouts/default"

export default ({ data }) => (
  <Layout>
    <div className="home">
      <div className="background">
        <div className="circle"></div>
        <div className="vector1"></div>
        <div className="vector2"></div>
        <div className="points"></div>
      </div>
      <div className="content">
        <h1>Hello,</h1>
        <h1>I'm Lucas Albert</h1>
        <h2>Web developer / Maker / Love to play video game</h2>
      </div>
    </div>
  </Layout>
)
