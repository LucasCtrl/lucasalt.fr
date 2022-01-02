<template>
  <div>
    <h1 class="text-center text-5xl font-semibold leading-normal mb-12">
      Blog
    </h1>
    <NuxtLink
      v-for="post in blogPosts"
      :key="post.slug"
      :to="`/blog/${post.slug}/`"
    >
      <div
        class="mb-6 p-5 border bg-slate-100 border-slate-200 dark:bg-slate-800 dark:border-slate-700 rounded-md"
      >
        <div class="flex sm:items-center">
          <img
            :src="`/img/blog/${post.slug}/thumbnail.png`"
            :alt="post.title + ' thumbnail image'"
            class="h-14 w-14 hidden sm:block"
          />
          <div class="sm:ml-6">
            <h3
              class="text-sm leading-normal text-slate-600 dark:text-slate-500"
            >
              {{ post.category }}
            </h3>
            <h2 class="text-2xl font-semibold leading-normal">
              {{ post.title }}
            </h2>
          </div>
        </div>

        <p class="ml-0 sm:ml-20 mt-4 text-justify">{{ post.description }}</p>
        <div
          class="ml-0 sm:ml-20 mt-4 flex justify-between text-sm text-slate-600 dark:text-slate-500"
        >
          <div class="hover:underline">Read more</div>
          <div>{{ formatDate(post.date) }}</div>
        </div>
      </div>
    </NuxtLink>
  </div>
</template>

<script>
export default {
  name: 'BlogPage',
  layout: 'default',

  async asyncData({ $content, params }) {
    const blogPosts = await $content('blog')
      .only(['title', 'description', 'category', 'date', 'slug'])
      .sortBy('date', 'desc')
      .fetch()
    return { blogPosts }
  },

  methods: {
    formatDate(date) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' }
      return new Date(date).toLocaleDateString('en', options)
    },
  },
}
</script>
