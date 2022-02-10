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
          <H1>Mes informations</H1>
        </div>
        <form action="">
          <input type="text" maxlength="30" placeholder="Nom Prénom">
          <p>Voici comment il apparaîtra sur PapaSucré. Attention, tu ne pourras pas le modifier.</p>
          <div id="gender">
            <H1>Je suis un-e</H1>
            <div class="selectGender">
              <button id="male">
                <Icon class="genderIcon" icon="mdi:gender-male" color="#2d2d2d" width="32" height="32" />
              </button>
              <button id="female">
                <Icon class="genderIcon" icon="mdi:gender-female" color="#2d2d2d" width="32" height="32" />
              </button>
            </div>
          </div>
          <div id="birth">
            <div id="birthTitle">
              <h1>Date de naissance</h1>
            </div>
            <span class="datepicker-toggle">
              <span class="datepicker-toggle-button"></span>
              <input type="date" class="datepicker-input">
            </span>
            <p>Votre âge sera visible par tous.</p>
          </div>
          <div id="continueButton">
            <RouterLink to="/verification" tag="continue">
              <button id="continue">
                <Icon class="icon" icon="" width="20" height="20" rotate="2"/>Continuer
              </button>
            </RouterLink>
          </div>
        </form>
      </div>
    </div>
  </body>
</template>

<style>
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
#information{
  width: 100%;
  padding-top: 30%;
  padding-left: 5%;
  padding-right: 5%;
  color: rgb(255, 255, 255);
}
input{
  background-color: transparent;
  border: 1px solid transparent;
  border-bottom: 2px solid rgb(255, 255, 255);
  width: 70%;
  height: 2em;
  color: white;
  font-size: 1.5em;
}
input::placeholder{
  color: white;
  font-size: 1em;
}
input:focus{
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
.selectGender{
  width: 100%;
  padding-top: 6%;
  
  display: flex;
  justify-content: center;
  justify-content: space-evenly;
  
}
#male, #female{
  width: 5em;
  height: 5em;
  border-radius: 100%;
  background-color: white;
  border: 3px solid #713A0B;
  justify-content: space-evenly;
}

#birth {
  padding-top: 6%;
  width: 100%;
}
#birthTitle {
  width: 45%;
  color: rgb(255, 255, 255);
  height: 7em;
}

.datepicker-input {
  position: absolute;
  width: 100%;
  height: 2em;
  cursor: pointer;
  box-sizing: border-box;
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

#continueButton{
  width: 100%;
  padding-top: 8%;
  padding-bottom: 8%;
  display: flex;
  justify-content: center;

}
a.RouterLink, #continue {
  text-decoration: none;
  border: 1px solid #fff;
  border-radius: 20px;
  width: 100%;
  height: 1.6em;
  background-color: #fff;
  font-size: 1.1em;
  
}

#logo{
  height: 8em;
  display: flex;
  justify-content: right;
  float: right;
}

@media (min-width: 1024px) {
  .signin {
    width: 100%;
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
  
}
</style>