<template>
    <div class="search" v-if="list.results">
        <h3>搜索 - {{ searchText }}</h3>
        <Row style="" class="search-list" v-if="list.results.length">
            <Col :xs="12" :sm="6" :md="6" :lg="4" v-for="subject in list.results" :key="subject.id"
                 class="subject">
            <subject-cover :subject="subject" :category="subject.category"></subject-cover>
            </Col>
            <Spin size="large" fix v-if="spinShow"></Spin>
        </Row>

        <p v-else style="text-align: center;height: 100px;vertical-align: middle;line-height: 100px;">
            未找到相关的影片
        </p>

        <Page :total="list.count" @on-change="changePage" v-bind:current="page" simple/>
    </div>
    <loadingCard v-else></loadingCard>
</template>

<script>
//    import SubjectCover from '../components/SubjectCover'
//    import loadingCard from '../components/loadingCard.vue'

    export default {
        name: 'search',
        components: {
            SubjectCover:resolve => {require(['../components/SubjectCover'], resolve)},//懒加载
            loadingCard:resolve => {require(['../components/loadingCard'], resolve)},//懒加载
        },
        data() {
            return {
                list: [],
                spinShow: true,
                page: 1,
                searchText: '',
            }
        },
        methods: {
            initPage: function () {
                this.page = this.$route.query.page ? parseInt(this.$route.query.page) : 1;
                this.searchText = this.$route.query.search ? this.$route.query.search : '';
            },
            changePage: function (page) {
                this.page = parseInt(page);
                this.$route.query.page = page;
                this.getList(this.page);
            },
            startLoad: function () {
//                this.$Loading.start();
//                this.$Message.loading({
//                    content: 'Loading...',
//                    duration: 0
//                });
//                this.$Spin.show();
                this.spinShow = true;
            },
            endLoad: function () {
//                this.$Loading.finish();
//                this.$Message.destroy();
//                this.$Spin.hide();
                this.spinShow = false;
            },
            /**
             * 获取主题
             * @param page 页数
             */
            getList: function (page) {
                let searchText = this.$route.query.search;    // 获取分类ID
                let searchCategory = this.$route.query.category;
                if (!searchText) return;
                if (!searchCategory) searchCategory = '';
                this.startLoad();   // Loading

                // 获取数据
                this.$api.searchSubject(searchText, searchCategory, page).then(res => {
                    if (res.hasOwnProperty('results')) {
                        this.list = res;
                    }
                }, () => {
                    console.log('获取主题失败')
                }).then(() => {
                    this.endLoad();
                })
            },
            init(){
                this.initPage();
                let searchText = this.$route.query.search;
                let searchCategory = this.$route.query.category;
                console.log('search init searchText:', searchText);
//                this.$store.dispatch('initCategory', cid);
                this.getList(this.page);
            }
        },
        computed: {},

        created(){

            this.init();

        },
        mounted(){

        },
        watch: {
            '$route' (to, from) {
                console.log('search watch init');
                this.init();
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .ivu-page {
        text-align: center;
        margin: 10px 0;
    }

    .ivu-spin {
        /*background: #00000066;*/
    }

    .category-list {
        width: 100%;
        min-height: 200px;
        background: white;
        border-radius: 4px;
    }

    /* 页面输入框宽度 */
    .ivu-page-simple .ivu-page-simple-pager input {
        width: 50px;
    }
</style>
