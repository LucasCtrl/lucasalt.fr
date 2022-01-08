<template>
  <figure class="flex flex-col m-auto">
    <img :src="image" :alt="altText" class="rounded-md" />
    <caption class="text-sm">
      {{
        altText
      }}
    </caption>
  </figure>
</template>

<script>
export default {
  name: 'ImageComponent',
  props: {
    imgName: {
      type: String,
      default: null,
      required: true,
    },
    altText: {
      type: String,
      default: null,
      required: true,
    },
  },

  data: () => ({
    image: '',
  }),

  mounted() {
    if (this.imgName.includes('https://') || this.imgName.includes('http://'))
      this.image = this.imgName
    else this.image = `/img/blog/${this.$route.params.slug}/${this.imgName}`
  },
}
</script>
