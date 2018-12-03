<template>
    <div class="lines">
        <Card style="width:100%;min-height:50px;" dis-hover>
            <play-list :currentVideo="currentVideo" v-for="line in lines" v-if="line.list.length > 0" :key="line.id"
                       :line="line" :videos="line.list"></play-list>
        <Spin size="large" fix v-if="spinShow"></Spin>
        </Card>
    </div>
</template>
<script>
    import PlayList from './PlayList'
    export default {
        data(){
            return {
                lines: [],
                spinShow: true,
            }
        },
        props: ['currentVideo', 'subject'],
        components: {
            PlayList
        },
        methods: {
            getList(sid){
                this.spinShow = true;
                this.$api.getLines(sid).then(res => {
                    console.log(res);
                    this.lines = res.results;
                }, () => {
                    console.log('获取视频错误');
                }).then(() => {
                    this.spinShow = false;
                });
            }
        },
        mounted(){

        },
        watch: {
            'subject' (to, from) {
                if (this.subject)
                    this.getList(this.subject.id);
            }
        },
    }
</script>
<style scoped>

</style>