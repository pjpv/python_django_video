<style scoped="">
    video {
        width: 100%;
    }

    #player {
        width: 100%;
        height: 550px;
        background-image: url(https://ws1.sinaimg.cn/large/6260f60dly1fxt87tx6fug20jo0k0tbx.gif);
        background-position: top;
        background-repeat: no-repeat;
        background-size: auto;
    }

    @media screen and (min-width: 1201px) {
        #player {
            height: 650px;
        }
    }

    /* css注释：设置了浏览器宽度不小于1201px时 abc 显示1200px宽度 */

    @media screen and (max-width: 1200px) {
        #player {
            height: 550px;
        }
    }

    /* 设置了浏览器宽度不大于1200px时 abc 显示900px宽度 */

    @media screen and (max-width: 901px) {
        #player {
            height: 400px;
        }
    }

    /* 设置了浏览器宽度不大于901px时 abc 显示200px宽度 */

    @media screen and (max-width: 500px) {
        #player {
            height: 300px;
        }
    }

    @media screen and (max-width: 450px) {
        #player {
            height: 250px;
        }
    }
    @media screen and (max-width: 450px) {
        #player {
            height: 190px;
        }
    }
</style>
<template>
    <div class="player">
        <div id="player" v-if="video">
            <iframe name="ifm" class="fan mdui-container" :src="video.link" style="height: 100%;width: 100%;"
                    frameborder="no" scrolling="no" allowfullscreen="true" marginwidth="0" marginheight="0" vspace="0"
                    hspace="0" align="middle">
            </iframe>
        </div>
    </div>
</template>
<script>

    export default {
        props: ['video'],
        data(){
            return {}
        },
        components: {},
        methods: {},
        mounted(){
        },
        metaInfo: {},
        watch: {},
    }
</script>
