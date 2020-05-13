import React, { Component } from "react"
import { graphql } from "gatsby"

import Layout from "../layouts/default"
import SEO from "../components/SEO"

export default class Page extends Component {
  render() {
    const { slug } = this.props.pageContext
    const page = this.props.data.markdownRemark

    return (
      <Layout>
        <SEO meta={page} urlPath={slug} seoType="page" />
        <div className="page">
          <div className="page-header">
            <h1 className="page-title">{page.frontmatter.title}</h1>
          </div>
          <div
            className="page-content"
            dangerouslySetInnerHTML={{ __html: page.html }}
          />
        </div>
      </Layout>
    )
  }
}

export const pageQuery = graphql`
  query($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      frontmatter {
        title
      }
      html
    }
  }
`
