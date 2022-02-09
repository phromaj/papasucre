<script setup lang="ts">
import { Icon } from '@iconify/vue';
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
        <input type="text" placeholder="Nom Prénom">
        <p>Voici comment il apparaîtra sur PapaSucré. Attention, tu ne pourras pas le modifier</p>
        <div id="gender">
          <H1>Je suis un-e</H1>
          <div class="selectGender">
            <button id="male">
              <Icon icon="mdi:gender-male" color="#2d2d2d" />
            </button>
            <button id="female">
              <Icon icon="carbon:gender-female" color="#2d2d2d" />
            </button>
          </div>
        </div>
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
  height: 7em;
}
#information{
  width: 100%;
  padding-left: 5%;
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
  width: 70%;
  color: #8D8D8D;
  padding-top: 2%;
}
#gender{
  width: 50%;
  color: rgb(255, 255, 255);
  height: 7em;
  padding-top: 3%
}
.selectGender{
  width: 100%;
  padding-left: 10%;
  
  display: flex;
  justify-content: space-evenly;
}
#male, #female{
  width: 5em;
  height: 5em;
  border-radius: 100%;
  background-color: white;
  border: 3px solid #713A0B;

}

#logo{
  width: 100%;
  height: 8em;
  display: flex;
  justify-content: right;
}
img{
  padding-right: 10%;
  width: 10em;
  height: 8em;
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