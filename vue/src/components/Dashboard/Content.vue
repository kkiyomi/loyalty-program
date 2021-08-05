<template>
  <div class="flex flex-wrap">
    <div class="w-full bg-gray-800 py-6 px-6 rounded-3xl">
      <div class="flex justify-between text-white items-center mb-8">
        <p class="text-2xl font-bold">Welcome, {{ maker.username }}</p>
        <p class="hidden">December, 12</p>
      </div>
      <div class="flex flex-wrap justify-between items-center pb-8">
        <div class="flex flex-wrap text-white">
          <div class="pr-10">
            <div class="text-2xl font-bold">45</div>
            <div class="">In Progress</div>
          </div>
          <div class="pr-10">
            <div class="text-2xl font-bold">24</div>
            <div class="">Upcoming</div>
          </div>
          <div>
            <div class="text-2xl font-bold">62</div>
            <div class="">Total Projects</div>
          </div>
        </div>
        <div class="flex items-center mt-4 md:mt-0">
          <button
            class="text-white p-2"
            :class="list_view ? 'bg-gray-700' : 'bg-transparent'"
            title="List View"
            @click="list_view = true"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <line x1="8" y1="6" x2="21" y2="6" />
              <line x1="8" y1="12" x2="21" y2="12" />
              <line x1="8" y1="18" x2="21" y2="18" />
              <line x1="3" y1="6" x2="3.01" y2="6" />
              <line x1="3" y1="12" x2="3.01" y2="12" />
              <line x1="3" y1="18" x2="3.01" y2="18" />
            </svg>
          </button>
          <button
            class="text-white p-2 ml-2"
            :class="!list_view ? 'bg-gray-700' : 'bg-transparent'"
            title="Grid View"
            @click="list_view = false"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <rect x="3" y="3" width="7" height="7" />
              <rect x="14" y="3" width="7" height="7" />
              <rect x="14" y="14" width="7" height="7" />
              <rect x="3" y="14" width="7" height="7" />
            </svg>
          </button>
        </div>
      </div>

      <DashboardTable v-if="list_view" />
      <PromoBox v-else />
    </div>
  </div>
</template>

<script>
import { useStore } from 'vuex'
import { ref, computed } from 'vue'

import DashboardTable from './DashboardTable.vue'
import PromoBox from './PromoBox.vue'

export default {
  name: 'Content',

  components: { DashboardTable, PromoBox },
  setup() {
    const store = useStore()
    const list_view = ref(false)
    const maker = computed(() => store.state.qrmaker.maker)

    return {
      maker,
      list_view,
    }
  },
}
</script>
