<style scoped>
    @import 'styles/common.css';
</style>
<style>
    .layout-footer-center {
        text-align: center;
    }

    html, body, .layout, .ivu-layout {
        height: 100%;
    }

    /* 内容居中 */
    .top-menu, .content {
        margin: 0 auto;
    }

    @media screen and (min-width: 1201px) {
        .top-menu {
            width: 80%;
        }

        .content {
            padding: 0 50px;
            width: 80%;
        }
    }

    @media screen and (max-width: 1200px) {
        .top-menu {
            width: 84%;
        }

        .content {
            padding: 0 30px;
            width: 84%;
        }
    }

    @media screen and (max-width: 901px) {
        .top-menu {
            width: 90%;
        }

        .content {
            padding: 0 2px;
            width: 90%;
        }
    }

    @media screen and (max-width: 500px) {
        .top-menu {
            width: 98%;
        }

        .content {
            padding: 0;
            width: 98%;
        }
    }

    /* 固定Footer */
    .ivu-layout {
        min-height: 100%;
        height: auto !important;
        height: 100%; /*IE6不识别min-height*/
        position: relative;
    }

    .content-card {
        margin-bottom: 85px; /*等于footer的高度*/
    }

    .ivu-layout-footer {
        position: absolute;
        bottom: 24px;
        width: inherit;
        height: 60px; /*脚部的高度*/
        clear: both;
    }

    /* 侧边栏触发器 */
    .ivu-layout-sider-zero-width-trigger {
        z-index: 999;
        display: none !important;
        top: 10px !important;
    }

    @media screen and (min-width: 901px) {
        /* 大屏幕显示顶部菜单 */
        .layout-nav {
            display: block !important;;
        }

        /* 大屏幕强制不显示侧边栏 */
        .left-sider {
            display: none !important;
        }
    }

    /* 小屏幕显示侧边栏 */
    @media screen and (max-width: 901px) {
        .ivu-layout-sider-zero-width-trigger {
            display: block !important;
        }
    }

</style>
<template>
    <div class="layout">
        <Layout>
            <Sider class="left-sider" breakpoint="md" collapsible :default-collapsed="true" :collapsed-width="0"
                   v-model="isCollapsed">
                <TopSider></TopSider>
                <div slot="trigger"></div>
            </Sider>
            <Layout>
                <Header>
                    <TopMenu></TopMenu>
                </Header>
                <Content class="content">

                    <TopBreadcrumb></TopBreadcrumb>

                    <Card class="content-card">
                        <router-view></router-view>

                    </Card>
                    <MyFooter></MyFooter>
                </Content>

            </Layout>
        </Layout>
        <BackTop></BackTop>
    </div>
</template>
<script>

    import TopMenu from './components/TopMenu'
    import TopSider from './components/TopSider'
    import TopBreadcrumb from './components/TopBreadcrumb'
    import MyFooter from './components/Footer'

    export default {
        data () {
            return {
                isCollapsed: false
            }
        },
        mounted () {

        },
        beforeDestroy () {

        },
        methods: {},
        components: {
            TopMenu: TopMenu,
            TopSider: TopSider,
            TopBreadcrumb: TopBreadcrumb,
            MyFooter: MyFooter,
        },
    }
</script>
