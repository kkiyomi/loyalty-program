<template>
  <div>
    <div
      class="
        max-w-4xl
        py-3
        px-1
        sm:p-6
        mx-auto
        bg-white
        rounded-md
        shadow-md
        dark:bg-gray-800
      "
    >
      <h2
        class="text-lg font-semibold text-gray-700 capitalize dark:text-white"
      >
        Add Promo
      </h2>

      <div>
        <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-2">
          <div>
            <label class="text-gray-700 dark:text-gray-200" for="title">
              Title
            </label>
            <input
              id="title"
              v-model="data.title"
              type="text"
              class="
                block
                w-full
                px-4
                py-2
                mt-2
                text-gray-700
                bg-white
                border border-gray-300
                rounded-md
                dark:bg-gray-800
                dark:text-gray-300
                dark:border-gray-600
                focus:border-blue-500
                dark:focus:border-blue-500
                focus:outline-none
                focus:ring
              "
            />
          </div>

          <div>
            <label class="text-gray-700 dark:text-gray-200" for="size">
              Size
            </label>
            <input
              id="size"
              v-model="data.size"
              type="text"
              class="
                block
                w-full
                px-4
                py-2
                mt-2
                text-gray-700
                bg-white
                border border-gray-300
                rounded-md
                dark:bg-gray-800
                dark:text-gray-300
                dark:border-gray-600
                focus:border-blue-500
                dark:focus:border-blue-500
                focus:outline-none
                focus:ring
              "
            />
          </div>

          <div class="sm:col-span-2">
            <label class="text-gray-700 dark:text-gray-200" for="description">
              Description
            </label>
            <textarea
              id="description"
              v-model="data.description"
              type="email"
              class="
                block
                w-full
                h-30
                px-4
                py-2
                mt-2
                text-gray-700
                bg-white
                border border-gray-300
                rounded-md
                dark:bg-gray-800
                dark:text-gray-300
                dark:border-gray-600
                focus:border-blue-500
                dark:focus:border-blue-500
                focus:outline-none
                focus:ring
              "
            />
          </div>
        </div>

        <div class="flex justify-end mt-6">
          <button
            @click="AddPromo(data)"
            class="
              px-6
              py-2
              leading-5
              text-white
              transition-colors
              duration-200
              transform
              bg-gray-700
              rounded-md
              hover:bg-gray-600
              focus:outline-none
              focus:bg-gray-600
            "
          >
            Save
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { reactive } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'PromoForm',
  setup() {
    const store = useStore()

    const data = reactive({
      title: 'N/A',
      description: 'N/A',
      size: 1,
    })
    const AddPromo = async (promo_data) => {
      await store.dispatch('AddPromo', promo_data)
    }
    return {
      data,
      AddPromo,
    }
  },
}
</script>