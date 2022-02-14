<script setup>
import { Icon } from "@iconify/vue";
import { RouterLink } from "vue-router";
</script>

<template>
  <div class="firstPage">
    <img id="logo" src="../assets/papasucre.png" alt="papasucre-logo" />
    <div class="buttonDiv">
      <div class="signUp">
        <RouterLink to="/signin" tag="signin">
          <button>
            <Icon
              class="icon"
              icon="tabler:login"
              width="30"
              height="30"
              rotate="2"
            />Se Connecter
          </button>
        </RouterLink>
      </div>
      <div class="signIn">
        <RouterLink to="/signup" tag="signup">
          <button>
            <Icon
              class="icon"
              icon="akar-icons:google-fill"
              width="25"
              height="25"
            />S'inscrire avec Google
          </button>
        </RouterLink>
        <RouterLink to="/" tag="signup">
          <button>
            <Icon
              class="icon"
              icon="bi:facebook"
              width="25"
              height="25"
            />S'inscrire avec Facebook
          </button>
        </RouterLink>
        <RouterLink to="/" tag="signin">
          <button>
            <Icon
              class="icon"
              icon="ci:message-circle"
              width="28"
              height="28"
            />S'inscrire avec N° de tél.
          </button>
        </RouterLink>
      </div>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style scoped>
.firstPage {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

#logo {
  width: 17em;
  margin: 2em auto;
}

a {
  width: 100%;
  display: flex;
  justify-content: center;
  text-decoration: none;
}

a.RouterLink,
button {
  text-decoration: none;
  border: 1px solid #fff;
  border-radius: 20px;
  width: 18em;
  height: 2.5em;
  background-color: #fff;
  font-size: 1.1em;
  line-height: 1.7em;
}

.login {
  float: left;
  line-height: 2em;
  width: 40%;
}

.buttonDiv {
  margin-top: 2em;
}

.signUp {
  display: flex;
  justify-content: center;
  margin-bottom: 5em;
}

.signIn {
  display: grid;
  place-items: center;
  gap: 1.5em;
}

.icon {
  float: left;
  size: 2em;
}

@media (min-width: 320px) and (max-width: 1000px) {
  body {
    display: flex;
    place-items: center;
    width: 100%;
  }

  .firstPage {
    width: 100%;
  }

  #logo {
    width: 17em;
    margin: 2rem auto;
  }

  .buttonDiv {
    margin-top: 2em;
  }

  a {
    width: 100%;
    display: flex;
    justify-content: center;
    text-decoration: none;
  }

  a.RouterLink,
  button {
    text-decoration: none;
    border: 1px solid #fff;
    border-radius: 20px;
    width: 18em;
    height: 2.5em;
    background-color: #fff;
    font-size: 1.1em;
    line-height: 1.7em;
    transition: 0.4s;
  }

  button:focus {
    border: 1px solid #472709;
    color: rgb(211, 162, 0);
    background-color: #472709;
  }

  .login {
    float: left;
    line-height: 2em;
    width: 40%;
  }

  button {
    cursor: pointer;
  }

  .buttonDiv {
    display: row;
  }

  .signUp {
    display: flex;
    justify-content: center;
    margin-bottom: 5em;
  }

  .signIn {
    display: grid;
    place-items: center;
    gap: 1.5em;
  }

  .icon {
    float: left;
    size: 2em;
  }
}

@media (max-width: 320px) {
  #logo {
    width: 15em;
    margin-top: 2em;
  }

  a.RouterLink,
  button {
    text-decoration: none;
    border: 1px solid #fff;
    border-radius: 20px;
    width: 15em;
    height: 2.5em;
    background-color: #fff;
    font-size: 1em;
    line-height: 1.7em;
  }

  .buttonDiv {
    margin-top: 4em;
  }
}

@media (hover: hover) {
  a:hover {
    background-color: hsla(160, 100%, 37%, 0.2);
  }
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  body {
    display: flex;
    place-items: center;
  }

  #app {
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 0 2rem;
  }

  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  .logo {
    margin: 0 5rem 0 0;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
