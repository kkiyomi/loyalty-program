<template>
  <div>
    <div class="mt-10 sm:mt-0">
      <div class="md:grid md:grid-cols-8 md:gap-6">
        <div class="md:col-span-2">
          <div class="px-4 sm:px-0">
            <h3
              class="
                text-lg
                font-medium
                leading-6
                text-gray-900
                dark:text-white
              "
            >
              Personal Information
            </h3>
            <p class="mt-1 text-sm text-gray-600 dark:text-gray-300">
              Use a permanent address where you can receive mail.
            </p>
          </div>
        </div>
        <div class="mt-5 md:mt-0 md:col-span-6">
          <div>
            <div class="shadow overflow-hidden sm:rounded-md">
              <div class="px-4 py-5 bg-white dark:bg-gray-800 sm:p-6">
                <div class="grid grid-cols-6 gap-6">
                  <div class="col-span-6 sm:col-span-3">
                    <label
                      for="Username"
                      class="
                        block
                        text-sm
                        font-medium
                        text-gray-700
                        dark:text-gray-200
                      "
                    >
                      Username
                    </label>
                    <input
                      type="text"
                      name="Username"
                      id="Username"
                      autocomplete="Username"
                      class="
                        mt-1
                        focus:ring-indigo-500
                        focus:border-indigo-500
                        block
                        w-full
                        shadow-sm
                        sm:text-sm
                        border-gray-300
                        rounded-md
                        dark:bg-gray-800
                        dark:text-gray-300
                        dark:border-gray-600
                      "
                    />
                  </div>

                  <div class="col-span-6 sm:col-span-4">
                    <label
                      for="email-address"
                      class="
                        block
                        text-sm
                        font-medium
                        text-gray-700
                        dark:text-gray-200
                      "
                    >
                      Email address
                    </label>
                    <input
                      type="text"
                      name="email-address"
                      id="email-address"
                      autocomplete="email"
                      class="
                        mt-1
                        focus:ring-indigo-500
                        focus:border-indigo-500
                        block
                        w-full
                        shadow-sm
                        sm:text-sm
                        border-gray-300
                        rounded-md
                        dark:bg-gray-800
                        dark:text-gray-300
                        dark:border-gray-600
                      "
                    />
                  </div>
                </div>
              </div>
              <div
                class="
                  px-4
                  py-3
                  bg-gray-50
                  dark:bg-gray-800
                  dark:border-t dark:border-gray-700
                  text-right
                  sm:px-6
                "
              >
                <button
                  type="submit"
                  class="
                    inline-flex
                    justify-center
                    py-2
                    px-4
                    border border-transparent
                    shadow-sm
                    text-sm
                    font-medium
                    rounded-md
                    text-white
                    bg-indigo-600
                    hover:bg-indigo-700
                    focus:outline-none
                    focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500
                  "
                >
                  Save
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Account',
  setup() {},
}
</script>