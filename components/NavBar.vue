<template>
  <div class="flex justify-between items-center py-12">
    <div>
      <NuxtLink to="/">
        <Logo />
      </NuxtLink>
    </div>
    <div>
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
