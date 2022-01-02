ata
<template>
  <figure class="flex flex-col m-auto">
    <img
      :src="`/img/blog/${$route.params.slug}/${imgName}.png`"
      :alt="altText"
      class="rounded-md"
    />
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
}
</script>
