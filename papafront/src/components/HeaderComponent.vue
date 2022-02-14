<template lang="">
  <div>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </nav>
  </div>
</template>
<script>
 import { RouterLink } from "vue-router";

export default {
  components: {
    RouterLink
  }

};
</script>
<style></style>
