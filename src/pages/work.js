import React from "react"
import { Link, graphql } from "gatsby"
import Layout from "../layouts/default"

export default ({ data }) => (
  <Layout>
    <div className="page">
      <div className="page-header">
        <h1 className="page-title">Work</h1>
      </div>
      <div className="works">
        {data.allMarkdownRemark.edges.map(({ node }) => (
          <div key={node.id} className="work-card">
            <Link to={node.fields.slug}>
              <div className="work-header">
                <img
                  src={node.frontmatter.hero.childImageSharp.fixed.src}
                  alt={node.frontmatter.title + " hero"}
                />
              </div>
              <div className="work-content">
                <h3>{node.frontmatter.category}</h3>
                <h2>{node.frontmatter.title}</h2>
                <p className="work-excerpt">{node.excerpt}</p>
                <p className="work-details">Details →</p>
              </div>
            </Link>
          </div>
        ))}
      </div>
    </div>
  </Layout>
)

export const query = graphql`
  query {
    allMarkdownRemark(
      sort: { fields: [frontmatter___date], order: DESC }
      filter: { frontmatter: { template: { eq: "work" } } }
    ) {
      edges {
        node {
          id
          frontmatter {
            title
            category
            hero {
              childImageSharp {
                fixed(width: 1280) {
                  src
                }
              }
            }
          }
          excerpt
          fields {
            slug
          }
        }
      }
    }
  }
`
