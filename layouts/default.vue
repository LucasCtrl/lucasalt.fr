<template>
  <div class="min-h-screen relative text-black bg-gray-50 dark:text-white dark:bg-gray-900">
    <div class="h-full container mx-auto sm:max-w-xl md:max-w-2xl lg:max-w-4xl 2xl:max-w-6xl px-8 sm:px-0 pb-28">
      <NavBar />
      <Nuxt />
    </div>
    <Footer />
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'
import Footer from '@/components/Footer'

export default {
  name: 'DefaultLayout',
  components: {
    NavBar,
    Footer,
  },

  beforeMount() {
    this.$store.dispatch('theme/getLocalTheme')
  },
}
</script>
