<template>
  <body>
    <div class="signin">
      <div id="logo">
        <img src="../assets/papasucre.png" alt="papasucre-logo" />
      </div>
      <div id="information">
        <div id="title">
          <h1>Mes informations</h1>
        </div>
        <form @submit.prevent="submitForm">
          <div class="container">
            <div class="inputName">
              <input
                class="text-input"
                v-model="name"
                type="text"
                maxlength="20"
                placeholder="Nom Prénom"
              />
              <div>
                <small
                  class="error"
                  v-for="(error, index) of v$.name.$errors"
                  :key="index"
                  >{{ error.$message }}</small
                >
              </div>
            </div>
          </div>
          <p>
            Voici comment il apparaîtra sur PapaSucré. Attention, tu ne pourras
            pas le modifier.
          </p>
          <div id="gender">
            <h2>Je suis un-e</h2>
            <div class="selectGender">
              <input
                :class="{ active: maleActive }"
                type="button"
                @click="getButtonValue"
                value="male"
                id="male"
                autocomplete="off"
              />
              <input
                :class="{ active: femaleActive }"
                type="button"
                @click="getButtonValue"
                value="female"
                id="female"
              />
            </div>
            <div>
              <small
                class="error genderError"
                v-for="(error, index) of v$.sex.$errors"
                :key="index"
                >{{ error.$message }}</small
              >
            </div>
          </div>
          <div class="containerBirth">
            <div id="birth">
              <div id="birthTitle">
                <h2>Date d'anniversaire</h2>
              </div>
              <span class="datepicker-toggle">
                <span class="datepicker-toggle-button"></span>
                <input
                  type="date"
                  class="datepicker-input"
                  v-model="birth_date"
                />
              </span>
            </div>
            <div>
              <small
                class="error"
                v-for="(error, index) of v$.birth_date.$errors"
                :key="index"
                >{{ error.$message }}</small
              >
            </div>
          </div>

          <p>Votre âge sera visible par tous.</p>
          <div id="continueButton">
            <button type="submit" id="continue">Continuer</button>
          </div>
        </form>
      </div>
    </div>
  </body>
</template>

<script>
import { useSignUpForm } from "../stores/signupform";
import { helpers, minLength, required } from "@vuelidate/validators";
import useVuelidate from "@vuelidate/core";
export default {
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
      name: "",
      sex: "",
      femaleActive: false,
      maleActive: false,
      birth_date: "",
    };
  },
  methods: {
    getButtonValue(event) {
      if (event.target.value == "female") {
        this.femaleActive = true;
        this.maleActive = false;
      } else {
        this.maleActive = true;
        this.femaleActive = false;
      }
      this.sex = event.target.value;
    },
    // submit the form to our backend api
    submitForm() {
      this.v$.$touch();
      if (this.v$.$error) return;
      let user_age =
        new Date().getFullYear() - new Date(this.birth_date).getFullYear();
      // complète l'utilisateur dans le store au fur et au mesure
      this.store.$patch((state) => {
        (state.name = this.name),
          (state.sex = this.sex),
          (state.birth_date = this.birth_date),
          (state.age = user_age);
      });
      console.log(this.store.$state);
      // methode pour poster un utilisateur dans l'api
      //this.store.postUser();
      this.$router.push("/signup-profile");
    },
  },
  validations() {
    return {
      name: {
        required: helpers.withMessage(
          "Veuillez renseignez votre Nom",
          required
        ),
        minLength: helpers.withMessage(
          ({ $params }) =>
            `Votre nom doit comporter au minimum ${$params.min} caractères`,
          minLength(3)
        ),
      },
      sex: {
        required: helpers.withMessage(
          "Veuillez renseignez votre genre",
          required
        ),
      },
      birth_date: {
        required: helpers.withMessage(
          "Veuillez renseignez votre date de naissance",
          required
        ),
      },
      femaleActive: false,
      maleActive: false,
    };
  },
};
</script>

<style scoped>
.signin {
  width: 100%;
}

#title {
  width: 25%;
  color: rgb(255, 255, 255);
  height: 6em;
  line-height: 1.2;
  font-size: 18px;
}

#logo {
  width: 100%;
  margin-top: 1rem;
  display: flex;
  justify-content: flex-end;
}

img {
  width: 70px;
  height: 70px;
  margin-right: 1rem;
}

.inputName {
  height: 3.2em;
}

.error {
  color: red;
  font-size: 0.95em;
}

input[type="button"] {
  cursor: pointer;
  color: transparent;
}
#information {
  width: 100%;
  color: rgb(255, 255, 255);
  padding: 2% 4% 0 4%;
}

.container {
  height: 5em;
}
.containerBirth {
  height: 10em;
}
.text-input {
  background-color: transparent;
  border: 1px solid transparent;
  border-bottom: 2px solid rgb(255, 255, 255);
  width: 70%;
  height: 2em;
  margin-bottom: 0.3em;
  color: white;
  font-size: 1.5em;
}
.text-input::placeholder {
  color: white;
  font-size: 1em;
}
.text-input:focus {
  outline: none;
}

p {
  width: 85%;
  color: #8d8d8d;
  height: 3em;
}

#gender {
  width: 100%;
  color: rgb(255, 255, 255);
  height: 12em;
  padding-top: 7%;
}

.genderError {
  width: 100%;
  display: flex;
  justify-content: center;
  margin-top: 0.4em;
}

h2 {
  font-size: 24px;
  line-height: 1.3em;
}
.selectGender {
  width: 100%;
  padding-top: 6%;
  display: flex;
  justify-content: space-evenly;
}

#male,
#female {
  width: 6em;
  height: 6em;
  border-radius: 100%;
  background-color: white;
  border: 3px solid #713a0b;
  justify-content: space-evenly;
}

.active {
  border: 3px solid rgb(211, 162, 0) !important;
}

#male {
  background-color: #ffff;
  background-image: url("https://api.iconify.design/bi/gender-male.svg?width=24&height=24");
  background-repeat: no-repeat;
  background-position: center;
}

#female {
  background-color: #ffff;
  background-image: url("https://api.iconify.design/bi/gender-female.svg?width=24&height=24");
  background-repeat: no-repeat;
  background-position: center;
}

#birth {
  padding: 1% 0;
  width: 100%;
}

#birthTitle {
  width: 45%;
  color: rgb(255, 255, 255);
  height: 5.5em;
}

.datepicker-input {
  position: absolute;
  cursor: pointer;
  box-sizing: border-box;
  background-color: transparent;
  border: 1px solid transparent;
  border-bottom: 2px solid rgb(255, 255, 255);
  width: 85%;
  height: 2em;
  color: white;
  font-size: 1.2em;
  font-family: "Arial";
}

.datepicker-input:focus {
  outline: none;
}

.datepicker-toggle {
  display: inline-block;
  position: relative;
  width: 80%;
  height: 2em;
}
.datepicker-toggle-button {
  position: absolute;
  width: 85%;
  height: 100%;
  background: url("https://api.iconify.design/bx/bx-calendar.svg?color=white")
    no-repeat right center / contain;
}

input[type="date"]::-webkit-calendar-picker-indicator {
  opacity: 0;
  position: absolute;
  left: 0;
  margin: 0;
  padding: 0;
  width: 100%;
  cursor: pointer;
}

button {
  cursor: pointer;
}

#continueButton {
  width: 100%;
  padding-top: 8%;
  padding-bottom: 8%;
  display: flex;
  justify-content: center;
}
/*  Continue Button  */
#continue {
  text-decoration: none;
  border: 1px solid #fff;
  border-radius: 20px;
  width: 18em;
  height: 2.5em;
  background-color: #fff;
  font-size: 1.1em;
  line-height: 1.7em;
}

@media (min-width: 1024px) {
  .signin {
    width: 100%;
    display: flex;
    align-items: center;
  }
}
</style>
