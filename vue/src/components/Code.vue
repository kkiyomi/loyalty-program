<template>
  <div
    v-if="instance"
    class="shadow-lg rounded-2xl p-4 bg-white dark:bg-gray-800 w-64 m-auto"
  >
    <div class="w-full h-full text-center">
      <div class="flex h-full flex-col justify-between">
        <CheckIcon
          class="h-12 w-12 mt-4 m-auto text-green-500"
          aria-hidden="true"
        />
        <p class="text-gray-600 dark:text-gray-100 text-md py-2 px-6">
          Success {{ promo_suid }}
        </p>
        <div class="flex items-center justify-between gap-4 w-full mt-8">
          <router-link
            :to="{
              name: 'PromoInstance',
              params: { pinstance_uid: instance.uid },
            }"
            custom
            v-slot="{ navigate }"
          >
            <button
              @click="navigate"
              class="
                py-2
                px-4
                bg-indigo-600
                hover:bg-indigo-700
                focus:ring-indigo-500 focus:ring-offset-indigo-200
                text-white
                w-full
                transition
                ease-in
                duration-200
                text-center text-base
                font-semibold
                shadow-md
                focus:outline-none
                focus:ring-2 focus:ring-offset-2
                rounded-lg
              "
            >
              Go to Promo Page
            </button>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { CheckIcon } from '@heroicons/vue/outline'

import { computed } from 'vue'
import { useStore } from 'vuex'
import { useRouter, useRoute } from 'vue-router'

export default {
  name: 'Code',
  components: {
    CheckIcon,
  },
  setup() {
    const route = useRoute()
    const promo_suid = route.params.promo_suid

    const store = useStore()
    const instance = computed(() => store.state.qrmaker.instance)

    const promoInstanceCookie = computed(
      () => store.getters.promoInstanceCookie
    )

    const AddPromoInstance = async (promo_suid) => {
      await store.dispatch('addPromoInstance', promo_suid)
      await store.dispatch('getInstance', promo_suid)
      store.dispatch('setPromoInstanceCookie', promoInstanceCookie.value)
    }

    const test = async () => {
      await store.dispatch('getPromoInstanceCookie', promo_suid)
      if (!instance.value) {
        await AddPromoInstance(promo_suid)
        store.dispatch('setPromoInstanceCookie', promoInstanceCookie.value)
      }
    }
    test()

    return {
      promo_suid,
      instance,
    }
  },
}
</script>