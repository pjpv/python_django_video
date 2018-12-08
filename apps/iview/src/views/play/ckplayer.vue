<style scoped="">
    video {
        width: 100%;
    }

    #player {
        width: 100%;
        height: 550px;
        background-image: url(//ws1.sinaimg.cn/large/6260f60dly1fxt87tx6fug20jo0k0tbx.gif);
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;

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

    @media screen and (max-width: 400px) {
        #player {
            height: 250px;
        }
    }
</style>
<template>
    <div class="player">
        <div id="player" ref="dplayer"></div>
    </div>
</template>
<script>
//    import '../../static/js/ckplayer/hls/hls'
    import '../../static/js/ckplayer/ckplayer'


    export default {
        props: ['video'],
        data(){
            return {
                player: null
            }
        },
        components: {},
        methods: {
            init(){


                if (this.player) {
                    this.player.videoClear();
                    this.player.newVideo(this.video.link);

                } else {

                    let videoObject = {
                        container: '#player', //容器的ID或className
                        variable: 'player',//播放函数名称
                        autoplay: false,
                        flashplayer: true,
                        live: this.video.live,
                        video: this.video.link,
//                                mobileCkControls: true,//是否在移动端（包括ios）环境中显示控制栏#}
//                                mobileAutoFull: false,//在移动端播放后是否按系统设置的全屏播放#}
//                                html5m3u8: true

                        loaded: 'loadedHandler', //当播放器加载后执行的函数
                    };
                    this.player = new ckplayer(videoObject);

                }
//                    function errorHandler(e) {
//                        //出错了
//                        console.log('ckPlayer 播放错误',e)
//                    }
//                    function loadedHandler() {
//                        console.log('ckPlayer loadedHandler')
//                        this.player.addListener('loadedmetadata', errorHandler); //监听元数据
//                        this.player.addListener('error', errorHandler); //监听元数据
//                        this.player.addListener('duration', errorHandler); //监听元数据
//                        this.player.addListener('time', errorHandler); //监听元数据
//                        this.player.addListener('play', errorHandler); //监听元数据
//                        this.player.addListener('pause', errorHandler); //监听元数据
//                        this.player.addListener('paused', errorHandler); //监听元数据
//                        this.player.addListener('buffer', errorHandler); //监听元数据
//                        this.player.addListener('seek', errorHandler); //监听元数据
//                        this.player.addListener('seekTime', errorHandler); //监听元数据
//                        this.player.addListener('volume', errorHandler); //监听元数据
//                        this.player.addListener('full', errorHandler); //监听元数据
//                        this.player.addListener('ended', errorHandler); //监听元数据
//                        this.player.addListener('screenshot', errorHandler); //监听元数据
//                        this.player.addListener('mouse', errorHandler); //监听元数据
//                        this.player.addListener('frontAd', errorHandler); //监听元数据
//                        this.player.addListener('insertAd', errorHandler); //监听元数据
//                        this.player.addListener('endAd', errorHandler); //监听元数据
//                        this.player.addListener('playbackRate', errorHandler); //监听元数据
//                        this.player.addListener('controlBar', errorHandler); //监听元数据
//                        this.player.addListener('definitionChange', errorHandler); //监听元数据
//                        this.player.addListener('clickEvent', errorHandler); //监听元数据
//                    }

            }
        },
        mounted(){
            this.init();
        },
        beforeDestroy(){
            // 离开时销毁播放器（清除视频）
            this.player.videoClear();
        },
        metaInfo: {
            meta: [
                {name: 'referrer', content: 'never'}
            ]
        },
        watch: {
            '$route' (to, from) {
                this.init();
            }
        },
    }
</script>
