<template>
    <div class="play-page">
        <div class="player" v-if="video">
            <!--v-title :data-title="'《' + subject.name + '》' + video.name + ' 正在播放'"-->
            <div v-if="!resetPlayer">
                <dplayer v-if="video.player === 0" :video="video"></dplayer>
                <ckplayer v-else-if="video.player === 1" :video="video"></ckplayer>
                <Viframe v-else-if="video.player === 2 || video.player === 4" :video="video"></Viframe>
                <div v-else-if="video.player === 3"
                     style="text-align: center;vertical-align: middle;">
                    <Card>
                        <p style="height: 100px;">
                            请复制地址到浏览器打开:
                            <br>
                            {{ video.link }}
                        </p>
                    </Card>
                </div>
            </div>
            <div v-else style="text-align: center;vertical-align: middle;height: 100px;line-height: 100px;">
                <Spin size="large" fix></Spin>
                加载中...
            </div>
        </div>
        <div v-if="error">
            数据错误, 无法播放
        </div>
        <lines :currentVideo="video" :subject="subject.id"></lines>
    </div>
</template>

<script>


    //    import '../../static/js/hls'
    //    //        require('hls');
    //    import '../../static/js/dash.all.min'
    //    import '../../static/js/flv'


    import Lines from '../../components/Lines'
    import dplayer from './dplayer.vue'
    import ckplayer from './ckplayer.vue'
    import Viframe from './iframe.vue'

    export default {
        name: 'play',
        data() {
            return {
                lines: [],
                video: '',
                hisInterval: 0,
                error: false,
                resetPlayer: false,
            }
        },
        methods: {
            reset(){
                this.video = '';
                this.resetPlayer = true;
                this.$nextTick(() => {
                    this.resetPlayer = false;
                })
            },
            init(){
                this.$Message.warning({
                    content:'部分视频源自带虚假广告！！！<br>与本站无关，切勿相信！',
                    duration: 5,
                })
                let video_id = this.$route.params.vid;
                console.log('paly init video_id:', video_id);
//                this.$store.dispatch('initSubject', video_id);
                this.getVideo(video_id).then(res => {
//                    console.log('getVideo res', res);
//                    this.getList(res.line.subject.id);
                }, () => {
                    this.error = true;
                });

                this.savePlayHistory();

            },
            getVideo(vid){
                return this.$api.getVideo(vid).then(res => {
                    console.log('getVideo', res);
                    this.video = res;
                    this.$store.state.currentVideo = res;
                    this.$store.state.currentSubject = res.line.subject;
                    this.subject = res.line.subject;
                    this.$store.state.currentCategory = res.line.subject.category;

                    this.$util.title('《' + this.subject.name + '》' + res.name + ' 正在播放' + ' ' + this.subject.category.name); // 设置标题
                    return res
                }, () => {
                    console.log('获取视频错误');
                })
            },
            getList(sid){
                this.$api.getLines(sid).then(res => {
                    console.log(res);
                    this.lines = res.results;
                }, () => {
                    console.log('获取视频错误');
                })
            },
            /* 两分钟后保存当前视频播放记录 */
            savePlayHistory(){
                let that = this;
                /* 清除上一个计时器 */
                clearInterval(that.hisInterval);
                /* 重新计时 */
                that.hisInterval = setInterval(function () {
                    let video = that.$store.state.currentVideo;
                    let subjtct = that.$store.state.currentSubject;
                    if (video.id && subjtct.id) {
                        localStorage.setItem('his-' + subjtct.id, video.id);
                    }
                    /* 只记录1次 */
                    clearInterval(that.hisInterval);
                    // 保存播放历史
                    that.$util.arrStore.set('PlayHistory', video.id);
                }, 60 * 2e3);
            }
        },
        computed: {
            subject: {
                get: function () {
                    return this.$store.state.currentSubject;
                },
                set: function () {
                }

            }
        },
        created()
        {
            this.init();
        },
        mounted(){
        },
        watch: {
            '$route'(to, from)
            {
                if (to.name === 'play' &&  to.params.vid != from.params.vid) {
                    console.log('Play watch init');
                    this.reset();
                    this.init();
                }
            }
        },
        components: {
            Lines,
            dplayer,
            ckplayer,
            Viframe,
        }
        ,
        metaInfo: {
            title: '播放视频',
            meta: [
                {name: 'referrer', content: 'never'},
            ],
            script: [
                {src: "https://cdn.staticfile.org/hls.js/0.10.1/hls.min.js", type: "text/javascript"},
                {src: "https://cdn.staticfile.org/dashjs/2.9.2/dash.all.min.js", type: "text/javascript"},
                {src: "https://cdn.staticfile.org/flv.js/1.4.2/flv.min.js", type: "text/javascript"},
            ]
        }
        ,
    }
</script>

<style>
    #player {
        margin-bottom: 10px;
    }
</style>
<style scoped>
    #player {
        width: 100%;
        height: 550px;
        background-image: url(https://ws1.sinaimg.cn/large/6260f60dly1fxt87tx6fug20jo0k0tbx.gif);
        background-position: top;
        background-repeat: no-repeat;
        background-size: auto;
    }
</style>