import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "login",
      component: () => import("../views/LoginView.vue"),
    },
    {
      path: "/feed",
      name: "feed",
      component: () => import("../views/FeedView.vue"),
    },
    {
      path: "/signup",
      name: "signUpMail",
      component: () => import("../views/SignUpMailView.vue"),
    },
    {
      path: "/signup-info",
      name: "signupinfo",
      component: () => import("../views/SignUpInfoView.vue"),
    },
    {
      path: "/signup-profile",
      name: "signinprofile",
      component: () => import("../views/SignUpProfileView.vue"),
    },
    {
      path: "/signin",
      name: "signin",
      component: () => import("../views/SignInView.vue"),
    },
    {
      path: "/docUpload",
      name: "docupload",
      component: () => import("../views/SignUpDocUpload.vue"),
    },
    {
      path: "/upload-profile-pic",
      name: "UploadProfilePic",
      component: () => import("../views/SignUpUploadProfile.vue"),
    },
    {
      path: "/profile",
      name: "profile",
      component: () => import("../views/ProfileView.vue"),
    },
  ],
});

export default router;
