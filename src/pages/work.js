import React, { Component } from "react"
import { Link, graphql } from "gatsby"

import Layout from "../layouts/default"
import SEO from "../components/SEO"

const HeroDecoration = props => {
  if (props.frontmatter.hero !== null) {
    return (
      <div className="work-header">
        <img
          src={props.frontmatter.hero.childImageSharp.fixed.src}
          alt={props.frontmatter.title + " hero"}
        />
      </div>
    )
  } else {
    return null
  }
}

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
          <div className="works">
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
