
<template>
  <div class="w-full text-black p-4">
    <div class="w-max-full -mx-4 sm:-mx-8 px-4 sm:px-8 py-4 overflow-x-auto">
      <div class="inline-block min-w-full shadow rounded-2xl overflow-hidden">
        <table class="min-w-full leading-normal">
          <thead>
            <tr>
              <th
                v-for="item in headers"
                :key="item.id"
                scope="col"
                class="
                  bg-white
                  dark:bg-gray-700
                  text-gray-800
                  dark:text-gray-200
                  text-sm
                  font-normal
                  px-5
                  py-3
                  text-left
                  uppercase
                "
              >
                {{ item.name }}
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in instanceList" :key="item.id" class="bg-white">
              <td class="text-sm text-gray-900 px-5 py-5">
                <div class="flex items-center">
                  <div class="ml-3">
                    <p class="whitespace-no-wrap">
                      {{ item.title }}
                    </p>
                  </div>
                </div>
              </td>
              <td class="text-sm text-gray-900 px-5 py-5">
                <p class="whitespace-no-wrap">
                  {{ item.uid }}
                </p>
              </td>
              <td class="text-sm text-gray-900 px-5 py-5">
                <p class="whitespace-no-wrap">transactions</p>
              </td>
              <td class="text-sm text-gray-900 px-5 py-5">
                <p class="whitespace-no-wrap">
                  {{ humanizeDate(item.date_added) }}
                </p>
              </td>
              <td class="text-sm px-5 py-5">
                <a href="#" class="text-indigo-600, hover:text-indigo-900">
                  Edit
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { useStore } from 'vuex'
import { computed } from 'vue'

export default {
  name: 'InstanceList',
  setup() {
    const headers = [
      { name: 'Title' },
      { name: 'uid' },
      { name: 'transactions' },
      { name: 'Created at' },
    ]

    const store = useStore()
    const instanceList = computed(() => store.state.qrmaker.instanceList)
    const humanizeDate = (date) => {
      const test = new Date(date)
      return test.toLocaleString('en-GB', { timeZone: 'UTC' })
    }

    return {
      instanceList,
      headers,
      humanizeDate,
    }
  },
}
</script>
