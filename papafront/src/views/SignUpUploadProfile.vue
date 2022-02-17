<template lang="">
  <div>
    <UploadPicture />
  </div>
</template>
<script>
import { useSignUpForm } from "../stores/signupform";
import UploadPicture from "@/components/UploadPictureComponent.vue";

export default {
  setup() {
    // instancie le store
    const store = useSignUpForm();
    return {
      store,
    };
  },
  components: {
    UploadPicture,
  },
};
</script>
<style lang=""></style>
