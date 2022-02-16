<template>
    <div>
        <body>
            <div class="signup">
                <div id="logo">
                    <img src="../assets/PAPASUCRE.png" alt="papasucre-logo" />
                </div>
                <div class="information">
                    <div id="title">
                        <h1>Informations complémentaires</h1>
                    </div>
                    <form @submit.prevent="submitForm">
                        <div class="container">
                            <div class="description">
                                <div class="descriptionTitle">
                                    <h2>Description</h2>
                                </div>
                                <input v-model="description" maxlength="40" type="text" placeholder="centre d'interêts, goûts, ...">
                            </div>
                            <div>
                                <small  class="error"
                                        v-for="(error, index) of v$.description.$errors"
                                        :key="index">
                                        {{ error.$message }}
                                </small>
                            </div>
                        </div>
                        <div class="container">
                            <div class="location">
                                <div class="locationTitle">
                                    <h3>Où habitez-vous</h3>
                                </div>
                                <input v-model="location" type="text" placeholder="Pays / Ville">
                            </div>
                            <div>
                                <small  class="error"
                                        v-for="(error, index) of v$.location.$errors"
                                        :key="index">
                                        {{ error.$message }}
                                </small>
                            </div>
                        </div>
                        <div class="container">
                            <div class="job">
                                <div class="jobTitle">
                                    <h4>Votre métier</h4>
                                </div>
                                <input v-model="job" type="text" maxlength="20">
                            </div>
                            <div>
                                <small  class="error"
                                        v-for="(error, index) of v$.job.$errors"
                                        :key="index">
                                        {{ error.$message }}
                                </small>
                            </div>
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
import { useSignUpForm } from "../stores/signupform";
import { helpers, minLength, required, } from "@vuelidate/validators";
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
        description: "",
        location: "",
        job: "",
        cities: [],
        };
    },
    methods:{
        // submit the form to our backend api
        submitForm() {
            this.v$.$touch();
            if (this.v$.$error) return;
            // complète l'utilisateur dans le store au fur et au mesure
            this.store.$patch((state) => {
                (state.description = this.description), (state.location = this.location), (state.job = this.job);
            });
            console.log(this.store.$state);
            // methode pour poster un utilisateur dans l'api
            this.$router.push("/docUpload");
        },
    },
    validations() {
        return {
        description: { 
            required: helpers.withMessage('Veuillez renseignez une description', required),
            minLength: helpers.withMessage(
                ({
                    $params
                }) => `La description doit contenir au minimum ${$params.min} caractères.`,
                minLength(5),
                )
            },
        location: { 
            required: helpers.withMessage('Veuillez renseignez une localisation', required),
            minLength: helpers.withMessage(
                ({
                    $params
                }) => `La localisation doit comporter au minimum ${$params.min} caractères.`,
                minLength(3)
                )
            },
        job: { 
            required: helpers.withMessage('Veuillez renseignez un métier.', required),
             minLength: helpers.withMessage(
                ({
                    $params
                }) => `Le métier doit comporter au minimum ${$params.min} caractères.`,
                minLength(3)
                )
            },
        };
    },
}
</script>

<style scoped>
    body{
        padding-left: 5%;
        padding-right: 5%;
    }
    /** title */
    h2,h3,h4 {
        font-size: 1.5em;
        line-height: 1.3em;
        vertical-align: middle;
    }
    #title {
        width: 25%;
        color: rgb(255, 255, 255);
        height: 6em;
        line-height: 1.2;
        font-size: 18px;
    }
    .descriptionTitle, .locationTitle, .jobTitle {
        padding-top: 3%;
        width: 65%;
        color: rgb(255, 255, 255);
        height: 3em;
        line-height: 1.2;
    }
    .error {
        color: red;
        font-size: 0.95em;
    }


    /** div form */
    .description, .location, .job{
        padding-top: 5%;
    }
    /** logo css */
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

    /** input description */
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

    .container {
        height: 7em;
    }

    /** continue button */
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