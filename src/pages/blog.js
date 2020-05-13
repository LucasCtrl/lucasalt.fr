import React, { Component } from "react"
import { Link, graphql } from "gatsby"

import Layout from "../layouts/default"
import SEO from "../components/SEO"

export default class BlogPosts extends Component {
  render() {
    const meta = {
      frontmatter: {
        title: "Blog",
      },
    }

    return (
      <Layout>
        <SEO meta={meta} urlPath={this.props.path} seoType="page" />

        <div className="page">
          <div className="page-header">
            <h1 className="page-title">Blog</h1>
          </div>
          <div className="posts">
            {this.props.data.allMarkdownRemark.edges.map(({ node }) => (
              <div key={node.id} className="post-card">
                <Link to={node.fields.slug}>
                  <div className="post-header">
                    <div className="post-thumbnail">
                      <img
                        src={
                          node.frontmatter.thumbnail.childImageSharp.fixed.src
                        }
                        alt={node.frontmatter.title + " image"}
                      />
                    </div>
                    <div className="post-title">
                      <h3>{node.frontmatter.category}</h3>
                      <h2>{node.frontmatter.title}</h2>
                    </div>
                  </div>
                  <div className="post-content">
                    <div className="post-excerpt">
                      <p>{node.excerpt}</p>
                      <p className="post-read-more">Read more →</p>
                    </div>
                  </div>
                </Link>
              </div>
            ))}
          </div>
        </div>
      </Layout>
    )
  }
}

export const query = graphql`
  query {
    allMarkdownRemark(
      sort: { fields: [frontmatter___date], order: DESC }
      filter: { frontmatter: { template: { eq: "post" } } }
    ) {
      edges {
        node {
          id
          frontmatter {
            title
            thumbnail {
              childImageSharp {
                fixed(height: 150, width: 150) {
                  src
                }
              }
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
