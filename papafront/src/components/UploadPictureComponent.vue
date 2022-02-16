<template lang="">
  <div class="signup">
    <div id="logo">
      <img src="../assets/PAPASUCRE.png" alt="papasucre-logo" />
    </div>
    <div class="information">
      <div id="title">
        <h1>Ajout <br />Photo de profil</h1>
      </div>
      <form @submit.prevent="submitForm">
        <div class="document">
          <p>
            Veuillez ajouter une photo de profil.
          </p>
          <div class="upload">
            <div>
              <input
                type="file"
                class="ID-card recto"
                ref="fileInputRecto"
                @input="pickFileRecto"
                id="fileRecto"
                name="ID-cardRecto"
                accept="image/*,.pdf"
              />
              <label for="fileRecto">Choisissez un fichier</label>
              <p>Recto</p>
              <div
                class="imagePreviewWrapper"
                :style="{ 'background-image': `url(${profile_photo})` }"
                @click="selectImageRecto"
              ></div>
              <p>Aperçu</p>
            </div>
          </div>
            <div id="continueButton">
              <button type="submit" id="continue">Continuer</button>
            </div>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
import { useSignUpForm } from "../stores/signupform";


export default {
    setup() {
        // instancie le store
        const store = useSignUpForm();
        return {
            store,
        };
    },
    data() {
        return {
            profile_photo: null,
        };
    },

    methods: {
        selectImageRecto() {
            this.$refs.fileInputRecto.click();
        },
        pickFileRecto() {
            let input = this.$refs.fileInputRecto;
            let file = input.files;
            if (file && file[0]) {
                let reader = new FileReader();
                reader.onload = (e) => {
                    this.profile_photo = e.target.result;
                };
                reader.readAsDataURL(file[0]);
                this.$emit("input", file[0]);
            }
        },
        submitForm() {
            if (!this.profile_photo) {
                return
            }
            this.store.$patch((state) => {
                state.profile_picture = this.profile_photo;
            });
            console.log(this.store.$state);
            // methode pour poster un utilisateur dans l'api
            this.store.postUser();
            this.$router.push("/signin");

        },
    },
};
</script>
<style scoped>
.signup {
    width: 100vw;
    margin: 0 1%;
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

.information {
    width: 100%;
    color: #fff;
}

#title {
    height: 8em;
}
.document {
    width: 100%;
    display: flex;
    flex-direction: column;
}

.upload {
    display: flex;
    widows: 100%;
    flex-direction: column;
    align-items: center;
    margin: 5% 0;
}

.upload > div p {
    text-align: center;
}

.ID-card {
    width: 0.1px;
    height: 0.1px;
    opacity: 0;
    overflow: hidden;
    position: absolute;
    z-index: -1;
    align-items: center;
}

label {
    height: 5em;
    padding: 25px 3px 0 3px;
}
.ID-card + label {
    font-size: 1em;
    color: white;
    display: inline-block;
    cursor: pointer;
    border: 2px dashed #fff;
}

.ID-card + label * {
    pointer-events: none;
}
.ID-card:focus + label,
.ID-card + label:hover {
    background-color: rgb(163, 125, 0);
    border: 2px dashed rgb(163, 125, 0);
}

.imagePreviewWrapper {
    width: 100%;
    height: 20vh;
    margin-top: 10%;
    cursor: pointer;
    background-size: cover;
    background-position: center center;
    border: 2px solid #fff;
}

.idCardInstruction {
    width: 100%;
}

#idCardExample {
    display: flex;
    justify-content: center;
    margin: 10% 0;
}

#idCardExample img {
    width: 137px;
    height: 87px;
}

#continueButton {
    width: 100%;
    padding-top: 8%;
    padding-bottom: 8%;
    display: flex;
    justify-content: center;
}

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
</style>
