<template>
  <div>
    <div class="mt-[10%]">
      <h1 class="text-5xl font-semibold">
        Hey, I'm <br />
        <span class="text-blue-700 dark:text-blue-600 font-bold"
          >Lucas ALBERT</span
        >
      </h1>
      <h1 class="pt-4 text-2xl text-slate-600 dark:text-slate-500">
        Web developer / Maker / Love to play video games
      </h1>
    </div>
    <div class="mt-[10%] text-xl space-y-4 text-justify">
      <p>
        A 22 years old French web developer with more than five years of
        experience, I develop web applications and I am specialised in the
        development of ergonomic and minimalist interfaces.
      </p>
      <p>
        Currently instructor on
        <a
          href="https://en.wikipedia.org/wiki/Computer-aided_design"
          target="_blank"
          rel="noopener noreferrer"
          class="text-pink-600 hover:underline font-semibold"
          >CAD software</a
        >
        and
        <a
          href="https://en.wikipedia.org/wiki/Numerical_control"
          target="_blank"
          rel="noopener noreferrer"
          class="text-blue-600 hover:underline font-semibold"
          >CNC machines</a
        >, I take advantage of my free time to do prototyping in the mechanical
        keyboard area.
      </p>
      <p>
        I am also working on the library
        <a
          href="#"
          target="_blank"
          rel="noopener noreferrer"
          class="text-green-600 hover:underline font-semibold"
          >CanvasMe</a
        >. A library for creating canvas in a simplified way. In parallel I
        maintain
        <a
          href="https://github.com/lucasctrl/spookybot"
          target="_blank"
          rel="noopener noreferrer"
          class="text-orange-600 hover:underline font-semibold"
          >SpookyBot</a
        >, a little terror that comes to scare you on your Discord server. A
        project initiated during the Hacktoberfest 2020.
      </p>
    </div>
    <div class="mt-[10%]">
      <SocialButtons />
    </div>
    <!-- <div class="mt-[10%]">
      <hr class="border-t-2 border-slate-200 dark:border-slate-800" />
    </div> -->
  </div>
</template>

<script>
import SocialButtons from '@/components/SocialButtons.vue'

export default {
  name: 'IndexPage',
  components: { SocialButtons },
  layout: 'default',
}
</script>
