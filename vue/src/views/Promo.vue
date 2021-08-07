<template>
  <div v-if="promo">
    <div class="flex flex-col items-center w-screen sm:px-4 md:px-8">
      <PromoDetail />
      <div class="w-10/12">
        <InstanceList v-if="instanceList" />
      </div>
    </div>
  </div>
</template>


<script>
import PromoDetail from '../components/Promo/PromoDetail.vue'
import InstanceList from '../components/Promo/InstanceList.vue'

import { useStore } from 'vuex'
import { computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'

export default {
  name: 'Promo',
  components: { PromoDetail, InstanceList },
  setup() {
    const route = useRoute()
    const store = useStore()
    const promo_uid = route.params.promo_uid

    const promo = computed(() => store.getters.promo(promo_uid))
    const instanceList = computed(() => store.state.qrmaker.instanceList)

    const get_list = onMounted(() => {
      store.dispatch('getInstanceList', promo_uid)
    })

    return {
      promo,
      instanceList,
      get_list,
    }
  },
}
</script>