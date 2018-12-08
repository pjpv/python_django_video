<template>

    <Menu :active-name="activeName" theme="dark" width="auto" :class="menuitemClasses" @on-select='selectMenu'>
        <div class="sider-logo">
            <img src="../images/logo4.png" alt="">
        </div>
        <MenuItem name="index" :to="{name: 'index'}">
            <Icon type="ios-home"></Icon>
            <span>首页</span>
        </MenuItem>
        <MenuItem v-for="item in headCategory" :name="item.id"
                  :to="{name: 'category',params: {id: item.id,name: item.name,title: item.name}}" :key="item.id">
            <Icon :type="item.icon"/>
            {{ item.name }}
        </MenuItem>
    </Menu>
</template>
<script>
    export default {
        name: 'TopSider',
        data() {
            return {}
        },
        computed: {
            url: function () {
                console.log(this.$route.path);
                console.log(this.$route);
                return '1'
            },
            headCategory(){
                if (!this.$store.state.headCategory) {
                    console.log('TopSider headCategory');
                    this.$store.dispatch('initHeadCategory');
                    return null;
                } else {
                    return this.$store.state.headCategory;
                }

            },
            activeName() {
                let path = this.$route.path;
                let name = this.$route.name;
                // 首页
                if (path === '/')
                    return 'index';
                let category = this.$store.state.currentCategory;
                if (!category.id) {
//                    throw new Error('未初始化')
                    return ''
                }
                console.log('name', name);
                console.log('category', category);
//                let video = this.$store.state.currentVideo;
                switch (name) {
                    case 'category':
                    case 'subject':
                    case 'play':
                        return category.id;
                        break;
                }
                return '';
            },
            menuitemClasses: function () {
                return [
                    'menu-item',
                    this.isCollapsed ? 'collapsed-menu' : ''
                ]
            }
        },
        methods: {
            selectMenu(name) {

                document.querySelector('.ivu-layout-sider-zero-width-trigger').click();

//                console.log(name)
//                let category = this.headCategory[name];
////                 首页
//                if (name === 'index') {
//                    this.$router.push('/')
//                    return
//                } else if (name === 'logo') {
//                    return
//                }
//                // 分类
//                this.$router.push({
//                    name: 'category',
//                    params: {
//                        id: category.id,
//                        name: category.name,
//                        title: category.name,
//                    }
//                })
            }
        }
    }
</script>
<style media="screen">

    .ivu-menu-vertical {

        height: 100%;
        /* 需要在顶部菜单上面 */
        z-index: 1001 !important;
    }

    .ivu-layout-sider {
        position: absolute !important;
        height: 100% !important;;
    }
</style>
<style scoped>
    .sider-logo {
        width: 100px;
        height: 40px;
        background: #5b6270;
        border-radius: 3px;
        margin: 10px auto;
    }

    .sider-logo > img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .layout {
        border: 1px solid #d7dde4;
        background: #f5f7f9;
        position: relative;
        border-radius: 4px;
        overflow: hidden;
    }

    .layout-header-bar {
        background: #fff;
        box-shadow: 0 1px 1px rgba(0, 0, 0, .1);
    }

    .menu-item span {
        display: inline-block;
        overflow: hidden;
        width: 69px;
        text-overflow: ellipsis;
        white-space: nowrap;
        vertical-align: bottom;
        transition: width .2s ease .2s;
    }

    .menu-item i {
        transform: translateX(0px);
        transition: font-size .2s ease, transform .2s ease;
        vertical-align: middle;
        font-size: 16px;
    }

    .collapsed-menu span {
        width: 0px;
        transition: width .2s ease;
    }

    .collapsed-menu i {
        transform: translateX(5px);
        transition: font-size .2s ease .2s, transform .2s ease .2s;
        vertical-align: middle;
        font-size: 22px;
    }


</style>