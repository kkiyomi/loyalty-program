<template>
  <div class="p-2 sm:w-10/12">
    <div class="inset-0 flex items-center justify-center">
      <button
        type="button"
        @click="openModal"
        class="
          px-4
          py-2
          text-sm
          font-medium
          text-white
          bg-black
          rounded-md
          bg-opacity-20
          hover:bg-opacity-30
          focus:outline-none
          focus-visible:ring-2
          focus-visible:ring-white
          focus-visible:ring-opacity-75
        "
      >
        Open dialog
      </button>
    </div>
    <h1>Home</h1>
    <h1>settings : {{ settings }}</h1>
    <h1>token : {{ token }}</h1>
    <h1 v-if="user.user">user : {{ user.user.email }}</h1>
    <div v-if="maker">
      <h1>headers : {{ headers }}</h1>
      <h1>maker uid: {{ maker.uid }}</h1>
      <br />
      <br />
      <h1>promos : {{ promos[0] }}</h1>
    </div>
    <button @click="delUserCookie" class="bg-red-500">delete cookie</button>
    <button @click="UserTokenLogin" class="m-10 bg-red-500">login</button>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'Home',
  components: {},
  setup() {
    const store = useStore()
    const user = computed(() => store.state.user)
    const token = computed(() => store.state.user.token)
    const headers = computed(() => store.getters.headers)

    const UserTokenLogin = async () => {
      const token = '63a9f042049952f3cfa5bc8df35bc91e62d34e30'
      await store.dispatch('UserTokenLogin', token)
      store.dispatch('getMaker')
    }

    const delUserCookie = () => {
      store.dispatch('UserSignout')
      store.dispatch('delMaker')
    }
    const maker = computed(() => store.state.qrmaker.maker)
    const promos = computed(() => store.state.qrmaker.maker.promos)
    const settings = computed(() => store.state.settings)

    const huminizeDate = (date) => date.split('T')[0]

    return {
      maker,
      UserTokenLogin,
      delUserCookie,
      huminizeDate,
      settings,
      promos,
      user,
      token,
      headers,
      openModal() {
        store.commit('SET_NOTI_DIALOG', true)
      },
    }
  },
}
</script>