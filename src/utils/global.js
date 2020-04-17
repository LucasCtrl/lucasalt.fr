import moment from "moment"

const formatDate = date => moment.utc(date).format("MMMM Do, YYYY")

export { formatDate }
