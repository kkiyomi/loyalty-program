<template>
  <div class="w-56 text-right">
    <Menu as="div" class="relative inline-block text-left">
      <div>
        <MenuButton
          class="
            inline-flex
            justify-center
            w-full
            px-3
            py-2
            text-sm
            font-medium
            text-indigo-900
            rounded-md
            bg-opacity-20
            hover:bg-opacity-30
            focus:outline-none
            focus-visible:ring-2
            focus-visible:ring-white
            focus-visible:ring-opacity-75
            bg-indigo-400
            hover:bg-indigo-500
          "
        >
          Options
          <ChevronDownIcon
            class="w-5 h-5 ml-2 -mr-1 text-indigo-900"
            aria-hidden="true"
          />
        </MenuButton>
      </div>

      <transition
        enter-active-class="transition duration-100 ease-out"
        enter-from-class="transform scale-95 opacity-0"
        enter-to-class="transform scale-100 opacity-100"
        leave-active-class="transition duration-75 ease-in"
        leave-from-class="transform scale-100 opacity-100"
        leave-to-class="transform scale-95 opacity-0"
      >
        <MenuItems
          class="
            z-10
            absolute
            right-0
            w-40
            mt-2
            origin-top-right
            bg-white
            divide-y divide-gray-100
            rounded-md
            shadow-lg
            ring-1 ring-black ring-opacity-5
            focus:outline-none
          "
        >
          <div class="px-1 py-1">
            <MenuItem v-slot="{ active }">
              <button
                @click="test(promo)"
                :class="[
                  active ? 'bg-indigo-500 text-white' : 'text-gray-900',
                  'group flex rounded-md items-center w-full px-2 py-2 text-sm',
                ]"
              >
                <PencilIcon
                  class="w-5 h-5 mr-2 text-indigo-400"
                  aria-hidden="true"
                />
                Edit
              </button>
            </MenuItem>
            <MenuItem v-slot="{ active }">
              <button
                @click="DeletePromo(promo.uid)"
                :class="[
                  active ? 'bg-indigo-500 text-white' : 'text-gray-900',
                  'group flex rounded-md items-center w-full px-2 py-2 text-sm',
                ]"
              >
                <TrashIcon
                  :active="active"
                  class="w-5 h-5 mr-2 text-indigo-400"
                  aria-hidden="true"
                />
                Delete
              </button>
            </MenuItem>
          </div>
        </MenuItems>
      </transition>
    </Menu>
  </div>
</template>

<script>
import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/vue'
import {
  ChevronDownIcon,
  PencilIcon,
  ArchiveIcon,
  TrashIcon,
} from '@heroicons/vue/solid'

import { useStore } from 'vuex'
import { computed } from 'vue'

export default {
  name: 'PromoEditMenu',
  components: {
    Menu,
    MenuButton,
    MenuItems,
    MenuItem,
    ChevronDownIcon,
    PencilIcon,
    TrashIcon,
  },
  props: {
    promo: {
      type: Object,
      default() {
        return { title: '' }
      },
    },
  },
  setup(props) {
    const store = useStore()
    const DeletePromo = (promo_uid) => store.dispatch('DeletePromo', promo_uid)

    return {
      DeletePromo,
      test(data) {
        console.log(data)
      },
    }
  },
}
</script>
