import React from "react"
import { graphql } from "gatsby"
import Layout from "../layouts/default"

export default ({ data }) => {
  const post = data.markdownRemark
  const frontmatter = post.frontmatter
  return (
    <Layout>
      <div className="page">
        <div className="page-header">
          <p className="page-subtitle">{frontmatter.category}</p>
          <h1 className="page-title">{frontmatter.title}</h1>
        </div>
        <div className="page-decoration">
          <div className="page-hero">
            <img
              src={frontmatter.hero.childImageSharp.fixed.src}
              alt={frontmatter.title + " hero"}
            />
          </div>
        </div>
        <div
          className="page-content"
          dangerouslySetInnerHTML={{ __html: post.html }}
        />
      </div>
    </Layout>
  )
}

export const pageQuery = graphql`
  query($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      frontmatter {
        category
        title
        hero {
          childImageSharp {
            fixed(width: 1280) {
              src
            }
          }
        }
      }
      html
    }
  }
`
