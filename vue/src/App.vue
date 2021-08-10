<template>
  <div :class="darkMode ? 'dark' : ''">
    <Header />
    <div
      class="
        py-10
        min-h-screen
        h-full
        flex
        place-content-center
        bg-gray-200
        dark:bg-gray-700
        dark:text-gray-100
      "
    >
      <router-view />
    </div>
    <Note />
  </div>
</template>


<script>
import { useStore } from 'vuex'
import { computed } from 'vue'

import Header from './components/Header/Header.vue'
import Note from './components/Notification.vue'

export default {
  components: { Header, Note },

  setup() {
    const store = useStore()
    const darkMode = computed(() => store.state.settings.darkMode)
    const token = computed(() => store.state.user.token)

    const getCookies = () => store.dispatch('getCookies')
    getCookies()

    if (token.value) {
      store.dispatch('alreadyLogged')
    }

    return {
      darkMode,
    }
  },
}
</script>
