export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'sge',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
    { rel: "stylesheet", href: "https://unpkg.com/primeflex@3.1.0/primeflex.css" },],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['primeflex/primeflex.css', '~/static/global.scss'],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: '~/plugins/persistedState.client.js' }
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // Doc: https://www.primefaces.org/primevue/showcase-v2/#/setup
    'primevue/nuxt',
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: 'http://127.0.0.1:8000/api/',
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    // https://github.com/primefaces/primevue/issues/844
    transpile: ['primevue'],
  },
  primevue: {
    theme: "saga-blue",
    ripple: true,
    components: [
      "InputText",
      "Textarea",
      "Divider",
      "Panel",
      "Button",
      "DataTable",
      "Column",
      "toast",
      "Dropdown",
      "Steps",
      "Sidebar",
      "PickList",
      "Carousel",
      "TabView",
      "TabPanel",
      "Accordion",
      "AccordionTab",
      "Timeline",
      "Toolbar",
      "Carousel",
      "Dialog",
      "FileUpload",
      "Rating",
      "MultiSelect",
    ]
  },
}
