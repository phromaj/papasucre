<template lang="">
  <div>
    <Header />
    <Tinder />

  </div>
</template>
<script>
import Tinder from "@/components/TinderComponent.vue"
import Header from "@/components/HeaderComponent.vue"


export default {
  name: "FeedView",
  components: {
    Tinder,
    Header
  },
};
</script>
<style lang=""></style>
