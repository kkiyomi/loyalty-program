<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <Disclosure as="nav" class="bg-gray-100 dark:bg-gray-800" v-slot="{ open }">
    <div class="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
      <div class="relative flex items-center justify-between h-16">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
          <!-- Mobile menu button-->
          <DisclosureButton
            class="
              inline-flex
              items-center
              justify-center
              p-2
              rounded-md
              text-gray-900
              dark:text-gray-400
              hover:text-white
              hover:bg-gray-700
              focus:outline-none
              focus:ring-2 focus:ring-inset focus:ring-white
            "
          >
            <span class="sr-only">Open main menu</span>
            <MenuIcon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
            <XIcon v-else class="block h-6 w-6" aria-hidden="true" />
          </DisclosureButton>
        </div>
        <div
          class="
            flex-1 flex
            items-center
            justify-center
            sm:items-stretch
            sm:justify-start
          "
        >
          <div class="flex-shrink-0 flex items-center">
            <img
              class="block lg:hidden h-8 w-auto"
              src="https://tailwindui.com/img/logos/workflow-mark-indigo-500.svg"
              alt="Workflow"
            />
          </div>
          <div class="hidden sm:block sm:ml-6">
            <div class="flex space-x-4">
              <router-link
                v-for="item in navigation"
                :key="item.name"
                :to="{ name: item.href }"
                custom
                v-slot="{ href, navigate, isActive }"
              >
                <a
                  :class="[
                    isActive
                      ? 'bg-gray-900 text-white'
                      : 'text-gray-900 dark:text-gray-400 hover:bg-gray-700 hover:text-white',
                    'px-3 py-2 rounded-md text-sm font-medium',
                  ]"
                  :href="href"
                  @click="navigate"
                  :aria-current="isActive ? 'page' : undefined"
                >
                  {{ item.name }}
                </a>
              </router-link>
            </div>
          </div>
        </div>
        <!-- Top Right -->
        <div>
          <HeaderLoginSignup
            v-if="!token"
            class="hidden sm:flex items-center justify-end md:flex-1 lg:w-0"
          />
        </div>
        <div
          class="
            absolute
            inset-y-0
            right-0
            flex
            items-center
            pr-2
            sm:static
            sm:inset-auto
            sm:ml-6
            sm:pr-0
            space-x-3
          "
        >
          <button
            v-if="user"
            @click="switchMode"
            class="
              p-1
              rounded-full
              text-gray-400
              hover:text-black
              dark:hover:text-white
              focus:outline-none
              focus:ring-2
              focus:ring-offset-2
              focus:ring-offset-gray-800
              focus:ring-white
            "
          >
            <SunIcon v-if="darkMode" class="h-6 w-6" aria-hidden="true" />
            <MoonIcon v-else class="h-6 w-6" aria-hidden="true" />
          </button>

          <button
            v-if="user"
            class="
              p-1
              rounded-full
              text-gray-400
              hover:text-black
              dark:hover:text-white
              focus:outline-none
              focus:ring-2
              focus:ring-offset-2
              focus:ring-offset-gray-800
              focus:ring-white
              hidden
              sm:block
            "
          >
            <BellIcon class="h-6 w-6" aria-hidden="true" />
          </button>

          <!-- Profile dropdown -->
          <Menu v-if="user" as="div" class="pl-2 relative">
            <div>
              <MenuButton
                class="
                  bg-gray-800
                  flex
                  text-sm
                  rounded-full
                  focus:outline-none
                  focus:ring-2
                  focus:ring-offset-2
                  focus:ring-offset-gray-800
                  focus:ring-white
                "
              >
                <span class="sr-only">Open user menu</span>
                <!-- src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                   -->
                <img
                  class="h-8 w-8 rounded-full"
                  src="https://cdn.pixabay.com/photo/2018/08/25/11/20/abstract-3629844_960_720.jpg"
                  alt=""
                />
              </MenuButton>
            </div>
            <transition
              enter-active-class="transition ease-out duration-100"
              enter-from-class="transform opacity-0 scale-95"
              enter-to-class="transform opacity-100 scale-100"
              leave-active-class="transition ease-in duration-75"
              leave-from-class="transform opacity-100 scale-100"
              leave-to-class="transform opacity-0 scale-95"
            >
              <MenuItems
                class="
                  origin-top-right
                  absolute
                  right-0
                  mt-2
                  w-48
                  rounded-md
                  shadow-lg
                  py-1
                  bg-white
                  ring-1 ring-black ring-opacity-5
                  focus:outline-none
                "
              >
                <MenuItem disabled>
                  <span
                    class="opacity-75 block px-4 py-2 text-sm text-gray-700"
                  >
                    Logged in as {{ user.email ? user.email : 'XXX' }}
                  </span>
                </MenuItem>
                <MenuItem
                  as="router-link"
                  v-for="item in settings"
                  :key="item.name"
                  v-slot="{ active }"
                >
                  <router-link
                    :to="{ name: item.href }"
                    custom
                    v-slot="{ href, navigate }"
                  >
                    <a
                      :class="[
                        active ? 'bg-gray-100' : '',
                        'block px-4 py-2 text-sm text-gray-700',
                      ]"
                      :href="href"
                      @click="navigate"
                    >
                      {{ item.name }}
                    </a>
                  </router-link>
                </MenuItem>
              </MenuItems>
            </transition>
          </Menu>
        </div>
      </div>
    </div>

    <DisclosurePanel class="sm:hidden">
      <div class="px-2 pt-2 pb-3 space-y-1">
        <router-link
          v-for="item in navigation"
          :key="item.name"
          :to="{ name: item.href }"
          custom
          v-slot="{ href, navigate, isActive }"
        >
          <a
            :class="[
              isActive
                ? 'bg-gray-900 text-white'
                : 'text-gray-900 dark:text-gray-400  hover:bg-gray-700 hover:text-white',
              'block px-3 py-2 rounded-md text-base font-medium',
            ]"
            :href="href"
            @click="navigate"
            :aria-current="isActive ? 'page' : undefined"
          >
            {{ item.name }}
          </a>
        </router-link>
      </div>
    </DisclosurePanel>
  </Disclosure>
</template>

<script>
import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
} from '@headlessui/vue'
import {
  SunIcon,
  MoonIcon,
  BellIcon,
  MenuIcon,
  XIcon,
} from '@heroicons/vue/outline'

import { watch, ref, computed } from 'vue'
import { useStore } from 'vuex'

import HeaderLoginSignup from './HeaderLoginSignup.vue'

const navigation = [
  { name: 'Home', href: 'Home' },
  { name: 'Dashboard', href: 'Dashboard' },
  { name: 'test', href: 'test' },
]

const settings = [
  { name: 'Signin', href: 'Home' },
  { name: 'Sign out', href: 'Home' },
]

export default {
  components: {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
    Menu,
    MenuButton,
    MenuItem,
    MenuItems,
    BellIcon,
    MenuIcon,
    XIcon,
    SunIcon,
    MoonIcon,
    HeaderLoginSignup,
  },
  setup() {
    const store = useStore()
    const token = computed(() => store.state.user.token)

    const darkMode = computed(() => store.state.user.darkMode)
    const setDarkmode = (data) => store.dispatch('setDarkmode', data)
    const switchMode = () => {
      setDarkmode(!darkMode.value)
    }

    const user = computed(() => store.state.user.user)
    const UserSignout = () => store.dispatch('UserSignout')

    const open = ref(false)
    return {
      user,
      UserSignout,
      darkMode,
      navigation,
      settings,
      switchMode,
      open,
      token,
    }
  },
}
</script>

