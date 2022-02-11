<script setup>
import { Icon } from "@iconify/vue";

import { RouterLink, RouterView } from "vue-router";
</script>
<template>
<div>
    <body>
        <div class="signup">
            <div id="logo">
                <img src="../assets/PAPASUCRE.png" alt="papasucre-logo" />
            </div>
            <div class="information">
                <h1>Informations complémentaires</h1>
                <form @submit.prevent="submitForm">
                    <div class="mail">
                        <div class="mailTitle">
                            <h2>Saisissez votre mail</h2>
                        </div>
                        <input v-model="email"  type="text" maxlength="30" placeholder="mail@exemple.com" />
                    </div>
                    <div class="password">
                        <div class="passwordTitle">
                            <h2>Saisissez votre mot de passe</h2>
                        </div>
                        <input v-model="password" type="text" maxlength="30" placeholder="Entrez votre mot de passe" />
                    </div>
                    <div class="verifPassword">
                        <div class="verifPasswordTitle">
                            <h2>Vérifiez votre mot de passe</h2>
                        </div>
                        <input v-model="password_verif" type="text" maxlength="30" placeholder="Entrez votre mot de passe" />
                    </div>
                    <div class="continueButton">
                        <button type="submit" class="continue">
                            <Icon class="icon" icon width="20" height="20" rotate="2" />
                            <span>Continuer</span>
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </body>
</div>
</template>
<script>
export default {
    data() {
        return {
            email: '',
            password: '',
            password_verif: '', 
            
        };
    },
    methods: {
        // submit the form to our backend api
        async submitForm() {
            console.log(this.email)
            console.log(this.password)
            console.log(this.password_verif)
            this.$router.push("/signup-info");

        },
    },
};
</script>
<style scoped>
.signup {
    width: 100%;
}
body {
    background: linear-gradient(#472709, #241303);
    background-repeat: no-repeat;
    background-position: fixed;
    width: 100%;
}

#logo {
    width: 100%;
    margin-top: 1rem;
    display: flex;
    justify-content: flex-end;
}

#logo img {
    width: 70px;
    height: 70px;
    
}
.mailTitle {
    padding-top: 3%;
    width: 45%;
    color: rgb(255, 255, 255);
    height: 6em;
    line-height: 1.2;
}

.passwordTitle {
    width: 65%;
    color: rgb(255, 255, 255);
    line-height: 1.2;
    padding-top: 6%;
    height: 7em;
}
.verifPasswordTitle {
    width: 55%;
    color: rgb(255, 255, 255);
    line-height: 1.2;
    padding-top: 6%;
    height: 7em;
}
.mail {
    width: 100%;
}
.password {
    padding-top: 6%;
    width: 100%;
}
.information {
    width: 100%;
    padding-top: 2%;
    color: rgb(255, 255, 255);
    padding: 0 4%;
}

input {
    background-color: transparent;
    border: 1px solid transparent;
    border-bottom: 2px solid rgb(255, 255, 255);
    width: 70%;
    height: 2em;
    color: white;
    font-size: 1.2em;
}
input::placeholder {
    color: white;
    font-size: 1em;
}
input:focus {
    outline: none;
}
h2 {
    font-size: 1.5em;
    line-height: 1.3em;
    vertical-align: middle;
}
.continueButton {
    width: 100%;
    padding-top: 10%;
    padding-bottom: 10%;
    display: flex;
    justify-content: center;
}
.continue {
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
</style>