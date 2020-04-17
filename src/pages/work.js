import React from "react"
import Layout from "../layouts/default"

export default ({ data }) => {
  console.log(data)
  return (
    <Layout>
      <div className="page">
        <div className="page-header">
          <h1 className="page-title">Work</h1>
        </div>
      </div>
    </Layout>
  )
}
