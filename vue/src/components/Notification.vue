<template>
  <div>
    <TransitionRoot
      appear
      :show="notiIsOpen"
      :class="darkMode ? 'dark' : ''"
      as="template"
    >
      <Dialog as="div" @close="closeModal">
        <DialogOverlay class="fixed inset-0 bg-black opacity-0" />
        <div class="absolute inset-0 z-10 overflow-y-auto">
          <div class="min-h-screen mt-10 px-4 text-center">
            <TransitionChild
              as="template"
              enter="duration-300 ease-out"
              enter-from="opacity-0"
              enter-to="opacity-100"
              leave="duration-200 ease-in"
              leave-from="opacity-100"
              leave-to="opacity-0"
            >
              <DialogOverlay class="fixed inset-0" />
            </TransitionChild>

            <TransitionChild
              as="div"
              enter="duration-300 ease-out"
              enter-from="opacity-0 scale-95"
              enter-to="opacity-100 scale-100"
              leave="duration-200 ease-in"
              leave-from="opacity-100 scale-100"
              leave-to="opacity-0 scale-95"
            >
              <!--  -->
              <div
                class="
                  shadow-lg
                  rounded-2xl
                  p-4
                  bg-white
                  align-middle
                  dark:bg-gray-800
                  w-auto
                  m-auto
                  sm:max-w-2xl
                "
              >
                <div class="w-full h-full text-center">
                  <div class="flex h-full justify-between items-center">
                    <CheckIcon
                      class="h-12 w-12 text-green-500"
                      aria-hidden="true"
                    />
                    <p class="text-gray-600 dark:text-gray-100 text-md">
                      Link Copied!
                      <span class="text-gray-800 dark:text-white font-bold">
                      </span>
                    </p>
                    <div class="flex items-center justify-between">
                      <button
                        type="button"
                        class="
                          p-1
                          bg-indigo-500
                          hover:bg-indigo-700
                          focus:ring-indigo-500 focus:ring-offset-indigo-200
                          text-white
                          transition
                          ease-in
                          duration-200
                          text-center text-base
                          font-semibold
                          shadow-md
                          focus:outline-none
                          focus:ring-2 focus:ring-offset-2
                          rounded-lg
                        "
                      >
                        <XIcon class="block h-6 w-6" aria-hidden="true" />
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
  </div>
</template>

<script>
import {
  TransitionRoot,
  TransitionChild,
  Dialog,
  DialogOverlay,
} from '@headlessui/vue'

import { CheckIcon, XIcon } from '@heroicons/vue/outline'

import { useStore } from 'vuex'
import { ref, computed } from 'vue'

export default {
  components: {
    TransitionRoot,
    TransitionChild,
    Dialog,
    DialogOverlay,
    CheckIcon,
    XIcon,
  },

  setup() {
    const store = useStore()
    const darkMode = computed(() => store.state.settings.darkMode)

    const notiIsOpen = computed(() => store.state.settings.notiIsOpen)

    return {
      darkMode,
      notiIsOpen,
      closeModal() {
        store.commit('SET_NOTI_DIALOG', false)
      },
    }
  },
}
</script>
