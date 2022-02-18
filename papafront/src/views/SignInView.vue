
<template>
  <div class="SignInPage">
    <img id="logo" src="../assets/papasucre.png" alt="papasucre-logo" />
    <div class="signIn">
      <form @submit.prevent="submitForm">
        <p id="connect">Connexion</p>
        <div class="email">
          <input
            :type="typeEmail"
            name="email"
            class="input emailInput"
            v-model="email"
            maxlength="30"
            placeholder="Email"
          />
        </div>
        <div class="password">
          <input
            :type="typePwd"
            name="password"
            class="input pwdInput"
            v-model="password"
            maxlength="12"
            placeholder="Mot de Passe"
          />
          <button class="togglePwd" @click="togglePassword">
            <Icon icon="ant-design:eye-filled" color="white" width="25" height="25" />
          </button>
        </div>
        <div id="pwdForget">
          <a href>
            <p>Mot de passe oublié ?</p>
          </a>
        </div>
        <div id="loginButton">
          <button type="submit" id="buttonConnect">Connexion</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
// Import stores
import { useAuthStore } from "../stores/authStore.js";
import { Icon } from "@iconify/vue";

export default {
  setup() {
    // instancie le store
    const auth = useAuthStore();
    return {
      auth,
    };
  },
  components: {
    Icon,
  },

  data() {
    return {
      email: "",
      password: "",
      typeEmail: "email",
      typePwd: "password",
    };
  },

  methods: {
    
    togglePassword() {
      if (this.type === "password") {
        this.type = "text";
      } else {
        this.type = "password";
      }
    },
    async submitForm() {
      let user = {
        email: this.email,
        password: this.password,
      }
      //this.auth.user.email = this.mail
      //this.auth.user.password = this.password
      try {
        await this.auth.login(user)
        await this.auth.authenticate(user.email)


      } catch (error) {
        alert("Vos identifiants sont incorrects")
      }
      this.$router.push('/feed')
    }
  },
};
</script>

<style scoped>
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
  margin-bottom: 1em;
}

#logo {
  width: 17em;
  margin: 2em auto;
}

.email,
.password {
  width: 70%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: 0 auto 2em auto;
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

.togglePwd {
  position: absolute;
  left: 88%;
  top: 18%;
  border: 1px solid transparent;
  background-color: transparent;
}
.togglePwd:focus {
  outline: none;
}

#pwdForget {
  text-align: center;
  height: 3em;
}

#pwdForget a {
  color: #fff;
}

#loginButton {
  display: flex;
  justify-content: center;
  margin-bottom: 2em;
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
