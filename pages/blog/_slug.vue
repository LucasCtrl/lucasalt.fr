<template>
  <div>
    <div>
      <p class="text-center text-slate-600 dark:text-slate-500">Blog</p>
      <h1 class="text-center text-5xl font-semibold leading-normal">
        {{ blogPost.title }}
      </h1>
      <div class="my-12">
        <div
          class="flex justify-between mx-auto mb-6 sm:max-w-lg md:max-w-xl lg:max-w-2xl xl:max-w-3xl text-slate-600 dark:text-slate-500"
        >
          <div>{{ blogPost.author }}</div>
          <div>{{ formatDate(blogPost.createdAt) }}</div>
        </div>
        <img
          v-if="blogPost.headerImage"
          :src="require(`~/assets/img/blog/${blogPost.slug}/header.jpg`)"
          :alt="blogPost.title + ' header image'"
          class="rounded-md"
        />
        <div class="mt-1 text-right text-slate-600 dark:text-slate-500">
          Image by
          <a
            :href="blogPost.sourceURL"
            target="_blank"
            rel="noopener noreferrer"
            class="underline"
            >{{ blogPost.source }}</a
          >
        </div>
      </div>
    </div>

    <NuxtContent :document="blogPost" />
    <!-- <pre>{{ blogPost }}</pre> -->
  </div>
</template>

<script>
export default {
  layout: 'default',

  async asyncData({ $content, params }) {
    const blogPost = await $content('blog', params.slug).fetch()

    return { blogPost }
  },

  methods: {
    formatDate(date) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' }
      return new Date(date).toLocaleDateString('en', options)
    },
  },
}
</script>

<style>
.nuxt-content h1,
.nuxt-content h2,
.nuxt-content h3,
.nuxt-content p {
  @apply mx-auto sm:max-w-lg md:max-w-xl lg:max-w-2xl xl:max-w-3xl;
}

.nuxt-content h1 {
  @apply text-4xl font-bold;
}

.nuxt-content h2 {
  @apply text-2xl font-bold;
}

.nuxt-content h3 {
  @apply text-xl font-bold;
}

.nuxt-content p {
  @apply text-base text-justify mb-6;
}

.nuxt-content figure {
  @apply text-base mb-6;
}
</style>
