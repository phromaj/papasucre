<template>
    <div class="SignInPage">
        <img id="logo" src="../assets/papasucre.png" alt="papasucre-logo" />
        <div class="signIn">
            <form action="">
                <p id="connect">Connexion</p>
                    <div class="email">
                        <input type="email" name="email" class="input emailInput" v-model="mail" maxlength="30" placeholder="Email">
                        <p>Error</p>
                    </div>
                    <div class="password">
                        <input type="password" name="password" class="input pwdInput" v-model="password" maxlength="20" placeholder="Mot de Passe">
                        <p>Error</p>
                    </div>
                    <div id="pwdForget">
                        <a href=""><p>Mot de passe oublié ?</p></a>
                    </div>
                    <button id="buttonConnect">Connexion</button>
            </form>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
            mail: '',
            password: '',
        }
    }

}
</script>

<style>
    
    .SignInPage {
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    #connect {
        text-align: center;
        color: #fff;
        font-size: 2.1em;
        margin-bottom: 2em;
    }

    #logo {
        width: 17em;
        margin: 2em auto;
    }

    .email, .password {
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        margin-bottom: 2em;
    }

    .email:checked {
        border: 2px solid transparent;
        background-color: transparent;
        border-bottom: 2px solid #fff;
    }

    .input {
        height: 2.5em;
        border: 2px solid transparent;
        background-color: transparent;
        border-bottom: 2px solid #fff;
        font-size: 1.3em;
        color: #fff;
    }

    .input:focus {
        outline: none;
    }

    .input::placeholder {
        color: #fff;
        font-size: 1em;
    }

    #pwdForget {
        text-align: center;
        height: 3em;
    }

    #pwdForget a {
        color: #fff;
    }

    #buttonConnect {
        text-decoration: none;
        border: 1px solid #fff;
        border-radius: 20px;
        width: 18em;
        height: 2.5em;
        background-color: #fff;
        font-size: 1.1em;
    }

</style>