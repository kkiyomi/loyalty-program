<template>
  <div class="grid grid-cols-5 w-full h-full sm:p-4 gap-6 lg:px-16">
    <div class="col-span-5 md:col-span-1 leading-6 dark:text-white">
      <button
        v-for="item in tabs"
        :key="item.index"
        class="block p-2 my-2 rounded-md w-full text-sm text-left"
        :class="
          activeTab === item.tabName
            ? 'bg-gray-300 dark:text-gray-900'
            : 'hover:bg-gray-300 dark:hover:bg-gray-500 '
        "
        @click="activeTab = item.tabName"
      >
        {{ item.title }}
      </button>
    </div>

    <div class="col-span-5 md:col-span-4">
      <Account v-if="activeTab === 'account'" />
      <Profile v-if="activeTab === 'profile'" />
    </div>
  </div>
</template>


<script>
import Account from '../components/Settings/Account.vue'
import Profile from '../components/Settings/Profile.vue'

import { ref, reactive } from 'vue'
export default {
  name: 'SettingsView',
  components: {
    Account,
    Profile,
  },
  setup() {
    const activeTab = ref('account')
    const tabs = reactive([
      { title: 'Account', tabName: 'account' },
      { title: 'Profile', tabName: 'profile' },
    ])

    return {
      activeTab,
      tabs,
    }
  },
}
</script>