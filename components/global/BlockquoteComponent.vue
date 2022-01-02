<template>
  <blockquote :class="`rounded ${blockquoteClasses}`">
    <div>
      <p class="font-bold"><slot name="title"></slot></p>
      <p><slot name="content"></slot></p>
    </div>
    <p class="mt-2 text-sm text-slate-700 dark:text-slate-300">
      <slot name="source"></slot>
    </p>
  </blockquote>
</template>

<script>
export default {
  name: 'BlockquoteComponent',
  props: {
    color: {
      type: String,
      default: '',
    },
  },

  data: () => ({
    blockquoteClasses: '',
  }),

  mounted() {
    if (this.color === 'warning')
      this.blockquoteClasses = 'bg-amber-400/20 border-l-4 border-amber-400'
    else this.blockquoteClasses = 'bg-slate-400/20 border-l-4 border-slate-400'
  },
}
</script>
