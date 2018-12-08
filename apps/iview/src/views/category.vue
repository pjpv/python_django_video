<template>

    <div class="category" v-if="list.results">
        <!--{{ category.name }} - {{ list.count }}-->
        <Row style="" class="category-list" v-if="list.results.length">
            <Col :xs="12" :sm="6" :md="4" :lg="3" v-for="subject in list.results" :key="subject.id"
                 class="subject">
            <subject-cover :subject="subject" :category="category"></subject-cover>
            </Col>
            <Spin size="large" fix v-if="spinShow"></Spin>
        </Row>
        <p v-else style="text-align: center;height: 100px;vertical-align: middle;line-height: 100px;">
            此分类暂无相关的影片
        </p>

        <Page :total="list.count" @on-change="changePage" v-bind:current="page" simple/>
    </div>
    <loadingCard v-else></loadingCard>

</template>

<script>
    //    import {getCategory, getSubjects} from '../api/api'
    import SubjectCover from '../components/SubjectCover'
    import loadingCard from '../components/loadingCard.vue'

    export default {
        name: 'category',
        components: {
            SubjectCover,
            loadingCard,
        },
        data() {
            return {
//                category: {},
                list: [],
                spinShow: true,
                page: 1,
            }
        },
        methods: {
            initPage: function () {
                this.page = this.$route.query.page ? parseInt(this.$route.query.page) : 1;

            },
            changePage: function (page) {
                this.page = parseInt(page);
//                this.$route.query.page = page;
                this.$router.push({
                    name: 'category',
                    id: this.$route.params.id,
                    query: {page: page}
                });
                console.log('changePage', this.$router.path);
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
                let cid = this.$route.params.id;    // 获取分类ID
                this.startLoad();   // Loading

                // 获取数据
                this.$api.getSubjects(cid, page).then(res => {
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
                let cid = this.$route.params.id;
                console.log('category init cid:', cid);
                this.$store.dispatch('initCategory', cid);
                this.getList(this.page);
            }
        },
        computed: {
            category: function () {
                let c = this.$store.state.currentCategory;
                if (c)
                    this.$util.title(c.name + ' - 第' + this.page + '页'); // 设置标题
                return c;
            }
        },

        created(a, b){
            console.log('category created init');
            console.log(this.$route.query);
//            if (!this.$route.query.page || !this.list.results)
                this.init();

        },
        mounted(){

        },
        watch: {
            '$route' (to, from) {
                console.log('category watch init', to, from);
//                if (!to.query.page)
//                    this.init();
                if (to.name === 'category' && to.params.id != from.params.id)
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
