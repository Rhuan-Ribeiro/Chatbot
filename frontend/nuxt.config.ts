// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    'nuxt-primevue'
],
primevue: {
    components: {
      include: ['Button', 'Fieldset', 'Avatar', 'Textarea']
    },
},
  css: ['primevue/resources/themes/md-light-indigo/theme.css', 'primeicons/primeicons.css'],
})
