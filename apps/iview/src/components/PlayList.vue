<template>
    <div class="play-list">

        <Divider orientation="left">{{ line.name }}</Divider>
        <div class="links">
            <Row style="padding: 10px;" :gutter="5">
                <Col :xs="8" :sm="6" :md="4" :lg="3" style="margin: 5px 0;" v-for="video in videos" :key="video.id">

                <Button class="video-btn" long
                        :type="isCurrent(currentVideo, video) ? 'primary' : 'default'"
                        :icon="last_id==video.id ? 'ios-time-outline' : ''"
                        :style="isPlay(video) && !isCurrent(currentVideo, video) ? 'color:#808695;background: #f8f8f9;' : ''"
                        :title="last_id==video.id ? '上一次播放' : ''"
                        :to="{name:'play',params:{cid:line.subject.category.id, sid:line.subject.id, vid:video.id}}">
                    {{ video.name }}
                </Button>
                </Col>
            </Row>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'PlayList',
        props: ['currentVideo', 'line', 'videos'],
        data(){
            return {
                playHistory: []
            }
        },
        methods: {
            isCurrent(v, v2){
                return v && v2 && v.id && v2.id && v.id === v2.id;
            },
            initPlayHistory(){
                let his = this.$util.arrStore.get('PlayHistory');
                if (his instanceof Array) {
                    this.playHistory = his;
                }
            },
            isPlay(v){
                return this.playHistory.indexOf(v.id) >= 0;
            },

        },
        computed: {
            last_id(){
                let subjtct = this.line.subject.id;
                return localStorage.getItem('his-' + subjtct);
            },
        },
        created(){
            this.initPlayHistory();
        },
        mounted(){
        },
        watch: {
            '$route'(to, from)
            {
                this.initPlayHistory();
            }
        }
    }
</script>
<style>
    .play-list .ivu-divider-horizontal.ivu-divider-with-text-left {
        margin: 0!important;
    }
</style>
<style scoped="">
    .video-btn {
        margin: 2px 5px;
    }
</style>
