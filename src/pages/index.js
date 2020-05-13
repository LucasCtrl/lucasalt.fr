import React, { Component } from "react"

import Layout from "../layouts/default"
import SEO from "../components/SEO"

export default class Index extends Component {
  render() {
    const meta = {
      frontmatter: {
        title: "Home",
      },
    }

    return (
      <Layout>
        <SEO meta={meta} urlPath={this.props.path} seoType="page" />

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
  }
}
