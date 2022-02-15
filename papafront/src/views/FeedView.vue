<template lang="">
  <div>
    <Header />
    <Tinder />

  </div>
</template>
<script>
import Tinder from "@/components/TinderComponent.vue"
import Header from "@/components/Header.vue"


export default {
  name: "FeedView",
  components: {
    Tinder,
    Header
  },
};
</script>
<style lang=""></style>
