<template>
  <div
    class="
      w-full
      bg-gray-800
      text-gray-200 text-sm text-left
      md:text-base
      font-normal
      overflow-hidden
      sm:rounded-lg
      sm:max-w-screen-lg
    "
  >
    <div class="p-4">
      <h3 class="text-lg leading-6 font-medium">Promo Instances</h3>
    </div>

    <div class="hidden sm:block">
      <div class="grid grid-cols-4 px-4 py-5 border-b-2 border-gray-500">
        <p class="font-medium col-span-2 text-gray-300 uppercase">
          Promo Instance uid
        </p>
        <p class="font-medium col-span-1 text-gray-300 uppercase">
          transactions
        </p>
        <p class="font-medium col-span-1 text-gray-300 uppercase">Created at</p>
      </div>
      <div
        v-for="item in instanceList"
        :key="item.id"
        class="grid grid-cols-4 px-4 py-5 border-b-2 border-gray-500"
      >
        <p class="mt-1 col-span-2">
          {{ item.uid }}
        </p>
        <p class="mt-1 col-span-1">
          {{ item.ts_count }}
        </p>
        <p class="mt-1 col-span-1">
          {{ humanizeDate(item.date_added) }}
        </p>
      </div>
    </div>

    <div class="sm:hidden">
      <dl
        v-for="item in instanceList"
        :key="item.id"
        class="grid grid-cols-4 px-4 py-5 border-b-2 border-gray-500"
      >
        <div class="col-span-4 sm:col-span-2">
          <dt class="font-medium text-gray-300 uppercase">
            Promo Instance uid
          </dt>
          <dd class="mt-1">
            {{ item.uid }}
          </dd>
        </div>
        <div class="col-span-2 pt-4 sm:col-span-1 sm:pt-0">
          <dt class="font-medium text-gray-300 uppercase">transactions</dt>
          <dd class="mt-1">
            {{ item.ts_count }}
          </dd>
        </div>
        <div class="col-span-2 pt-4 sm:col-span-1 sm:pt-0">
          <dt class="font-medium text-gray-300 uppercase">Created at</dt>
          <dd class="mt-1">
            {{ humanizeDate(item.date_added) }}
          </dd>
        </div>
      </dl>
    </div>
  </div>
</template>

<script>
import { useStore } from 'vuex'
import { computed } from 'vue'

export default {
  name: 'InstanceTable',
  setup() {
    const store = useStore()
    const promo = computed(() => store.state.qrmaker.promo)

    const instanceList = promo.value.pinstances
    const humanizeDate = (date) => {
      const test = new Date(date)
      return test.toLocaleString('en-GB', { timeZone: 'UTC' })
    }

    return {
      instanceList,
      humanizeDate,
    }
  },
}
</script>
