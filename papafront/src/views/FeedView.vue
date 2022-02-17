<template lang="">
  <div>
    <Header />
    <Tinder />

  </div>
</template>
<script>
import { useAuthStore } from "../stores/authStore.js";

import Tinder from "@/components/TinderComponent.vue"
import Header from "@/components/Header.vue"
import { useRouter, useRoute } from 'vue-router'



export default {
 
  name: "FeedView",
  components: {
    Tinder,
    Header
  },
 



};
</script>
<style lang=""></style>
