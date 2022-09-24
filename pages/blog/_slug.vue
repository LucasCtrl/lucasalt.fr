<template>
  <div>
    <div>
      <p class="text-center text-slate-600 dark:text-slate-500">
        {{ blogPost.category }}
      </p>
      <h1 class="text-center text-5xl font-semibold leading-normal">
        {{ blogPost.title }}
      </h1>
      <div class="my-12">
        <div
          class="flex justify-between mx-auto mb-6 sm:max-w-lg md:max-w-xl lg:max-w-2xl xl:max-w-3xl text-slate-600 dark:text-slate-500"
        >
          <div>{{ blogPost.author }}</div>
          <div>{{ formatDate(blogPost.date) }}</div>
        </div>
        <div v-if="blogPost.headerImage">
          <img
            :src="`/img/blog/${blogPost.slug}/header.png`"
            :alt="blogPost.title + ' header image'"
            class="rounded-md"
          />
          <div class="mt-1 text-right text-slate-600 dark:text-slate-500">
            Image by
            <a
              v-if="blogPost.sourceURL"
              :href="blogPost.sourceURL"
              target="_blank"
              rel="noopener noreferrer"
              class="underline"
              >{{ blogPost.source }}</a
            ><span v-else>{{ blogPost.source }}</span>
          </div>
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
.nuxt-content p,
.nuxt-content blockquote,
.nuxt-content table,
.nuxt-content ol,
.nuxt-content ul {
  @apply mx-auto sm:max-w-lg md:max-w-xl lg:max-w-2xl xl:max-w-3xl;
}

.nuxt-content h1 {
  @apply text-4xl font-bold leading-normal;
}

.nuxt-content h2 {
  @apply text-2xl font-bold leading-normal;
}

.nuxt-content h3 {
  @apply text-xl font-bold leading-normal;
}

.nuxt-content p {
  @apply text-base text-justify mb-6;
}

.nuxt-content a {
  @apply text-base text-blue-700 dark:text-blue-500 underline;
}

.nuxt-content figure {
  @apply text-base mb-6;
}

.nuxt-content blockquote {
  @apply px-8 py-4 mb-6;
}

.nuxt-content blockquote p {
  @apply text-base text-justify mb-0;
}

.nuxt-content table {
  @apply border border-slate-200 dark:border-slate-700 border-collapse box-border table-fixed mb-6;
}

.nuxt-content table th {
  @apply border border-slate-200 dark:border-slate-700 bg-slate-100 dark:bg-slate-800 px-2 py-1 text-left;
}

.nuxt-content table td {
  @apply border border-slate-200 dark:border-slate-700 px-2 py-1;
}

.nuxt-content ol > li,
.nuxt-content ul > li {
  @apply ml-8;
}

.nuxt-content ol {
  @apply list-decimal mb-6;
}

.nuxt-content ul {
  @apply list-disc mb-6;
}

.nuxt-content-highlight {
  @apply mb-6 rounded overflow-hidden text-[#575279] dark:text-[#e0def4] bg-[#faf4ed] dark:bg-[#191724] selection:bg-[#eee9e6] dark:selection:bg-[#2a2837] border border-[#6e6a86] border-opacity-80 dark:border-opacity-60;
}

.nuxt-content-highlight .filename {
  @apply px-4;
}

.nuxt-content-highlight .language-css .token.string {
  background: none;
}

.nuxt-content pre {
  @apply m-0 px-4 py-2 first:border-none border-t border-[#6e6a86] border-opacity-80 dark:border-opacity-60;
}
</style>
