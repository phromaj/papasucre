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
                <swiper-slide class="card">
                    <h2>Slide 1</h2>
                </swiper-slide>
                <swiper-slide class="card card-2">
                    <h2>Slide 2</h2>
                </swiper-slide>
                <swiper-slide class="card">
                    <h2>Slide 3</h2>
                </swiper-slide>
                <swiper-slide class="card">
                    <h2>Slide 4</h2>
                </swiper-slide>
                <swiper-slide class="card">
                    <h2>Slide 5</h2>
                </swiper-slide>
            </swiper>
            <!-- navigation -->
            <div class="navigation">
                <div class="slider-button dislike-button" :class="'swipe-next'">Dislike</div>
                <div class="slider-button like-button" :class="'swipe-next'">Like</div>
            </div>
        </div>
    </main>
</template>
<script>
// import Swiper core and required modules
import { Navigation, Pagination, Scrollbar, A11y, EffectFlip, EffectCoverflow, EffectCards } from 'swiper';

// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import 'swiper/css/effect-cube';

// Import Swiper styles
export default {
    components: {
        Swiper,
        SwiperSlide,
    },
    methods: {
        prev() {
            this.$refs.swiper.$swiper.slidePrev()
        },
        next() {
            this.$refs.swiper.$swiper.slideNext()
        },
        onSwiper(swiper) {
            console.log(swiper);
        },
        onSlideChange(swiper) {
            console.log('slide change');
        }
    },
    data() {
        return {
            modules: [Navigation, Pagination, Scrollbar, A11y, EffectCards],
            navigation: {
                nextEl: '.swipe-next',
                prevEl: '.__prev'
            },


        }
    },
};
</script>
<style scoped>
.card {
    width: 600px;
    height: 550px;
    background-color: red;
}
.feed-container {
    display: flex;
    justify-content: center;
    align-items: center;
}

.slider-container {
    width: 50%;
}

.navigation {
    display: flex;
    justify-content: space-evenly;
}

.slider-button {
    cursor: pointer;
    padding: 20px;
    background-color: blue;
}
.card-2{
    background-color: blue;;
}
</style>
