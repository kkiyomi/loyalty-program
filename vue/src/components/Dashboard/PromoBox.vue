<template>
  <div class="p-2 h-full text-black">
    <div class="p-4 rounded-3xl h-full" :class="style.background">
      <div class="flex items-center justify-b justify-between">
        <span class="text-sm">{{ humanizeDate(item.date_added) }}</span>
        <div v-if="promoEditing == item.uid">
          <button
            v-if="promoEditing == item.uid"
            @click="PatchPromo(promo_data)"
            class="
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
            Save
          </button>
          <button
            v-if="promoEditing == item.uid"
            @click="stopPromoEdit"
            class="
              px-3
              py-2
              ml-2
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
            Cancel
          </button>
        </div>

        <PromoEditMenu v-else :promo="item" />
      </div>
      <div
        class="text-center"
        :class="promoEditing == item.uid ? 'my-3' : 'mb-4 mt-5'"
      >
        <div
          v-if="promoEditing == item.uid"
          class="flex flex-wrap flex-col items-center w-full"
        >
          <input
            v-model="promo_data.title"
            type="text"
            class="
              block
              h-8
              w-48
              px-4
              py-2
              mt-1
              text-gray-700
              bg-white
              border border-gray-300
              rounded-md
              focus:border-blue-500
              focus:outline-none
              focus:ring
            "
          />
        </div>
        <!-- <button v-else class="w-full">
          <p class="text-base font-bold opacity-70">
            {{ item.title }}
          </p>
        </button> -->
        <router-link
          v-else
          :to="{ name: 'test', params: { promo_uid: item.uid } }"
          custom
          v-slot="{ navigate }"
        >
          <button
            class="text-base hover:bg-indigo-100 p-2 font-bold opacity-70"
            @click="navigate"
          >
            {{ item.title }}
          </button>
        </router-link>
      </div>
      <div>
        <p class="text-sm font-bold m-0 flex justify-between">
          Progress
          <span>{{ item.pi_count }}/{{ item.target }} customers</span>
        </p>
        <div class="w-full h-1 rounded-md overflow-hidden bg-white my-2 mx-0">
          <span
            class="block h-1 rounded-md"
            :style="{ width: item.progress }"
            :class="[style.progressbar]"
          />
        </div>
        <p class="text-right m-0 text-sm font-bold">
          {{ item.progress }}
        </p>
      </div>
      <div class="flex justify-between pt-4 relative">
        <div class="flex items-center">
          <p class="text-sm font-bold m-0 flex">Code {{ item.suid }}</p>
        </div>
        <div v-if="promoEditing == item.uid" class="w-20 z-10">
          <Listbox v-model="selectedSize">
            <div class="relative mt-1">
              <ListboxButton
                class="
                  relative
                  w-full
                  py-2
                  pl-3
                  pr-10
                  text-left
                  bg-white
                  rounded-lg
                  shadow-md
                  cursor-default
                  focus:outline-none
                  focus-visible:ring-2
                  focus-visible:ring-opacity-75
                  focus-visible:ring-white
                  focus-visible:ring-offset-indigo-300
                  focus-visible:ring-offset-2
                  focus-visible:border-indigo-500
                  sm:text-sm
                "
              >
                <span class="block truncate">
                  {{ selectedSize.number }}
                </span>
                <span
                  class="
                    absolute
                    inset-y-0
                    right-0
                    flex
                    items-center
                    pr-2
                    pointer-events-none
                  "
                >
                  <SelectorIcon
                    class="w-5 h-5 text-gray-400"
                    aria-hidden="true"
                  />
                </span>
              </ListboxButton>

              <transition
                leave-active-class="transition duration-100 ease-in"
                leave-from-class="opacity-100"
                leave-to-class="opacity-0"
              >
                <ListboxOptions
                  class="
                    absolute
                    w-full
                    py-1
                    mt-1
                    overflow-auto
                    text-base
                    bg-white
                    rounded-md
                    shadow-lg
                    max-h-60
                    ring-1 ring-black ring-opacity-5
                    focus:outline-none
                    sm:text-sm
                  "
                >
                  <ListboxOption
                    v-slot="{ active, selected }"
                    v-for="person in size"
                    :key="person.number"
                    :value="person"
                    as="template"
                  >
                    <li
                      :class="[
                        active
                          ? 'text-indigo-900 bg-indigo-100'
                          : 'text-gray-900',
                        'cursor-default select-none relative py-2 pl-10 pr-4',
                      ]"
                    >
                      <span
                        :class="[
                          selected ? 'font-medium' : 'font-normal',
                          'block truncate',
                        ]"
                      >
                        {{ person.number }}
                      </span>
                      <span
                        v-if="selected"
                        class="
                          absolute
                          inset-y-0
                          left-0
                          flex
                          items-center
                          pl-3
                          text-indigo-600
                        "
                      >
                        <CheckIcon class="w-5 h-5" aria-hidden="true" />
                      </span>
                    </li>
                  </ListboxOption>
                </ListboxOptions>
              </transition>
            </div>
          </Listbox>
        </div>
        <div
          v-else
          class="text rounded-lg flex flex-shrink-0 py-2 px-4 font-bold"
          :class="style.text"
        >
          Size {{ item.size }}
        </div>
      </div>
      <div>
        <section v-if="promoEditing == item.uid">
          <label class="text-indigo-600 ml-2" for="description">
            Description
          </label>
          <textarea
            v-model="promo_data.description"
            type="text"
            class="
              block
              w-full
              h-30
              px-4
              py-2
              text-gray-700
              bg-white
              text-sm
              border border-gray-300
              rounded-md
              focus:border-blue-500
              focus:outline-none
              focus:ring
            "
          />
        </section>

        <button v-else-if="item.description != 'N/A'" class="w-full">
          <p class="text-sm text-left opacity-70 mt-2">
            {{ item.description }}
          </p>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import {
  Listbox,
  ListboxButton,
  ListboxOptions,
  ListboxOption,
} from '@headlessui/vue'
import { CheckIcon, SelectorIcon } from '@heroicons/vue/solid'

import { useStore } from 'vuex'
import { reactive, ref, computed } from 'vue'

import PromoEditMenu from './PromoEditMenu.vue'

const style2 = {
  background: 'bg-yellow-100',
  progressbar: 'bg-yellow-700',
  text: 'text-yellow-600',
}

const style = {
  background: 'bg-gray-200',
  progressbar: 'bg-indigo-700',
  text: 'text-indigo-600',
}

export default {
  name: 'PromoBox',
  components: {
    PromoEditMenu,
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
    CheckIcon,
    SelectorIcon,
  },

  props: {
    item: {
      type: Object,
      default() {
        return {}
      },
    },
  },
  setup(props) {
    const store = useStore()
    const humanizeDate = (date) => date.split('T')[0]
    const promoEditing = computed(() => store.state.settings.promoEditing)

    const size = [
      { number: 1 },
      { number: 2 },
      { number: 3 },
      { number: 4 },
      { number: 5 },
    ]
    const found = size.find((element) => element.number == props.item.size)
    const selectedSize = ref(found)

    const promo_data = reactive({
      title: props.item.title,
      description:
        props.item.description == 'N/A' ? '' : props.item.description,
      size: props.item.size,
    })

    const PatchPromo = (data) => {
      data.size = selectedSize.value.number
      const vdata = {
        kwargs: props.item.uid,
        data: data,
      }
      store.dispatch('PatchPromo', vdata)
      store.commit('SET_PROMO_EDITING', null)
    }

    return {
      promo_data,
      humanizeDate,
      style,
      promoEditing,
      stopPromoEdit() {
        store.commit('SET_PROMO_EDITING', null)
      },

      size,
      selectedSize,
      PatchPromo,
    }
  },
}
</script>
