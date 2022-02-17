<template>
    <div class="card">
        <div @click="flipCard" class="card-inner">
            <div class="card-front" :style="bgImage">
                <div class="user-info">
                    <div class="user-info-personal">{{user.name}} {{user.age}}</div>
                    <div class="user-info-job line-container">
                        <Icon class="icon-container" icon="bytesize:work" />
                        <p class="text-info">{{user.job}}</p>
                    </div>
                    <div class="user-info-town line-container">
                        <Icon class="icon-container" icon="bi:geo-alt" />
                        <p class="text-info">{{user.location}}</p>
                    </div>
                </div>
            </div>
            <div class="card-back">
                
            </div>
        </div>
    </div>
</template>
<script>
import { Icon } from "@iconify/vue";

export default {
    components: {
        Icon,
    },
    props: {
        title: String,
        user: Object,
    },
    computed: {
        bgImage(){
            return 'background-image : url(' + this.user.profile_picture + ');'
        }
    },
    methods: {
        flipCard(event){
            let className = event.target.className
            if(className == 'card-front' || className == 'card-back' )
            event.target.parentNode.classList.toggle("is-flipped")
        }
    },
}
</script>
<style scoped>
.card {
    display: flex;
    width: 100%;
    height: 100%;
}

.card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    transition: transform 0.7s;
    transform-style: preserve-3d;
    -webkit-transform-style: preserve-3d;
}

.card-front {
    display: flex;
    flex-direction: column;
    background-size: cover;
    box-shadow: inset 0px -100px 28px -12px rgba(0, 0, 0, 0.4);
    justify-content: flex-end;
    
}

.card-back {
    transform: rotateY(180deg);
    background-color: white;
}

.card-front,
.card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden; /* Safari */
    backface-visibility: hidden;
    border-radius: 16px;
    
}

.is-flipped{
   transform: rotateY(-180deg);
   -moz-transform: rotateY(-180deg) translateZ(1px); 
}

.user-info {
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding-bottom: 1rem;
    padding-left: 2rem;
}

.user-info-personal {
    display: flex;
    align-items: center;
}

.user-info-age {
    font-size: 18px;
    font-weight: bold;
    text-align: center;
}
.icon-container {
    padding-right: 2px;
}

.line-container {
    display: flex;
    align-items: center;
}
.user-info-personal {
    font-size: 28px;
    font-weight: bold;
}

.text-info {
    font-size: 16px;
    font-weight: bold;
}
</style>