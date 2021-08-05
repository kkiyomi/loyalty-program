<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div>
    <DialogLogin />
    <DialogSignup />
  </div>
</template>

<script>
import DialogLogin from './DialogLogin.vue'
import DialogSignup from './DialogSignup.vue'

export default {
  name: 'HeaderLoginSignup',
  components: { DialogLogin, DialogSignup },
  setup() {},
}
</script>