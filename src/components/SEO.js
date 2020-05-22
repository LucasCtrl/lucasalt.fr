import React, { Component } from "react"
import { Helmet } from "react-helmet"
import urlJoin from "url-join"

import config from "../../data/siteConfig"

export default class SEO extends Component {
  render() {
    const { seoType, meta, urlPath } = this.props
    let title
    let author
    let description
    let thumbnailImage

    let pageUrl = urlJoin(config.siteUrl, urlPath)

    if (seoType === "post") {
      const frontmatter = meta.frontmatter

      title = `${frontmatter.title} | ${config.siteTitle}`
      author = frontmatter.author
      description = meta.excerpt
      thumbnailImage = frontmatter.thumbnail.childImageSharp.fixed.src
      thumbnailImage = urlJoin(config.siteUrl, thumbnailImage)
    } else if (seoType === "work") {
      const frontmatter = meta.frontmatter

      title = `${frontmatter.title} | ${config.siteTitle}`
      author = "Lucas Albert"
      description = meta.excerpt
      thumbnailImage = config.siteLogo
      thumbnailImage = urlJoin(config.siteUrl, thumbnailImage)
    } else if (seoType === "page") {
      const frontmatter = meta.frontmatter

      title = `${frontmatter.title} | ${config.siteTitle}`
      author = "Lucas Albert"
      description = config.siteDescription
      thumbnailImage = config.siteLogo
      thumbnailImage = urlJoin(config.siteUrl, thumbnailImage)
    }

    return (
      <Helmet>
        <title>{title}</title>
        <meta name="author" content={author} />
        <meta name="description" content={description} />

        {/* Web monetization */}
        <meta name="monetization" content="$ilp.uphold.com/gzagLwDzUUdp">

        {/* Open Graph */}
        <meta property="og:locale" content="en-US" />
        <meta property="og:site_name" content={config.siteTitle} />
        <meta
          property="og:type"
          content={seoType === "post" ? "article" : "website"}
        />
        <meta property="og:url" content={pageUrl} />
        <meta property="og:title" content={title} />
        <meta property="og:description" content={description} />
        <meta property="og:image" content={thumbnailImage} />
        <meta property="og:image:type" content="image/png" />
        <meta property="og:image:alt" content={`${title} thumbnail`} />
        {/* <meta property="fb:app_id" content="app_code" /> */}

        {/* Twitter */}
        <meta property="twitter:card" content="summary" />
        <meta property="twitter:site" content="@LucasCtrlAlt" />
        <meta property="twitter:creator" content="@LucasCtrlAlt" />
        <meta property="twitter:title" content={title} />
        <meta property="twitter:description" content={description} />
        <meta property="twitter:image" content={thumbnailImage} />
        <meta property="twitter:url" content={pageUrl} />
      </Helmet>
    )
  }
}
