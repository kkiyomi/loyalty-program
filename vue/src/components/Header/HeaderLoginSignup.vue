<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div v-if="!token">
    <DialogLogin />
    <DialogSignup />
  </div>
</template>

<script>
import DialogLogin from './DialogLogin.vue'
import DialogSignup from './DialogSignup.vue'

import { computed } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'HeaderLoginSignup',
  components: { DialogLogin, DialogSignup },
  setup() {
    const store = useStore()
    const token = computed(() => store.state.user.token)

    return { token }
  },
}
</script>