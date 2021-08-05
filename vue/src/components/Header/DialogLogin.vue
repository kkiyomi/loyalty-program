<template>
  <div>
    <div>
      <button
        type="button"
        @click="isOpen = true"
        class="
          whitespace-nowrap
          text-base
          font-medium
          text-gray-500
          hover:text-gray-900
        "
      >
        Sign in
      </button>
    </div>
    <TransitionRoot appear :show="isOpen" as="template">
      <Dialog as="div" @close="closeModal">
        <DialogOverlay class="fixed inset-0 bg-black opacity-70" />
        <div class="fixed inset-0 z-10 overflow-y-auto">
          <div class="min-h-screen md:px-4 text-center">
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
              as="template"
              enter="duration-300 ease-out"
              enter-from="opacity-0 scale-95"
              enter-to="opacity-100 scale-100"
              leave="duration-200 ease-in"
              leave-from="opacity-100 scale-100"
              leave-to="opacity-0 scale-95"
            >
              <div
                class="
                  inline-block
                  w-full
                  max-w-md
                  py-6
                  p-2
                  md:p-6
                  my-8
                  overflow-hidden
                  text-left
                  align-middle
                  transition-all
                  transform
                  bg-white
                  shadow-xl
                  rounded-2xl
                "
              >
                <Signin />
                <div class="text-center sm:text-left whitespace-nowrap">
                  <button
                    class="
                      transition
                      duration-200
                      mx-5
                      px-5
                      py-4
                      cursor-pointer
                      font-normal
                      text-sm
                      rounded-lg
                      text-gray-500
                      hover:bg-gray-200
                      ring-inset
                    "
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      class="w-4 h-4 inline-block align-text-top"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M10 19l-7-7m0 0l7-7m-7 7h18"
                      />
                    </svg>
                    <span class="inline-block ml-1" @click="closeModal">
                      Back
                    </span>
                  </button>
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

import { ref, watch, computed } from 'vue'
import { useStore } from 'vuex'

import Signin from './Login.vue'

export default {
  name: 'DialogLogin',
  components: {
    TransitionRoot,
    TransitionChild,
    Dialog,
    DialogOverlay,
    Signin,
  },

  setup() {
    const isOpen = ref(false)

    const store = useStore()
    const token = computed(() => store.state.user.token)

    const closeModal = () => {
      isOpen.value = false
    }

    watch(token, (currentValue, oldValue) => {
      if (token.value != null) {
        closeModal()
      }
    })

    return {
      isOpen,
      closeModal,
    }
  },
}
</script>
