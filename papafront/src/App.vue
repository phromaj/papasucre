<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "@/components/HelloWorld.vue";
</script>

<template>
  <RouterView />
</template>

<style>
@import "@/assets/base.css";

body {
  background: linear-gradient(#472709, #241303);
  background-repeat: no-repeat;
  background-position: fixed;
  width: 100%;
  display: flex;
  justify-content: center;
}
</style>
