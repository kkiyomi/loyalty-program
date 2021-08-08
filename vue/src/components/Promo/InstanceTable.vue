
<template>
  <div
    class="
      w-full
      bg-gray-800
      text-gray-200 text-sm text-left
      sm:text-base
      font-normal
      overflow-hidden
      sm:rounded-lg
      sm:max-w-screen-lg
    "
  >
    <div class="p-4">
      <h3 class="text-lg leading-6 font-medium">Promo Instances</h3>
    </div>
    <div class="">
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
    const instanceList = computed(() => store.state.qrmaker.instanceList)
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
