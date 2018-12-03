<template>
    <router-link :to="{ name: 'subject', params: {cid: category.id, id: subject.id} }" :title="subject.name">
        <Card class="cover" style="" :bordered="false" :shadow="false" :disHover="true">
            <div style="text-align:center">
                <!--<div class="cover-img" :style="backgroundImgUrl(subject.cover)"></div>-->
                <div class="cover-img">
                    <img class="cover-img-i" v-lazy="subject.cover"/>
                <div class="cover-mask">
                    <Icon type="ios-play"/>
                </div>
                </div>
                <h3 class="subject-title">{{ subject.name }}</h3>
            </div>
        </Card>
    </router-link>
</template>
<script>
    export default {
        props: ['subject', 'category'],
        methods: {
            backgroundImgUrl(url) {
                return `background-image: url(${url});`;
            },
        }
    }
</script>
<style media="screen">

    .cover .ivu-card-body {
        padding: 5px;
    }

    @media screen and (max-width: 768px) {
        .cover-img {
            height: 10pc;
        }
    }

    @media screen and  (max-width: 1024px) {
        .cover-img {
            height: 225px;
        }
    }

    @media screen and (max-width: 375px) {
        .cover-img {
            height: 148px;
        }
    }

    @media screen and (max-width: 544px) {
        .cover-img {
            height: 167px;
        }
    }

    @media screen and (max-width: 544px) {
        .cover-img {
            height: 165px;
        }
    }

    @media screen and (max-width: 768px) {
        .cover-img {
            height: 187px;
        }
    }

    /*.cover-img {*/
    /*height: 265px;*/
    /*}*/

    /*.cover-img {*/
    /*overflow: hidden;*/
    /*height: 167px;*/
    /*}*/
    .cover:hover {
        background: rgba(0, 0, 0, .15);
        /*opacity: 1;*/
    }

</style>
<style scoped>


    [lazy="error"] {
        object-fit: scale-down !important;
    }

    .cover-img {
        width: 100%;
        height: 250px;
        /* padding-bottom: 133.33%; */
        overflow: hidden;
        /* background-position: center center; */
        /* background-repeat: no-repeat; */
        /* background-size: cover; */
        /* box-shadow: 0 5px 5px -3px rgba(0, 0, 0, 0.2), 0 8px 10px 1px rgba(0, 0, 0, 0.14), 0 3px 14px 2px rgba(0, 0, 0, 0.12); */
        /* border-color: #eee; */
        /* border: 1px solid #000; */
        /*height: 250px;*/
        height: 14em;
        overflow: hidden;
        padding: 5px;
    }

    img.cover-img-i {
        width: 100%;
        /* width: auto; */
        height: 100%;
        max-width: 100%;
        max-height: 100%;
        /*box-shadow: 0 1px 6px rgba(0, 0, 0, .2);*/
        border-color: #eee;
        object-fit: cover;
        object-fit: contain;
    }

    .cover {
        /*padding: 5px 10px;*/
        /*width:100%;*/
        /*height:auto;*/
        border: 1px solid #eee !important;
    }

    /*.cover-img {*/
    /*width: 100%;*/
    /*!* height: 0; *!*/
    /*padding-bottom: 133.33%;*/
    /*overflow: hidden;*/
    /*background-position: center center;*/
    /*background-repeat: no-repeat;*/
    /*-webkit-background-size: cover;*/
    /*-moz-background-size: cover;*/
    /*background-size: cover;*/

    /*box-shadow: 0 5px 5px -3px rgba(0, 0, 0, .2), 0 8px 10px 1px rgba(0, 0, 0, .14), 0 3px 14px 2px rgba(0, 0, 0, .12);*/
    /*border-color: #eee;*/
    /*}*/

    .cover-mask {
        background: #00000026;
        opacity: 0;
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
    }

    .cover-mask:hover {
        opacity: 1;
    }

    .cover-mask i {
        font-size: 60px;
        text-align: center;
        display: block;
        line-height: 100%;
        padding: 50% 0;
        color: white;
    }

</style>