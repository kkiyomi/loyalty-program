<template>
  <div
    class="
      flex
      items-center
      self-start
      justify-center
      rounded-xl
      bg-gray-50
      py-12
      px-4
      sm:px-6
      lg:px-8
    "
  >
    <div class="max-w-md w-full space-y-8">
      <div>
        <!-- <img
          class="mx-auto h-12 w-auto"
          src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg"
          alt="Workflow"
        /> -->
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Register a new account
        </h2>
      </div>
      <div class="mt-8 space-y-6">
        <input type="hidden" name="remember" value="true" />
        <div class="rounded-md shadow-sm space-y-2">
          <div>
            <label for="email-address" class="sr-only">Email address</label>
            <input
              id="email-address"
              v-model="data.email"
              name="email"
              type="email"
              autocomplete="email"
              required=""
              class="
                appearance-none
                rounded-none
                relative
                block
                w-full
                px-3
                py-2
                border border-gray-300
                placeholder-gray-500
                text-gray-900
                rounded-t-md
                focus:outline-none
                focus:ring-indigo-500
                focus:border-indigo-500
                focus:z-10
                sm:text-sm
              "
              placeholder="Email address"
            />
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input
              id="password"
              v-model="data.password1"
              name="password"
              type="password"
              autocomplete="current-password"
              required=""
              class="
                appearance-none
                rounded-none
                relative
                block
                w-full
                px-3
                py-2
                border border-gray-300
                placeholder-gray-500
                text-gray-900
                rounded-b-md
                focus:outline-none
                focus:ring-indigo-500
                focus:border-indigo-500
                focus:z-10
                sm:text-sm
              "
              placeholder="Password"
            />
          </div>
          <div>
            <label for="password confirmation" class="sr-only">
              Password confirmation
            </label>
            <input
              id="password2"
              v-model="data.password2"
              name="password2"
              type="password"
              autocomplete="current-password"
              required=""
              class="
                appearance-none
                rounded-none
                relative
                block
                w-full
                px-3
                py-2
                border border-gray-300
                placeholder-gray-500
                text-gray-900
                rounded-b-md
                focus:outline-none
                focus:ring-indigo-500
                focus:border-indigo-500
                focus:z-10
                sm:text-sm
              "
              placeholder="Password confirmation"
            />
          </div>
        </div>

        <div>
          <button
            type="submit"
            @click="UserRegister(data)"
            class="
              group
              relative
              w-full
              flex
              justify-center
              py-2
              px-4
              border border-transparent
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
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
              <LockClosedIcon
                class="h-5 w-5 text-indigo-500 group-hover:text-indigo-400"
                aria-hidden="true"
              />
            </span>
            Sign up
          </button>
        </div>
      </div>
      <div>
        <p class="text-sm text-center sm:px-6 text-coolGray-400">
          Already have an account?
          <a href="#" class="underline text-coolGray-600">Sign in</a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { LockClosedIcon } from '@heroicons/vue/solid'
import { reactive } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'Signin',
  components: {
    LockClosedIcon,
  },
  setup() {
    const store = useStore()

    const data = reactive({
      email: '',
      password1: '',
      password2: '',
    })
    const UserRegister = (data) => store.dispatch('UserRegister', data)

    return {
      data,
      UserRegister,
    }
  },
}
</script>