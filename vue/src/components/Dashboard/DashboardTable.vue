
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
            <tr v-for="item in promos" :key="item.id" class="bg-white">
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
                  {{ item.description }}
                </p>
              </td>
              <td class="text-sm text-gray-900 px-5 py-5">
                <p class="whitespace-no-wrap">
                  {{ item.suid }}
                </p>
              </td>
              <td class="text-sm text-gray-900 px-5 py-5">
                <p class="whitespace-no-wrap">
                  {{ item.size }}
                </p>
              </td>
              <td class="text-sm text-gray-900 px-5 py-5">
                <p class="whitespace-no-wrap">
                  {{ humanizeDate(item.date_added) }}
                </p>
              </td>
              <td class="text-sm px-5 py-5">
                <span
                  class="
                    text-green-900
                    font-semibold
                    relative
                    inline-block
                    px-3
                    py-1
                    leading-tight
                  "
                >
                  <span
                    aria-hidden="true"
                    class="
                      bg-green-200
                      opacity-50
                      absolute
                      inset-0
                      rounded-full
                    "
                  >
                  </span>
                  <span class="relative"> {{ item.state }} </span>
                </span>
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
  name: 'DashboardTable',
  setup() {
    const headers = [
      { name: 'Title' },
      { name: 'Discription' },
      { name: 'Code' },
      { name: 'Size' },
      { name: 'Created at' },
      { name: 'Status' },
      { name: '' },
    ]
    const users = [
      {
        name: 'Jean marc',
        avatar: '/images/person/8.jpg',
        role: 'Admin',
        date: '01/10/2012',
        status: 'active',
      },
    ]
    const store = useStore()
    const promos = computed(() => store.getters.promos)
    const humanizeDate = (date) => date.split('T')[0]

    return {
      promos,
      headers,
      humanizeDate,
      users,
    }
  },
}
</script>
