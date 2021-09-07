<template>
  <div>
    <div class="mt-10 sm:mt-0">
      <div
        class="
          md:grid md:grid-cols-7
          md:gap-6
          bg-white
          dark:bg-gray-900
          shadow
          sm:rounded-md
          px-4
          py-6
        "
      >
        <div class="md:col-span-2 pt-2">
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
              Account
            </h3>
            <p class="mt-1 text-sm text-gray-600 dark:text-gray-300">
              When changing your email, you will need to confirm your new email
              first.
            </p>
          </div>
        </div>

        <div
          class="
            md:col-span-5
            mt-5
            md:mt-0
            overflow-hidden
            sm:rounded-md
            bg-white
            dark:bg-gray-800
          "
        >
          <div class="px-4 py-5 sm:p-6">
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
                    dark:focus:bg-gray-900
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
                    dark:focus:bg-gray-900
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
          <div class="px-4 py-3 text-right sm:px-6">
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
</template>

<script>
export default {
  name: 'Account',
  setup() {},
}
</script>