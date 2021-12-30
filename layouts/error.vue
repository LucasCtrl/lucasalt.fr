<template>
  <div>
    <h1 v-if="error.statusCode === 404">Page not found</h1>
    <h1 v-else>An error occurred {{ error }}</h1>
  </div>
</template>

<script>
export default {
  name: 'DefaultLayout',
  layout: 'default',
  props: {
    error: {
      type: Object,
      default() {
        return {}
      },
    },
  },
}
</script>
