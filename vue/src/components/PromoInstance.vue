<template>
  <div class="">
    {{ instance }}
  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
import { useRouter, useRoute } from 'vue-router'

export default {
  name: 'PromoInstance',
  components: {},
  setup() {
    const route = useRoute()
    const store = useStore()

    const instance = computed(() => store.state.qrmaker.instance)

    return {
      instance,
    }
  },
}
</script>