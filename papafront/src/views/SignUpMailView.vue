<template>
  <div>
    <body>
      <div class="signup">
        <div id="logo">
          <img src="../assets/PAPASUCRE.png" alt="papasucre-logo" />
        </div>
        <div class="information">
          <h1>Informations <br>Personnelles</h1>
          <form @submit.prevent="submitForm">
            <div class="container">
              <div class="mail">
                <div class="mailTitle">
                  <h2>Saisissez votre mail</h2>
                </div>

                <input
                  v-model="email"
                  type="mail"
                  maxlength="20"
                  placeholder="mail@exemple.com"
                />
                <Icon id="mailIcon" icon="ant-design:mail-outlined" color="white" width="25" height="25" />
              </div>
              <small
                class="error"
                v-for="(error, index) of v$.email.$errors"
                :key="index"
                >{{ error.$message }}</small
              >
            </div>
            
            <div class="container containPwd">
              <div class="password">
                <div class="passwordTitle">
                  <h2>Saisissez votre mot de passe</h2>
                </div>
                <input
                  v-model="password"
                  :type="typePwd"
                  maxlength="12"
                  placeholder="Mot de passe"
                />
                <button class="togglePwd" @click="togglePassword">
                    <Icon icon="ant-design:eye-filled" color="white" width="25" height="25" />
                </button>
              </div>
              <small
                class="error"
                v-for="(error, index) of v$.password.$errors"
                :key="index"
                >{{ error.$message }}</small
              >
            </div>
            <div class="container">
              <div class="verifPassword">
                <div class="verifPasswordTitle">
                  <h2>Vérifiez votre mot de passe</h2>
                </div>
                <input
                  v-model="password_verif"
                  :type="typePwdCheck"
                  maxlength="12"
                  placeholder="Mot de passe"
                />
                <button class="togglePwd" @click="togglePasswordCheck">
                    <Icon icon="ant-design:eye-filled" color="white" width="25" height="25" />
                </button>
              </div>
              <small
                class="error"
                v-for="(error, index) of v$.password_verif.$errors"
                :key="index"
                >{{ error.$message }}</small
              >
            </div>
            
            <div class="continueButton">
              <button type="submit" class="continue">
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
import useVuelidate from "@vuelidate/core";
import { required, email, sameAs, minLength, maxLength, helpers} from "@vuelidate/validators";
import { useSignUpForm } from "../stores/signupform";
import { Icon } from "@iconify/vue";



export default {
  components: {
    Icon,
  },

  setup() {
    // instancie le store
    const store = useSignUpForm();
    return {
      v$: useVuelidate(),
      store,
    };
  },
  data() {
    return {
      email: "",
      password: "",
      password_verif: "",
      typePwd: 'password',
      typePwdCheck: 'password',
    };
  },
  methods: {

    togglePassword() {
      if(this.typePwd === 'password') {
        this.typePwd = 'text';
      } else {
        this.typePwd = 'password';
      }
    },

    togglePasswordCheck() {
      if(this.typePwdCheck === 'password') {
        this.typePwdCheck = 'text';
      } else {
        this.typePwdCheck = 'password';
      }
    },

    // submit the form to our backend api
    submitForm() {
      this.v$.$touch();
      if (this.v$.$error) return;
      // complète l'utilisateur dans le store au fur et au mesure
      this.store.$patch((state) => {
        (state.email = this.email), (state.password = this.password);
      });
      console.log(this.store.$state);
      // methode pour poster un utilisateur dans l'api
      this.$router.push("/signup-info");
    },
  },
  validations() {
    return {
      email: {
        required: helpers.withMessage('Veuillez renseigner un email', required),
        email: helpers.withMessage(
          ({}) => `Veuillez renseignez un email correct.`,
            email,
          ),
          
      },
      password: {
        required: helpers.withMessage('Veuillez renseigner un mot de passe', required),
        minLength: helpers.withMessage(
          ({
            $params
          }) => `Le mot de passe doit contenir au minimum ${$params.min} caractères.`,
          minLength(8),
          ),
        },
      password_verif: {
        //required: helpers.withMessage('Veuillez renseignez à nouveau votre mot de passe.', required),
        sameAsPassword: helpers.withMessage(
          ({}) => `Le mot de passe doit correspondre à celui créer.`,
          sameAs(this.password),
          )
      }
    };
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
  width: 98%;
  margin-top: 1rem;
  margin-right: 3rem;
  display: flex;
  justify-content: flex-end;
}

#logo img {
  width: 70px;
  height: 70px;
}

.container {
  height: 10em;
}

.containPwd {
  height: 11em;
}
.mailTitle {
  padding-top: 3%;
  width: 45%;
  color: rgb(255, 255, 255);
  height: 6em;
  line-height: 1.2;
}

#mailIcon {
  position: relative;
  right: 7%;
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
  width: 100%;
  
}

.togglePwd {
  position: relative;
  right: 8%;
  border: 1px solid transparent;
  background-color: transparent;
}
.information {
  width: 100%;
  padding-top: 2%;
  color: rgb(255, 255, 255);
  padding: 0 4%;
}
.error {
  color: red;
  font-size: 0.95em;
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
