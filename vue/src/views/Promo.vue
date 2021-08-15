<template>
  <div v-if="promo" class="">
    <div
      class="
        flex flex-wrap
        items-center
        w-full
        space-y-8
        sm:px-4
        md:px-8
        sm:max-w-4xl
      "
    >
      <PromoDetail />
      <InstanceTable />
      <TransactionTable />
    </div>
  </div>
</template>


<script>
import PromoDetail from '../components/Promo/PromoDetail.vue'
import InstanceTable from '../components/Promo/InstanceTable.vue'
import TransactionTable from '../components/Promo/TransactionTable.vue'

import { useStore } from 'vuex'
import { computed } from 'vue'
import { useRoute } from 'vue-router'

export default {
  name: 'Promo',
  components: { PromoDetail, InstanceTable, TransactionTable },
  setup() {
    const route = useRoute()
    const store = useStore()
    const promo_uid = route.params.promo_uid

    const getPromo = async () => {
      await store.dispatch('getPromo', promo_uid)
    }

    getPromo()
    const promo = computed(() => store.state.qrmaker.promo)
    return {
      promo,
    }
  },
}
</script>