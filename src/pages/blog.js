import React from "react"
import { Link, graphql } from "gatsby"
import Layout from "../layouts/default"

export default ({ data }) => {
  console.log(data)
  return (
    <Layout>
      <div>
        {data.allMarkdownRemark.edges.map(({ node }) => (
          <div key={node.id}>
            <Link to={node.fields.slug}>
              <h2>{node.frontmatter.title}</h2>
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
            date
            title
          }
          fields {
            slug
          }
        }
      }
    }
  }
`
