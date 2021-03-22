import React, { Component } from "react"
import { Link, graphql } from "gatsby"

import Layout from "../layouts/default"
import SEO from "../components/SEO"

export default class WorksList extends Component {
  render() {
    const meta = {
      frontmatter: {
        title: "Work",
      },
    }

    return (
      <Layout>
        <SEO meta={meta} urlPath={this.props.path} seoType="page" />
        <div className="page">
          <div className="page-header">
            <h1 className="page-title">Work</h1>
          </div>
          {/* <div className="works">
            {this.props.data.allMarkdownRemark.edges.map(({ node }) => (
              <div key={node.id} className="work-card">
                <Link to={"/work" + node.fields.slug}>
                  <HeroDecoration frontmatter={node.frontmatter} />
                  <div className="work-content">
                    <h3>{node.frontmatter.category}</h3>
                    <h2>{node.frontmatter.title}</h2>
                    <p className="work-excerpt">{node.excerpt}</p>
                    <p className="work-details">Details →</p>
                  </div>
                </Link>
              </div>
            ))}
          </div> */}
          <div className="posts">
            {this.props.data.allMarkdownRemark.edges.map(({ node }) => (
              <div key={node.id} className="post-card">
                <a
                  href={node.frontmatter.link}
                  target="_blank"
                  rel="noreferrer noopener"
                >
                  <div className="post-header">
                    <div className="post-thumbnail">
                      <span className="emoji">{node.frontmatter.emoji}</span>
                    </div>
                    <div className="post-title">
                      <h3>{node.frontmatter.category}</h3>
                      <h2>{node.frontmatter.title}</h2>
                    </div>
                  </div>
                  <div className="post-content">
                    <div className="post-excerpt">
                      <p>{node.excerpt}</p>
                      <p className="post-read-more">{node.frontmatter.cta} →</p>
                    </div>
                  </div>
                </a>
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
      filter: { frontmatter: { template: { eq: "work" } } }
    ) {
      edges {
        node {
          id
          frontmatter {
            title
            category
            emoji
            link
            cta
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
