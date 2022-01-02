<template>
  <div class="flex justify-between items-center py-12">
    <div>
      <NuxtLink to="/" aria-label="Home">
        <Logo />
      </NuxtLink>
    </div>
    <div class="flex items-center space-x-8 text-xl">
      <NuxtLink to="/blog/" aria-label="Blog"> Blog </NuxtLink>
      <ThemeToggler />
    </div>
    <!-- <div>
      <NuxtLink to="work">Work</NuxtLink>
      <NuxtLink to="blog">Blog</NuxtLink>
      <NuxtLink to="about">About</NuxtLink>
    </div> -->
  </div>
</template>

<script>
import Logo from '@/components/Logo'
import ThemeToggler from '@/components/ThemeToggler'

export default {
  name: 'NavBar',
  components: {
    Logo,
    ThemeToggler,
  },
}
</script>
