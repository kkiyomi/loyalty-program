<template>
  <div v-if="promo">
    <div class="flex flex-col items-center space-y-8 w-screen sm:px-4 md:px-8">
      <PromoDetail />
      <InstanceTable v-if="instanceList" />
      <TransactionTable v-if="transactionList" />
    </div>
  </div>
</template>


<script>
import PromoDetail from '../components/Promo/PromoDetail.vue'
import InstanceTable from '../components/Promo/InstanceTable.vue'
import TransactionTable from '../components/Promo/TransactionTable.vue'

import { useStore } from 'vuex'
import { computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'

export default {
  name: 'Promo',
  components: { PromoDetail, InstanceTable, TransactionTable },
  setup() {
    const route = useRoute()
    const store = useStore()
    const promo_uid = route.params.promo_uid

    const promo = computed(() => store.getters.promo(promo_uid))
    const instanceList = computed(() => store.state.qrmaker.instanceList)
    const transactionList = computed(() => store.state.qrmaker.transactionList)

    const get_list = onMounted(() => {
      store.dispatch('getInstanceList', promo_uid)
      store.dispatch('getTransactionList', promo_uid)
    })

    return {
      promo,
      instanceList,
      transactionList,
      get_list,
    }
  },
}
</script>