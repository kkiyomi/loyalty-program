<template>
  <div>
    <button
      @click="openSlide"
      class="flex flex-wrap p-2 mr-4 text-white bg-gray-700"
    >
      <PlusIcon class="h-6 w-4" aria-hidden="true" />
      Add
    </button>
    <TransitionRoot
      appear
      as="template"
      :show="isOpen"
      :class="darkMode ? 'dark' : ''"
      class="z-20"
    >
      <Dialog
        as="div"
        static
        class="fixed inset-0 overflow-hidden"
        @close="isOpen = false"
        :isOpen="isOpen"
      >
        <div class="absolute inset-0 overflow-hidden">
          <TransitionChild
            as="template"
            enter="ease-in-out duration-500"
            enter-from="opacity-0"
            enter-to="opacity-100"
            leave="ease-in-out duration-500"
            leave-from="opacity-100"
            leave-to="opacity-0"
          >
            <DialogOverlay
              class="
                absolute
                inset-0
                bg-gray-500 bg-opacity-75
                transition-opacity
              "
            />
          </TransitionChild>
          <div class="fixed inset-y-0 right-0 pl-10 max-w-full flex">
            <TransitionChild
              as="template"
              enter="transform transition ease-in-out duration-500 sm:duration-700"
              enter-from="translate-x-full"
              enter-to="translate-x-0"
              leave="transform transition ease-in-out duration-500 sm:duration-700"
              leave-from="translate-x-0"
              leave-to="translate-x-full"
            >
              <div class="relative w-screen max-w-2xl">
                <TransitionChild
                  as="template"
                  enter="ease-in-out duration-500"
                  enter-from="opacity-0"
                  enter-to="opacity-100"
                  leave="ease-in-out duration-500"
                  leave-from="opacity-100"
                  leave-to="opacity-0"
                >
                  <div
                    class="
                      absolute
                      top-0
                      left-0
                      -ml-8
                      pt-4
                      pr-2
                      flex
                      sm:-ml-10
                      sm:pr-4
                    "
                  >
                    <button
                      class="
                        rounded-md
                        text-gray-300
                        hover:text-white
                        focus:outline-none
                        focus:ring-2 focus:ring-white
                      "
                      @click="isOpen = false"
                    >
                      <span class="sr-only">Close panel</span>
                      <XIcon class="h-6 w-6" aria-hidden="true" />
                    </button>
                  </div>
                </TransitionChild>
                <div
                  class="
                    h-full
                    flex flex-col
                    py-6
                    bg-white
                    shadow-xl
                    overflow-y-scroll
                    dark:bg-gray-700
                  "
                >
                  <div class="mt-6 relative flex-1 px-2 sm:px-6">
                    <PromoForm />
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
  Dialog,
  DialogOverlay,
  TransitionChild,
  TransitionRoot,
} from '@headlessui/vue'
import { XIcon, PlusIcon } from '@heroicons/vue/outline'

import { useStore } from 'vuex'
import { ref, computed } from 'vue'

import PromoForm from './PromoForm.vue'

export default {
  name: 'PromoFormSlide',
  components: {
    Dialog,
    DialogOverlay,
    TransitionChild,
    TransitionRoot,
    XIcon,
    PlusIcon,
    PromoForm,
  },

  setup() {
    const store = useStore()
    const darkMode = computed(() => store.state.user.darkMode)

    const isOpen = ref(false)
    return {
      darkMode,
      isOpen,
      openSlide() {
        isOpen.value = true
      },
    }
  },
}
</script>

