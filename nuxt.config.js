export default {
  target: 'static',

  generate: {
    fallback: true,
  },

  head: {
    title: 'LucasAlt',

    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  css: ['./assets/css/main.css'],

  plugins: [],

  components: true,

  buildModules: ['@nuxt/postcss8', '@nuxtjs/eslint-module'],

  modules: ['@nuxtjs/pwa', '@nuxt/content'],

  pwa: {
    meta: {
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',

      name: 'LucasAlt | Personal website',
      author: 'LucasAlt',
      description:
        'Web developer, UI/UX designer, minimalist, i leave my mark on this immense web that is the internet.',
      theme_color: '#1d4ed8',
      lang: 'en',

      // Open Graph
      ogType: 'website',
      // ogSiteName: '', // Retreive 'name' by default
      // ogTitle: '', // Retreive 'name' by default
      // ogDescription: '', // Retreive 'description' by default
      ogHost: 'https://lucasalt.fr', // Domain where the icon is hosted
      ogImage: true, // Use app icon
      // ogUrl: '', // Same as 'ogHost'

      // Twitter
      twitterCard: 'summary', // Twitter card type
      twitterSite: '@LucasCtrlAlt', // Twitter owner handle
      twitterCreator: '@LucasCtrlAlt', // Twitter developer handle
    },
    manifest: {
      name: 'LucasAlt | Personal website',
      short_name: 'LucasAlt',
      description:
        'Web developer, UI/UX designer, minimalist, i leave my mark on this immense web that is the internet.',
      background_color: '#f9fafb',
      dir: 'ltr',
      lang: 'en',
    },
  },

  build: {
    postcss: {
      plugins: {
        tailwindcss: {},
        autoprefixer: {},
      },
    },
  },
}
