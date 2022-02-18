<template>
    <main class="feed-container">
        <div class="slider-container">
            <swiper
                ref="swiper"
                :modules="modules"
                :slides-per-view="1"
                :navigation="navigation"
                :allow-slide-prev="true"
                :grab-cursor="true"
                effect="cards"
                @swiper="onSwiper"
                @slideChange="onSlideChange"
            >
                <swiper-slide v-for="(user, index) in userList" :key="index">
                    <div class="card-container">
                        <TinderCard :user="user"  title="Slide 1" />
                    </div>
                </swiper-slide>
            </swiper>
            <!-- navigation -->
            <div class="navigation">
                <button
                    @touchstart="dislikeHoverColorChange"
                    @touchend="leaveColorChange"
                    @click="checkusers"
                    class="slider-button dislike-button"
                    :class="'swipe-next'"
                >
                    <Icon class="icon" icon="clarity:heart-broken-solid" width="20" :inline="true" />
                </button>
                <button
                    @touchstart="likeHoverColorChange"
                    @touchend="leaveColorChange"
                    class="slider-button like-button"
                    :class="'swipe-next'"
                >
                    <Icon class="icon" icon="flat-color-icons:like" width="22" height="22" />
                </button>
            </div>
        </div>
    </main>
</template>
<script>
// import Swiper core and required modules
import { Navigation, Pagination, Scrollbar, A11y, EffectCards } from 'swiper';
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue';

import TinderCard from './TinderCardComponent.vue';
import { Icon } from "@iconify/vue";
import { RouterLink } from "vue-router";

// Import stores
import { userFeedStore } from "../stores/userFeedStore.js";



// Import Swiper styles
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import 'swiper/css/effect-cube';

// Import Swiper styles
export default {
    props: {
        user: Object,
    },
    setup(props) {
        // instancie le store
        const store = userFeedStore();
        store.getUserList(props.user)
        const userList = store.$state.userList
        
        return {
            store,
            userList
        };
    },
    components: {
        Swiper,
        SwiperSlide,
        TinderCard,
        Icon,
        RouterLink,
    },
    methods: {
        checkusers() {
            console.log(this.userList)
        },
        likeHoverColorChange() {
            let cards = document.getElementsByClassName("card-front");
            for (let index = 0; index < cards.length; index++) {
                let element = cards[index];
                element.style.border = "2px solid green";
            }
        },
        dislikeHoverColorChange() {
            let cards = document.getElementsByClassName("card-front");
            for (let index = 0; index < cards.length; index++) {
                let element = cards[index];
                element.style.border = "2px solid red";
            }
        },
        leaveColorChange() {
            let cards = document.getElementsByClassName("card-front");
            for (let index = 0; index < cards.length; index++) {
                let element = cards[index];
                element.style.border = "transparent";
            }
        },
        prev() {
            this.$refs.swiper.$swiper.slidePrev()
        },
        next() {
            this.$refs.swiper.$swiper.slideNext()
        },
        onSwiper(swiper) {
            //console.log(swiper);
        },
        onSlideChange(swiper) {
            console.log('slide change');
        }
    },
    data() {
        return {
            background: "https://picsum.photos/600/900",
            modules: [Navigation, Pagination, Scrollbar, A11y, EffectCards],
            navigation: {
                nextEl: '.swipe-next',
                prevEl: '.__prev'
            },
            userList: this.store.userList
        }
    },
};
</script>
<style scoped>
.card-container {
    width: 100%;
    height: 75vh;
}
.slider-container {
    margin-top: 10px;
    margin-left: 7px;
    margin-right: 7px;
}

.navigation {
    display: flex;
    justify-content: space-evenly;
    margin-top: 1vh;
}

.slider-button {
    width: 53px;
    height: 53px;
    margin-top: 10px;
    border-radius: 100%;
    background-color: white;
    border: 1px solid #aaaaaa;
}
</style>
