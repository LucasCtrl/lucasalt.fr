import React from "react"
import { graphql } from "gatsby"
import Layout from "../layouts/default"
import { formatDate } from "../utils/global"

const SourceLink = props => {
  if (props.url !== "none") {
    return (
      <a href={props.url} target="_blank" rel="noopener noreferrer">
        {props.text}
      </a>
    )
  } else {
    return props.text
  }
}

export default ({ data }) => {
  const post = data.markdownRemark
  const frontmatter = post.frontmatter
  const date = formatDate(frontmatter.date)
  return (
    <Layout>
      <div className="page">
        <div className="page-header">
          <p className="page-subtitle">{frontmatter.category}</p>
          <h1 className="page-title">{frontmatter.title}</h1>
        </div>
        <div className="page-decoration">
          <div className="page-informations">
            <div className="page-auhor">{frontmatter.author}</div>
            <div className="page-date">{date}</div>
          </div>
          <div className="page-hero">
            <img
              src={frontmatter.hero.childImageSharp.fixed.src}
              alt={frontmatter.title + " hero"}
            />
            <div className="hero-source">
              Image by{" "}
              <SourceLink
                url={frontmatter.sourceURL}
                text={frontmatter.source}
              />
            </div>
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
        author
        date
        hero {
          childImageSharp {
            fixed(width: 1280) {
              src
            }
          }
        }
        source
        sourceURL
      }
      html
    }
  }
`
