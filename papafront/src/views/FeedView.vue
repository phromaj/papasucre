<template lang="">
  <div>
    <Header :user="user" />
    <Tinder :user="user" />
  </div>
</template>
<script>
import { useAuthStore } from "../stores/authStore.js";

import Tinder from "@/components/TinderComponent.vue"
import Header from "@/components/Header.vue"
import { useRouter, useRoute } from 'vue-router'



export default {
   setup() {
        // instancie le store
        const authStore = useAuthStore();
        const user = authStore.$state.user
        return {
            authStore,
            user
        };
    },
 
  name: "FeedView",
  components: {
    Tinder,
    Header
  },
 



};
</script>
<style lang=""></style>
