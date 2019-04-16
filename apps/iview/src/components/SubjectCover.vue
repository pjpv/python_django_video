<template>
    <router-link :to="{ name: 'subject', params: {cid: category.id, id: subject.id} }" :title="subject.name">
        <Card class="cover" style="" :bordered="false" :shadow="false" :disHover="true">
            <div style="text-align:center">
                <!--<div class="cover-img" :style="backgroundImgUrl(subject.cover)"></div>-->
                <div class="cover-img">
                    <div class="tips">{{subject.tips}}</div>
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
        name: 'SubjectCover',
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

    /*.cover-img {*/
    /*height: 265px;*/
    /*}*/

    /*.cover-img {*/
    /*overflow: hidden;*/
    /*height: 167px;*/
    /*}*/
    /*.cover:hover {*/
    /*background: rgba(0, 0, 0, .15);*/
    /*opacity: 1;*/
    /*}*/

</style>
<style scoped>


    [lazy="error"] {
        object-fit: scale-down !important;
    }

    .cover-img {
        width: 100%;
        /*height: 250px;*/
        /* padding-bottom: 133.33%; */
        overflow: hidden;
        /* background-position: center center; */
        /* background-repeat: no-repeat; */
        /* background-size: cover; */
        /* box-shadow: 0 5px 5px -3px rgba(0, 0, 0, 0.2), 0 8px 10px 1px rgba(0, 0, 0, 0.14), 0 3px 14px 2px rgba(0, 0, 0, 0.12); */
        /* border-color: #eee; */
        /* border: 1px solid #000; */
        /*height: 250px;*/
        /*height: 14em;*/
        overflow: hidden;
        padding: 0px;
        /*height: calc(100vh / 4);*/
        position: relative;
    }

    /*@media screen and(max-width:1921px){.category .cover-img{height:225px;}}*/
    /*@media screen and(max-width:1921px){.category .cover-img{height:170px;}}*/
    /*@media screen and(max-width:1440px){.category .cover-img{height:160px;}}*/
    /*@media screen and(max-width:1366px){.category .cover-img{height:160px;}}*/
    /*@media screen and(max-width:1280px){.category .cover-img{height:180px;}}*/
    /*@media screen and(max-width:1024px){.category .cover-img{height:205px;}}*/
    /*@media screen and(max-width:767px){.category .cover-img{height:425px;}}*/
    /*@media screen and(max-width:600px){.category .cover-img{height:340px;}}*/
    /*@media screen and(max-width:544px){.category .cover-img{height:310px;}}*/
    /*@media screen and(max-width:410px){.category .cover-img{height:245px;}}*/
    /*@media screen and(max-width:376px){.category .cover-img{height:230px;}}*/
    /*@media screen and(max-width:375px){.category .cover-img{height:202px;}}*/
    /*@media screen and(max-width:321px){.category .cover-img{height:190px;}}*/
    /*@media screen and(max-width:320px){.category .cover-img{height:160px;}}*/

    /*@media screen and(max-width:1921px){.index .cover-img{height:225px;}}*/
    /*@media screen and(max-width:1440px){.index .cover-img{height:160px;}}*/
    /*@media screen and(max-width:1366px){.index .cover-img{height:160px;}}*/
    /*@media screen and(max-width:1280px){.index .cover-img{height:180px;}}*/
    /*@media screen and(max-width:1024px){.index .cover-img{height:195px;}}*/
    /*@media screen and(max-width:767px){.index .cover-img{height:425px;}}*/
    /*@media screen and(max-width:667px){.index .cover-img{height:360px;}}*/
    /*@media screen and(max-width:600px){.index .cover-img{height:320px;}}*/
    /*@media screen and(max-width:544px){.index .cover-img{height:270px;}}*/
    /*@media screen and(max-width:410px){.index .cover-img{height:230px;}}*/
    /*@media screen and(max-width:376px){.index .cover-img{height:200px;}}*/
    /*@media screen and(max-width:375px){.index .cover-img{height:202px;}}*/
    /*@media screen and(max-width:321px){.index .cover-img{height:190px;}}*/
    /*@media screen and(max-width:320px){.index .cover-img{height:160px;}}*/

    @media screen and(min-width: 1922px) {
        .category .cover-img {
            height: 330px;
        }
    }
    @media screen and(max-width: 1921px) {
        .category .cover-img {
            height: 300px;
        }
    }

    @media screen and(max-width: 1660px) {
        .category .cover-img {
            height: 250px;
        }
    }
    @media screen and(max-width: 1440px) {
        .category .cover-img {
            height: 160px;
        }
    }

    @media screen and(max-width: 1366px) {
        .category .cover-img {
            height: 200px;
        }
    }

    @media screen and(max-width: 1280px) {
        .category .cover-img {
            height: 195px;
        }
    }

    @media screen and(max-width: 1200px) {
        .category .cover-img {
            height: 310px;
        }
    }

    @media screen and(max-width: 1024px) {
        .category .cover-img {
            height: 235px;
        }
    }

    @media screen and(max-width: 991px) {
        .category .cover-img {
            height: 240px;
        }
    }

    @media screen and(max-width: 767px) {
        .category .cover-img {
            height: 425px;
        }
    }

    @media screen and(max-width: 600px) {
        .category .cover-img {
            height: 300px;
        }
    }

    @media screen and(max-width: 544px) {
        .category .cover-img {
            height: 250px;
        }
    }

    @media screen and(max-width: 410px) {
        .category .cover-img {
            height: 215px;
        }
    }

    @media screen and(max-width: 376px) {
        .category .cover-img {
            height: 200px;
        }
    }

    @media screen and(max-width: 375px) {
        .category .cover-img {
            height: 190px;
        }
    }

    @media screen and(max-width: 321px) {
        .category .cover-img {
            height: 170px;
        }
    }
    @media screen and(min-width: 1922px) {
        .search .cover-img {
            height: 330px;
        }
    }
    @media screen and(max-width: 1921px) {
        .search .cover-img {
            height: 300px;
        }
    }

    @media screen and(max-width: 1660px) {
        .search .cover-img {
            height: 250px;
        }
    }
    @media screen and(max-width: 1440px) {
        .search .cover-img {
            height: 160px;
        }
    }

    @media screen and(max-width: 1366px) {
        .search .cover-img {
            height: 200px;
        }
    }

    @media screen and(max-width: 1280px) {
        .search .cover-img {
            height: 195px;
        }
    }

    @media screen and(max-width: 1200px) {
        .search .cover-img {
            height: 310px;
        }
    }

    @media screen and(max-width: 1024px) {
        .search .cover-img {
            height: 235px;
        }
    }

    @media screen and(max-width: 991px) {
        .search .cover-img {
            height: 240px;
        }
    }

    @media screen and(max-width: 767px) {
        .search .cover-img {
            height: 425px;
        }
    }

    @media screen and(max-width: 600px) {
        .search .cover-img {
            height: 300px;
        }
    }

    @media screen and(max-width: 544px) {
        .search .cover-img {
            height: 250px;
        }
    }

    @media screen and(max-width: 410px) {
        .search .cover-img {
            height: 215px;
        }
    }

    @media screen and(max-width: 376px) {
        .search .cover-img {
            height: 200px;
        }
    }

    @media screen and(max-width: 375px) {
        .search .cover-img {
            height: 190px;
        }
    }

    @media screen and(max-width: 321px) {
        .search .cover-img {
            height: 170px;
        }
    }

    @media screen and(min-width: 1922px) {
        .index .cover-img {
            height: 300px;
        }
    }
    @media screen and(max-width: 1921px) {
        .index .cover-img {
            height: 300px;
        }
    }

    @media screen and(max-width: 1660px) {
        .index .cover-img {
            height: 260px;
        }
    }
    @media screen and(max-width: 1440px) {
        .index .cover-img {
            height: 210px;
        }
    }

    @media screen and(max-width: 1366px) {
        .index .cover-img {
            height: 200px;
        }
    }

    @media screen and(max-width: 1280px) {
        .index .cover-img {
            height: 180px;
        }
    }

    @media screen and(max-width: 1024px) {
        .index .cover-img {
            height: 195px;
        }
    }

    @media screen and(max-width: 767px) {
        .index .cover-img {
            height: 425px;
        }
    }

    @media screen and(max-width: 667px) {
        .index .cover-img {
            height: 360px;
        }
    }

    @media screen and(max-width: 600px) {
        .index .cover-img {
            height: 300px;
        }
    }

    @media screen and(max-width: 544px) {
        .index .cover-img {
            height: 250px;
        }
    }

    @media screen and(max-width: 410px) {
        .index .cover-img {
            height: 210px;
        }
    }

    @media screen and(max-width: 376px) {
        .index .cover-img {
            height: 200px;
        }
    }

    @media screen and(max-width: 375px) {
        .index .cover-img {
            height: 190px;
        }
    }

    @media screen and(max-width: 321px) {
        .index .cover-img {
            height: 160px;
        }
    }

    img.cover-img-i {
        width: 100%;
        /* width: auto; */
        height: 100%;
        max-width: 100%;
        max-height: 100%;
        /*box-shadow: 0 1px 6px rgba(0, 0, 0, .2);*/
        border-color: #eee;
        /*object-fit: cover;*/
        /*object-fit: contain;*/
        border-radius: 4px;
    }

    .cover {
        /*padding: 5px 10px;*/
        /*width:100%;*/
        /*height:auto;*/
        /*border: 1px solid #eee !important;*/
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

    /*.tips {*/
    /*float: right;*/
    /*position: absolute;*/
    /*color: white;*/
    /*right: 0;*/
    /*background: #0000006b;*/
    /*top: 5%;*/
    /*text-shadow:3px 2px 10px #000;*/
    /*}*/
    .tips {
        float: right;
        position: absolute;
        color: white;
        background: #000000b5;
        /*text-shadow: 3px 2px 10px #fff;*/
        bottom: 0;
        border-radius: 0 5px 0 0;
        padding: 0 5px;
    }
</style>