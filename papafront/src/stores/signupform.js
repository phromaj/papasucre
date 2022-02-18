import { defineStore } from "pinia";

export const useSignUpForm = defineStore("signupform", {
  state: () => ({
    name: "string",
    username: "string",
    email: "string",
    password: "string",
    location: "string",
    birth_date: "string",
    age: 0,
    job: "string",
    description: "string",
    interests: ["string"],
    phone_number: "string",
    first_name: "string",
    last_name: "string",
    sex: "string",
    is_verified: false,
    has_subscription: false,
    photo_album: [""],
    profile_picture: "",
    disliked_user_list: [""],
    liked_user_list: [""],
  }),
  actions: {
    postUser() {
      console.log(this.email);
      fetch("https://papasucre.herokuapp.com/users", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        // pass in the information from our form
        body: JSON.stringify({
          name: this.name,
          username: this.username,
          email: this.email,
          password: this.password,
          location: this.location,
          birth_date: new Date(this.birth_date),
          age: this.age,
          job: this.job,
          description: this.description,
          interests: this.interests,
          phone_number: this.phone_number,
          first_name: this.first_name,
          last_name: this.last_name,
          sex: this.sex,
          is_verified: this.is_verified,
          has_subscription: this.has_subscription,
          photo_album: this.photo_album,
          profile_picture: this.profile_picture,
          disliked_user_list: this.disliked_user_list,
          liked_user_list: this.liked_user_list,
        }),
      });
    },
  },
});
