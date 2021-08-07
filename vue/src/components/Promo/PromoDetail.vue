<template>
  <div
    v-if="promo"
    class="
      w-full
      bg-gray-800
      text-gray-200
      shadow
      overflow-hidden
      sm:rounded-lg
      sm:max-w-screen-lg
    "
  >
    <div class="px-4 py-5 sm:px-6">
      <h3 class="text-lg leading-6 font-medium">Promo Information</h3>
      <!-- <p class="mt-1 max-w-2xl text-sm text-gray-300">
          Personal details and application.
        </p> -->
    </div>
    <div class="border-t border-gray-900">
      <dl>
        <div class="px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          <dt class="text-sm font-medium text-gray-300">Title</dt>
          <dd class="mt-1 text-sm sm:mt-0 sm:col-span-2">
            {{ promo.title }}
          </dd>
        </div>
        <div class="px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          <dt class="text-sm font-medium text-gray-300">UID</dt>
          <dd class="mt-1 text-sm sm:mt-0 sm:col-span-2">
            {{ promo.uid }}
          </dd>
        </div>
        <div class="px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          <dt class="text-sm font-medium text-gray-300">State</dt>
          <dd class="mt-1 text-sm sm:mt-0 sm:col-span-2">
            {{ promo.state }}
          </dd>
        </div>
        <div class="px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          <dt class="text-sm font-medium text-gray-300">SUID</dt>
          <dd class="mt-1 text-sm sm:mt-0 sm:col-span-2">
            {{ promo.suid }}
          </dd>
        </div>
        <div class="px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          <dt class="text-sm font-medium text-gray-300">Size</dt>
          <dd class="mt-1 text-sm sm:mt-0 sm:col-span-2">
            {{ promo.size }}
          </dd>
        </div>
        <div class="px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          <dt class="text-sm font-medium text-gray-300">date_added</dt>
          <dd class="mt-1 text-sm sm:mt-0 sm:col-span-2">
            {{ promo.date_added }}
          </dd>
        </div>
        <div class="px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          <dt class="text-sm font-medium text-gray-300">Description</dt>
          <dd class="mt-1 text-sm sm:mt-0 sm:col-span-2">
            {{ promo.description }}
          </dd>
        </div>
      </dl>
    </div>
  </div>
</template>


<script>
import { useStore } from 'vuex'
import { computed } from 'vue'
import { useRoute } from 'vue-router'

export default {
  name: 'PromoDetail',
  components: {},
  setup() {
    const store = useStore()
    const route = useRoute()
    const promo_uid = route.params.promo_uid

    const promo = computed(() => store.getters.promo(promo_uid))

    return {
      promo,
    }
  },
}
</script>