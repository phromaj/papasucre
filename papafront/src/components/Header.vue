<script setup>
import { Icon } from "@iconify/vue";
import { RouterLink } from "vue-router";
</script>

<template lang="">
  <div id="navbar">
    <RouterLink to="/message" tag="message">
      <button class="navbarbtn">
        <Icon
          class="icon"
          icon="ci:message-circle"
          width="25"
          height="25"
        />
      </button>
    </RouterLink>
    <RouterLink to="/profile" tag="profile">
      <button class="navbarbtn">
        <Icon
          class="icon"
          icon="fa-regular:user"
          width="21"
          height="21"
        />
      </button>
    </RouterLink>
    <RouterLink to="/option" tag="option">
      <button class="navbarbtn">
        <Icon
          class="icon"
          icon="ant-design:setting-outlined"
          width="25"
          height="25"
        />
      </button>
    </RouterLink>
  </div>
</template>
<script>
export default {
  
};
</script>
<style scoped>
#navbar{
  padding-top: 3vh;
  padding-bottom: 1vh;
  width: 100%;
  display: flex;
  justify-content: space-evenly;
}
a.RouterLink, .navbarbtn{
  width: 4em;
  height: 4em;
  border-radius: 100%;
  background-color: white;
  border: 1px solid #aaaaaa;
}
  
</style>
