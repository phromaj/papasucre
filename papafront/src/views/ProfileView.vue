<template>
    <body>
        <RouterLink to="/feed">
            <button class="returnButton">
                <Icon class="icon" icon="eva:arrow-ios-back-outline" color="white" width="28" height="28"/>
                <span>Profil</span> 
            </button>
        </RouterLink>
        <div class="profileHeader">
            <div class="profilePicture">
                <img :src="user.profile_picture" alt="Photo">
            </div>
            <div class="counter">
                <div class="likeCounter">
                    <h2>Likes</h2>
                    <Icon class="icon" icon="bi:heart-fill" color="white" width="20" height="20"/>
                    <span> 000</span>
                </div>
                <div id="separator">

                </div>
                <div class="matchCounter">
                    <h2>Matches</h2>
                    <Icon class="icon" icon="jam:messages-alt-f" color="white" width="28" height="28"/>
                    <span> 000</span>
                </div>
            </div>
        </div>
        <div class="information">
            <div class="nameAndAge">
                <span>{{ this.user.name}}</span><br>
                <span>{{ this.user.age }} ans</span>
            </div>
            <div id="separator">

            </div>
            <div class="jobAndCity">
                <span>{{ this.user.job }}</span><br>
                <span>{{ this.user.location }}</span>
            </div>
        </div>
        <div class="description">
            <p>{{ this.user.description }}</p>
        </div>
    </body>
</template>
<script>
import { useAuthStore } from "../stores/authStore.js";
import { Icon } from "@iconify/vue";
import { RouterLink } from "vue-router";
export default {
    setup() {
        // instancie le store
        const authStore = useAuthStore();
        const user = authStore.$state.user
        console.log(user)
        return {
            authStore,
            user
        };
    },
    components: {
        Icon,
        RouterLink
    }

}
</script>
<style scoped>
    body{
        padding-left: 5%;
        padding-right: 5%;
        margin-top: 4%;
        margin-bottom: 3%;
    }
    h2{
        text-decoration: underline 1px solid #BF9835;
        text-underline-offset: 0.5rem;
        margin-bottom: 5px;
    }
    .icon{
        vertical-align: middle;
    }
    a.RouterLink, button {
        text-decoration: none;
        background-color: transparent;
        border: transparent;
        color: white;
        font-size: 1.5em;
        line-height: 1.9em;
    }
    .profileHeader{
        width: 100%;
        height: 10em;
        margin-top: 5%;
        display: flex;
        justify-content: space-around;
        align-items: center;
    }
    .profilePicture{
        justify-content: center; 
        width: 33vw;
        height:15vh;
        border-radius: 100%;
        border: 2.5px solid #BF9835;
    }
    img{
        display: flex;
        justify-content: center;
        width: 100%;
        height: 100%;
        border-radius: 100%;
        object-fit: cover;
    }
    .counter{
        height: 4.5em;
        width: 50%;
        display: flex;
        justify-content: space-around;
        vertical-align:middle;
    }
    #separator{
        width: 2px;
        border: 1px solid #BF9835;
        margin: 0px 10px;

    }
    .likeCounter, .matchCounter{
        color: white;
    }


    .information{
        margin-top: 5%;
        height: 4.5em;
        width: 100%;
        display: flex;
        justify-content: space-evenly;
        vertical-align:middle;
    }
    .nameAndAge, .jobAndCity{
        font-size: 22px;
        color: white;
    }
    .description{
        color: white;
        font-size: 18px;
        margin-top: 10%;
        padding: 3%;
        width: 100%;
        height: auto;
        border-radius: 30px;
        border: 1px solid #BF9835;
        background: linear-gradient(#472709, #241303b9);

    }

</style>