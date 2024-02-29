// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    'nuxt-primevue'
],
primevue: {
    components: {
      include: ['Button', 'Fieldset', 'Avatar', 'Textarea', 'splitter', 'splitterpanel', 'scrollpanel', 'listbox', 'List']
    },
},
  css: ['primevue/resources/themes/aura-dark-indigo/theme.css', 'primeicons/primeicons.css'],
})
