<template>
  <div class="flex flex-wrap">
    <div
      v-for="item in promos"
      :key="item.id"
      class="w-full md:w-4/12 text-black"
    >
      <div class="p-2">
        <div class="p-4 rounded-3xl" :class="style.background">
          <div class="flex items-center justify-b justify-between">
            <span class="text-sm">{{ humanizeDate(item.date_added) }}</span>
            <button>
              <span class="text-sm">Edit</span>
            </button>
          </div>
          <div class="text-center mb-4 mt-5">
            <button class="w-full">
              <p class="text-base font-bold opacity-70">
                {{ item.title }}
              </p>
              <p class="text-sm opacity-70 mt-2">{{ item.description }}</p>
            </button>
          </div>
          <div>
            <p class="text-sm font-bold m-0 flex justify-between">
              Progress
              <span>2/10 customers</span>
            </p>
            <div
              class="w-full h-1 rounded-md overflow-hidden bg-white my-2 mx-0"
            >
              <span
                class="block h-1 rounded-md"
                :style="{ width: style.progress }"
                :class="[style.progressbar]"
              />
            </div>
            <p class="text-right m-0 text-sm font-bold">
              {{ style.progress }}
            </p>
          </div>
          <div class="flex justify-between pt-4 relative">
            <div class="flex items-center">
              <p class="text-sm font-bold m-0 flex">
                {{ item.suid }}
              </p>
            </div>
            <div
              class="text-sm rounded-lg flex flex-shrink-0 py-2 px-4 font-bold"
              :class="style.text"
            >
              size {{ item.size }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useStore } from 'vuex'
import { computed } from 'vue'

const style2 = {
  background: 'bg-yellow-200',
  progressbar: 'bg-yellow-700',
  text: 'text-yellow-600',
  progress: '20%',
}

const style = {
  background: 'bg-gray-200',
  progressbar: 'bg-indigo-700',
  text: 'text-indigo-600',
  progress: '20%',
}

export default {
  name: 'PromoBox',

  setup() {
    const store = useStore()
    const promos = computed(() => store.getters.promos)
    const humanizeDate = (date) => date.split('T')[0]

    return {
      promos,
      humanizeDate,
      style,
    }
  },
}
</script>
