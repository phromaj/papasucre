<script setup>
import { Icon } from '@iconify/vue';

import { RouterLink, RouterView } from "vue-router";
</script>
<template>
    <div>
        <body>
            <div class="signup">
                <div class="logo">
                    <img  src="../assets/PAPASUCRE.png" alt="">
                </div>
                <div class="information" >
                    <h1>Informations complémentaires</h1>
                    <form @submit.prevent="submitForm">
                        <div class="mail">
                            <div class="mailTitle">
                                <h2>Saisissez votre mail</h2>
                            </div>
                            <input type="text" maxlength="30" placeholder="mail@exemple.com">
                        </div>
                        <div class="password">
                            <div class="passwordTitle">
                                <h3>Saisissez votre mot de passe</h3>
                            </div>
                            <input type="text" maxlength="30" placeholder="Entrez votre mot de passe">
                        </div>
                        <div class="verifPassword">
                            <div class="verifPasswordTitle">
                                <h4>Vérifiez votre mot de passe</h4>
                            </div>
                            <input type="text" maxlength="30" placeholder="Entrez votre mot de passe">
                        </div>
                        <div class="continueButton">
                            <RouterLink to="/signup-info" tag="continue">
                                <button class="continue">
                                    <Icon class="icon" icon="" width="20" height="20" rotate="2"/><span>Continuer</span>
                                </button>
                            </RouterLink>
                        </div>
                    </form>
                </div>
            </div>
        </body>
    </div>
</template>
<script>
export default {
    
}
</script>
<style>
    .signup{
        width: 100%;
    }
    body {
        background: linear-gradient(#472709, #241303);
        background-repeat: no-repeat;
        background-position: fixed;
        width: 100%;
    }
    .mailTitle {
        padding-top:3%;
        width: 45%;
        color: rgb(255, 255, 255);
        height: 6em;
        line-height: 1.2;
    }

    .passwordTitle{
        width: 65%;
        color: rgb(255, 255, 255);
        line-height: 1.2;
        padding-top:6%;
        height: 7em;
    }
    .verifPasswordTitle{
        width: 55%;
        color: rgb(255, 255, 255);
        line-height: 1.2;
        padding-top:6%;
        height: 7em;
    }
    .mail{ 
        width: 100%;
    }
    .password{
        padding-top: 6%;
        width: 100%;
    }
    .information{
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
        font-size: 1.2em;
    }
    input::placeholder{
        color: white;
        font-size: 1em;
    }
    input:focus{
        outline: none;
    }
    h2, h3, h4{
        font-size: 24px;
        line-height: 1.3em;
        vertical-align: middle;
    }
    .continueButton{
        width: 100%;
        padding-top: 10%;
        padding-bottom: 10%;
        display: flex;
        justify-content: center;
    }
    .continue{
        cursor: pointer;
        text-decoration: none;
        border: 1px solid #fff;
        border-radius: 20px;
        width: 16em;
        height: 2.5em;
        background-color: #fff;
        font-size: 1.1em;
        line-height: 1.7em;
    }
    .logo{
        padding-top: 5%;
        padding-right: 5%;
        height: 8em;
        display: flex;
        justify-content: right;
        float: right;
    }
</style>