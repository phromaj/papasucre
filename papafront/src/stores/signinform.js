import { defineStore } from "pinia";

export const useSignInForm = defineStore("signinform", {
  state: () => ({
    email: "string",
    password: "string",
  }),
  actions: {
    login() {
      fetch("http://127.0.0.1:8000/user-login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        // pass in the information from our form
        body: JSON.stringify({
          email: this.email,
          password: this.password,
        }),
      });
    },
  },
});
