import React from "react"
import { Link, graphql } from "gatsby"
import Layout from "../layouts/default"

export default ({ data }) => {
  console.log(data)
  return (
    <Layout>
      <div className="blogPage">
        <h1 className="page-title">Blog</h1>
        {data.allMarkdownRemark.edges.map(({ node }) => (
          <div key={node.id} className="post-card">
            <Link to={node.fields.slug}>
              <div className="post-content">
                <div className="post-thumbnail">
                  <img
                    src={node.frontmatter.thumbnail.publicURL}
                    alt={node.frontmatter.title + " image"}
                  />
                </div>
                <div className="post-title">
                  <h3>{node.frontmatter.category}</h3>
                  <h2>{node.frontmatter.title}</h2>
                </div>
                <div>{/* Empty box for the grid */}</div>
                <div className="post-excerpt">
                  <p>{node.excerpt}</p>
                  <p className="read">Read more →</p>
                </div>
              </div>
            </Link>
          </div>
        ))}
      </div>
    </Layout>
  )
}

export const query = graphql`
  query {
    allMarkdownRemark(sort: { fields: [frontmatter___date], order: DESC }) {
      edges {
        node {
          id
          frontmatter {
            title
            thumbnail {
              publicURL
            }
            category
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
