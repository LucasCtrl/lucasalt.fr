import React, { Component } from "react"
import { graphql } from "gatsby"

import Layout from "../layouts/default"
import SEO from "../components/SEO"

const HeroDecoration = props => {
  if (props.frontmatter.hero !== null) {
    return (
      <div className="page-decoration">
        <div className="page-hero">
          <img
            src={props.frontmatter.hero.childImageSharp.fixed.src}
            alt={props.frontmatter.title + " hero"}
          />
        </div>
      </div>
    )
  } else {
    return null
  }
}

export default class Work extends Component {
  render() {
    const { slug } = this.props.pageContext
    const work = this.props.data.markdownRemark
    const frontmatter = work.frontmatter

    return (
      <Layout>
        <SEO meta={work} urlPath={slug} seoType="work" />
        <div className="page">
          <div className="page-header">
            <p className="page-subtitle">{frontmatter.category}</p>
            <h1 className="page-title">{frontmatter.title}</h1>
          </div>
          <HeroDecoration frontmatter={frontmatter} />
          <div
            className="page-content"
            dangerouslySetInnerHTML={{ __html: work.html }}
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
        category
        title
        hero {
          childImageSharp {
            fixed(width: 1280, toFormat: PNG) {
              src
            }
          }
        }
      }
      excerpt
      html
    }
  }
`
