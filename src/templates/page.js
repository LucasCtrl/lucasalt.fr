import React from "react"
import { graphql } from "gatsby"
import Layout from "../layouts/default"

export default ({ data }) => {
  const page = data.markdownRemark
  return (
    <Layout>
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
