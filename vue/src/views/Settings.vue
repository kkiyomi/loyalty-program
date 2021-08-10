<template>
  <div class="grid grid-cols-7 w-full h-full sm:p-4 gap-6 lg:max-w-6xl">
    <div class="col-span-7 md:col-span-1 text-lg font-medium leading-6">
      <div>Account</div>
      <div>Profile</div>
    </div>
    <div class="col-span-7 md:col-span-6">
      <Account v-if="account" />
      <Profile v-if="profile" />
    </div>
  </div>
</template>


<script>
import Account from '../components/Settings/Account.vue'
import Profile from '../components/Settings/Profile.vue'

import { ref } from 'vue'
export default {
  name: 'SettingsView',
  components: {
    Account,
    Profile,
  },
  setup() {
    const account = ref(true)
    const profile = ref(false)
    const notification = ref(false)

    return {
      account,
      profile,
      notification,
    }
  },
}
</script>