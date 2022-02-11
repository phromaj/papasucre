<script setup>
import { Icon } from '@iconify/vue';

import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <body>
    <div class="signin">
      <div id="logo">
        <img  src="../assets/PAPASUCRE.png" alt="">
      </div>
      <div id="information" >
        <div id="title">
          <h1>Mes informations</h1>
        </div>
        <form @submit.prevent="submitForm">
          <input class="text-input" v-model="full_name" type="text" maxlength="30" placeholder="Nom Prénom">
          <p>Voici comment il apparaîtra sur PapaSucré. Attention, tu ne pourras pas le modifier.</p>
          <div id="gender">
            <h2>Je suis un-e</h2>
            <div class="selectGender">
              <input :class="{ active: maleActive }" type="button" @click="getButtonValue" value="male" id="male" autocomplete="off">
              <input :class="{ active: femaleActive }" type="button" @click="getButtonValue" value="female" id="female">
                <!--<Icon  value="female" class="genderIcon" icon="mdi:gender-female" color="#2d2d2d" width="32" height="32" />-->
            </div>
          </div>
          <div id="birth">
            <div id="birthTitle">
              <h2>Date d'anniversaire</h2>
            </div>
            <span class="datepicker-toggle">
              <span class="datepicker-toggle-button"></span>
              <input type="date" class="datepicker-input" v-model="user_birthdate">
            </span>
            <p>Votre âge sera visible par tous.</p>
          </div>
          <div id="continueButton">
              <button type="submit" id="continue">
                <Icon class="icon" icon="" width="20" height="20" rotate="2"/><span>Continuer</span>
              </button>
          </div>
        </form>
      </div>
    </div>
  </body>
</template>

<script>

export default {
  data() {
    return {
      full_name: '',
      email: '',
      password: '',
      gender: '',
      user_birthdate: '',
      femaleActive: false,
      maleActive: false,
    }
  },
  methods: {
    getButtonValue(event){
      if(event.target.value == "female"){
        this.femaleActive = true
        this.maleActive = false

      }
      else {
        this.maleActive = true;
        this.femaleActive = false
      }
      this.gender = event.target.value
    }, 
    toggleAndChooseGender(){
    },
    // submit the form to our backend api
    async submitForm() {

      const res = await fetch('http://127.0.0.1:8000/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },

        // pass in the information from our form
        body: JSON.stringify({
          name: this.full_name,
          username: "string",
          email: "string",
          password: "string",
          location: "string",
          birth_date: new Date(this.user_birthdate),
          age: 0,
          job: "string",
          phone_number: "string",
          sex: this.gender,
          
        }) 
      });

    } 
  }
}  

</script>

<style scoped>
.signin{
  width: 100%;
}
body {
  background: linear-gradient(#472709, #241303);
  background-repeat: no-repeat;
  background-position: fixed;
  width: 100%;
}
#title {
  width: 25%;
  color: rgb(255, 255, 255);
  height: 6em;
  line-height: 1.2;
  font-size: 18px;
}
input[type="button"]{
  cursor: pointer;
  color: transparent;
}
#information{
  width: 100%;
  padding-top: 10px;
  padding-left: 8%;
  padding-right: 8%;
  color: rgb(255, 255, 255);
}


.text-input{
  background-color: transparent;
  border: 1px solid transparent;
  border-bottom: 2px solid rgb(255, 255, 255);
  width: 70%;
  height: 2em;
  color: white;
  font-size: 1.5em;
}
.text-input::placeholder{
  color: white;
  font-size: 1em;
}
.text-input:focus{
  outline: none;
}
p{
  width: 85%;
  color: #8D8D8D;
  padding-top: 2%;
}
#gender{
  width: 100%;
  color: rgb(255, 255, 255);
  height: 10em;
  padding-top: 4%;
  
}
h2{
  font-size: 24px;
  line-height: 1.3em;
}
.selectGender{
  width: 100%;
  padding-top: 6%;
  
  display: flex;
  justify-content: center;
  justify-content: space-evenly;
  
}
#male, #female{
  width: 6em;
  height: 6em;
  border-radius: 100%;
  background-color: white;
  border: 3px solid #713A0B;
  justify-content: space-evenly;
}

#male {
  background-color: #FFFF;
  background-image: url('https://api.iconify.design/bi/gender-male.svg?width=24&height=24');
  background-repeat: no-repeat;
  background-position: center;
}

#female {
  background-color: #FFFF;
  background-image:  url('https://api.iconify.design/bi/gender-female.svg?width=24&height=24');
  background-repeat: no-repeat;
  background-position: center;
}

#birth {
  padding-top: 6%;
  width: 100%;
  padding-bottom: 2px;
}
#birthTitle {
  width: 45%;
  color: rgb(255, 255, 255);
}

.datepicker-input {
  position: absolute;
  cursor: pointer;
  box-sizing: border-box;
  background-color: transparent;
  border: 1px solid transparent;
  border-bottom: 2px solid rgb(255, 255, 255);
  width: 80%;
  height: 2em;
  color: white;
  font-size: 1.2em;
}

.datepicker-input:focus{
  outline: none;
}

.datepicker-toggle {
  display: inline-block;
  position: relative;
  width: 70%;
  height: 2em;
}
.datepicker-toggle-button {
  position: absolute;
  width: 100%;
  height: 100%;
  background: url('https://api.iconify.design/bx/bx-calendar.svg?color=white') no-repeat right center / contain;
}

input[type="date"]::-webkit-calendar-picker-indicator {
  opacity: 0;
  position: absolute;
  left: 0;
  width: 100%;
  margin: 0;
  padding: 0;
  cursor: pointer;
}

button{
  cursor: pointer;
}

#continueButton{
  width: 100%;
  padding-top: 8%;
  padding-bottom: 8%;
  display: flex;
  justify-content: center;

}
/*  Continue Button  */
#continue{
  text-decoration: none;
  border: 1px solid #fff;
  border-radius: 20px;
  width: 18em;
  height: 2.5em;
  background-color: #fff;
  font-size: 1.1em;
  line-height: 1.7em;
  
}

.active {
  border: 3px solid brown !important;
}

#logo{
  width: 100%;
  margin-top: 1rem;
  display: flex;
  justify-content: flex-end;
}
img {
  width: 70px;
  height: 70px;
  margin-right: 1rem;

  object-fit: cover;
}

@media (min-width: 1024px) {
  .signin {
    width: 100%;
    display: flex;
    align-items: center;
  }
  
}
</style>