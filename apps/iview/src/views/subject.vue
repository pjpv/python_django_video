<template>
    <div class="subject-page" v-cloak v-if="!resetPage && subject">
        <!--{{ subject }}-->
        <div class="subject-info">
            <Row style="padding: 10px;" :gutter="5">
                <Col :xs="24" :sm="10" :md="6" :lg="5" style="margin: 5px 0;">
                <div class="mdui-grid-tile mdui-shadow-4 mdui-color-white"
                     style="padding: 10px;-webkit-box-shadow: 0 2px 4px -1px rgba(0, 0, 0, .2), 0 4px 5px 0 rgba(0, 0, 0, .14), 0 1px 10px 0 rgba(0, 0, 0, .12);box-shadow: 0 2px 4px -1px rgba(0, 0, 0, .2), 0 4px 5px 0 rgba(0, 0, 0, .14), 0 1px 10px 0 rgba(0, 0, 0, .12);">
                    <img class="mdui-img-rounded" v-if="!resetPage"
                         style="display: block;width: 100%;border-radius: 4px;    min-height: 100px;"
                         v-lazy="subject.cover">
                </div>
                </Col>
                <Col :xs="24" :sm="14" :md="18" :lg="19">
                <span></span>
                <div class="subjtct-info-title"><h2>{{ subject.name }}</h2></div>
                <Table width="auto" small :disabled-hover="true" :border="false" :stripe="false" :columns="columns1"
                       :show-header="false"
                       :data="infoData"></Table>
                </Col>
            </Row>
            <Spin size="large" fix v-if="spinShow"></Spin>
        </div>
        <lines v-if="!resetPage" :subject="subjectId"></lines>
    </div>
    <loadingCard v-else></loadingCard>
</template>

<script>

//    import Lines from '../components/Lines'
//    import loadingCard from '../components/loadingCard.vue'

    export default {
        name: 'subject',
        data() {
            return {
                columns1: [
                    {
                        key: 'label',
                        width: 100,

                        className: 'subjtct-info-label'
                    },
                    {
                        key: 'content',

                        render: (h, params) => {
                            const row = params.row;
                            const arr = ['标签:', '主演:', '导演:', '地区:', '年代:'];
                            if (arr.indexOf(row.label) >= 0) {
                                let text = (row.content + '').split(',');
                                return h('div', text.map((item, index) => h('Tag', {
                                    nativeOn: {
                                        'click': () => {
                                            let route = {
                                                name: 'search',
                                                query: {
                                                    search: item,
                                                },
                                                meta: {
                                                    title: `搜索-${item}`
                                                }
                                            };
                                            this.$router.push(route);
                                        }
                                    }
                                }, item)));

                            } else {
                                return h('span', row.content);
                            }
                        }
                    }
                ],
                lines: [],
                spinShow: true,
                subject: '',
                subjectId: '',
                resetPage: false,
                infoData: [],
            }
        },
        methods: {
            reset(){
                let that = this;
                this.subject = '';
                that.resetPage = true;
                console.log('resetPage', that.resetPage);
                that.$nextTick(() => {
                    setTimeout(function () {
                        that.resetPage = false;
                        console.log('resetPage', that.resetPage);
                    }, 500);
                })
            },
            setSubject(){
                this.subject = this.$store.state.currentSubject;
            },
            setInfoData(){
                let s = this.$store.state.currentSubject;
                if (!s.id)return; // 未加载
                this.$util.title(s.name + ' - ' + s.category.name); // 设置标题
                this.infoData = [
//                    {
//                        label: '标题',
//                        content: s.name,
//                        cellClassName: {
//                            label: 'hideen',
//                            content: 'subjtct-info-title'
//                        }
//                    },
                    {
                        label: '年代:',
                        content: new Date(s.pub_date).getFullYear()
                    },
                    {
                        label: '地区:',
                        content: s.area

                    },
                    {
                        label: '状态:',
                        content: s.state ? '全集' : '连载中',
                    },
                    {
                        label: '标签:',
                        content: s.tags,
                    },
                    {
                        label: '导演:',
                        content: s.director
                    },
                    {
                        label: '主演:',
                        content: s.actress
                    },
                    {
                        label: '剧情:',
                        content: s.desc
                    }
                ]
            },
            init(){
                let sid = this.$route.params.id;
                this.subjectId = sid;
                this.subject = '';
                this.reset();
                console.log('subject init sid:', sid);
//                this.$store.dispatch('initSubject', sid);
                this.spinShow = true;
                this.$api.getSubject(sid).then(res => {
                    if (res.hasOwnProperty('id')) {
                        this.$store.state.currentSubject = res;
                        this.$store.state.currentCategory = res.category;
                    } else {
                        console.log('主题加载错误')
                    }
                }).then(() => {
                    this.spinShow = false;
                    this.setSubject();
                    this.setInfoData();
                })
//                this.getList(sid);
            },
//            getList(sid){
//
//                this.$api.getLines(sid).then(res => {
//                    console.log(res);
//                    this.lines = res.results;
//                }, () => {
//                    console.log('获取视频错误');
//                })
//            }

        },
        computed: {
//            subject: {
//                get: function () {
//                    return this.$store.state.currentSubject;
//                },
//                set: function () {
//                }
//
//            },

        },
        created(){
            this.init();
        },
        watch: {
            '$route' (to, from) {
                console.log('Subject watch init');

                if (to.name === 'subject' && to.params.id != from.params.id)
                    this.init();
            }
        },
        components: {
//            Lines,
//            loadingCard,
            Lines:resolve => {require(['../components/Lines'], resolve)},//懒加载
            loadingCard:resolve => {require(['../components/loadingCard'], resolve)},//懒加载
        },
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .ivu-table:before, .ivu-table:after {
        background-color: transparent !important;
    }

    .ivu-table, .ivu-table-wrapper, .ivu-table td {
        border: none !important;
    }

    td.hideen {
        visibility: hidden;
        display: none;
    }

    .subjtct-info-title {
        font-size: 100%;
        font-weight: bold;
        padding: 0 50px;
    }

    .subjtct-info-label {
        text-align: right !important;
    }

    [v-cloak] {
        display: none;
    }
</style>
