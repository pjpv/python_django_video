<template>
    <div class="player">
        <div id="player" ref="dplayer"></div>
    </div>
</template>
<script>
    import 'DPlayer/dist/DPlayer.min.css';
    //    import '../../static/js/hls'
    //    require('hls');
    //    import '../../static/js/dash.all.min'
    //    import '../../static/js/flv'
    import DPlayer from 'DPlayer';


    export default {
        props: ['video'],
        components: {},
        data(){
            return {
                player: null
            }
        },
        methods: {
            init0(){
                let that = this;
                let isHlsInit = false;
                let i = 0;

                let t = setInterval(function () {

                    console.log(i);
                    try {
                        new Hls();
                        clearInterval(t);
                        isHlsInit = true;
                        that.init();
                    } catch (e) {
                        i++;
                        if (i > 20) {
                            clearInterval(t);
                            console.log('Hls 初始化失败')
                        }
                    }
                }, 500);
            },
            init(){


                if (this.player) {
                    /* 切换视频源 */
                    this.player.switchVideo({
                        url: this.video.link,
//                        pic: 'second.png',
//                        thumbnails: 'second.jpg'
                    });
                    /* 销毁 */
//                    this.player.destroy();
                } else {
                    console.log('link', this.video.link);
                    this.player = new DPlayer({
                        container: this.$refs.dplayer,
//                screenshot: false,
//                logo: 'image/logo4.png',
                        video: {
                            url: this.video.link,
                        },
//                contextmenu: [
//                ],
                    });
//                    this.player.on('abort', function () {
//                        console.log('player abort');
//                    });
//                    this.player.on('canplay', function () {
//                        console.log('player canplay');
//                    });
//                    this.player.on('canplaythrough', function () {
//                        console.log('player canplaythrough');
//                    });
//                    this.player.on('durationchange', function () {
//                        console.log('player durationchange');
//                    });
//                    this.player.on('emptied', function () {
//                        console.log('player emptied');
//                    });
//                    this.player.on('ended', function () {
//                        console.log('player ended');
//                    });
//                    this.player.on('error', function () {
//                        console.log('player error');
//                    });
//                    this.player.on('loadeddata', function () {
//                        console.log('player loadeddata');
//                    });
//                    this.player.on('loadedmetadata', function () {
//                        console.log('player loadedmetadata');
//                    });
//                    this.player.on('loadstart', function () {
//                        console.log('player loadstart');
//                    });
//                    this.player.on('mozaudioavailable', function () {
//                        console.log('player mozaudioavailable');
//                    });
//                    this.player.on('pause', function () {
//                        console.log('player pause');
//                    });
//                    this.player.on('play', function () {
//                        console.log('player play');
//                    });
//                    this.player.on('playing', function () {
//                        console.log('player playing');
//                    });
//                    this.player.on('progress', function () {
//                        console.log('player progress');
//                    });
//                    this.player.on('ratechange', function () {
//                        console.log('player ratechange');
//                    });
//                    this.player.on('seeked', function () {
//                        console.log('player seeked');
//                    });
//                    this.player.on('seeking', function () {
//                        console.log('player seeking');
//                    });
//                    this.player.on('stalled', function () {
//                        console.log('player stalled');
//                    });
//                    this.player.on('suspend', function () {
//                        console.log('player suspend');
//                    });
//                    this.player.on('timeupdate', function () {
//                        console.log('player timeupdate');
//                    });
//                    this.player.on('volumechange', function () {
//                        console.log('player volumechange');
//                    });
//                    this.player.on('waiting', function () {
//                        console.log('player waiting');
//                    });
                }
            }

        },
        mounted(){
            this.init0();
        },
        beforeDestroy(){
            // 离开时销毁播放器
            this.player.destroy();
        },
//        metaInfo: {
//            meta: [
//                {name: 'referrer', content: 'never'}
//            ],
//        },
        /* 视频地址变化时,切换初始化 */
        watch: {
            'video' (to, from) {
                this.init0();
            }
        },
    }
</script>
