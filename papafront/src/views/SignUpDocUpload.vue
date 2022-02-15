<template lang="">
    <div class="signup">
        <div id="logo">
            <img src="../assets/PAPASUCRE.png" alt="papasucre-logo" />
        </div>
        <div class="information">
            <div id="title">
                <h1>Mes<br>Documents</h1>
            </div>
            <form>
                <div class="document">
                    <p>Nous allons vérifiez votre identité. Vous devez fournir votre pièce d'identité recto/verso au format .png .jpg ou .pdf</p>
                    <div class="upload">
                        <div>
                            <input type="file" class="ID-card recto" ref="fileInputRecto" 
                            @input="pickFileRecto" id="fileRecto" name="ID-cardRecto" accept="image/png, image/jpg, application/pdf">
                            <label for="fileRecto">Choisissez un fichier</label>
                            <p>Recto</p>
                                <div class="imagePreviewWrapper" 
                                :style="{ 'background-image': `url(${previewImageRecto})` }" 
                                @click="selectImageRecto">
                                </div>
                                <p>Aperçu</p>
                        </div>
                        <div>
                            <input type="file" class="ID-card verso" ref="fileInputVerso" 
                            @input="pickFileVerso" id="fileVerso"  name="ID-cardVerso" accept="image/png, image/jpg, application/pdf">
                            <label for="fileVerso">Choisissez un fichier</label>
                            <p>Verso</p>
                             <div class="imagePreviewWrapper" 
                                :style="{ 'background-image': `url(${previewImageVerso})` }" 
                                @click="selectImageVerso">
                                </div>
                                <p>Aperçu</p>
                        </div>
                    </div>
                    <div class="idCardInstruction">
                        <p>Les 4 coins de votre pièce d'identité doivent être visible sur l'image comme sur l'exemple ci-dessous :</p>
                        <div id="idCardExample">
                            <img src="../assets/idCardExample.png" alt="Exemple_carte_identite">
                        </div>
                        <div id="continueButton">
                            <button id="continue">Continuer</button>
                         </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            IdCardRecto: "",
            IdCardVerso: "",
            previewImageRecto: null,
            previewImageVerso: null
        };
    },

    methods: {
        selectImageRecto() {
            this.$refs.fileInputRecto.click()
        },

        selectImageVerso() {
            this.$refs.fileInputVerso.click()
        },

        

        pickFileRecto() {
            let input = this.$refs.fileInputRecto;
            let file = input.files;
            if(file && file[0]) {
                let reader = new FileReader
                reader.onload = e => {
                    this.previewImageRecto = e.target.result
                }
                reader.readAsDataURL(file[0]);
                this.$emit('input', file[0]);
            }
        },

        pickFileVerso() {
            let input = this.$refs.fileInputVerso;
            let file = input.files;
            if(file && file[0]) {
                let reader = new FileReader
                reader.onload = e => {
                    this.previewImageVerso = e.target.result
                }
                reader.readAsDataURL(file[0]);
                this.$emit('input', file[0]);
            }
        },
    },
}
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
}

.upload {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
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
    height: 7em;
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