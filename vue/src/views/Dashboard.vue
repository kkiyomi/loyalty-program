<template>
  <div v-if="maker" class="w-full p-4">
    <Content />
  </div>
</template>

<script>
import { useStore } from 'vuex'
import { computed } from 'vue'

import Content from '../components/Dashboard/Content.vue'

export default {
  name: 'Dashboard',
  components: { Content },
  setup() {
    const store = useStore()
    const maker = computed(() => store.state.qrmaker.maker)

    return {
      maker,
    }
  },
}
</script>