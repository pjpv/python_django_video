<template>
    <div class="top-menu">
        <Menu mode="horizontal" theme="dark" :active-name="activeName" @on-select='selectMenu'>
            <router-link to="/">
                <div class="layout-logo">
                    <img src="../images/logo4.png" alt="">
                </div>
            </router-link>

            <div class="layout-nav" style="width: auto;right: 20px;position: absolute;">


                <Input suffix="ios-search" placeholder="搜索" style="" search @on-search="search"
                       id="searchText" ref="searchInput">
                <Select placeholder="全部" v-model="selectCategory" slot="prepend" style="width: 80px">
                    <Option value="0">全部</Option>
                    <Option v-for="item in headCategory" v-model="item.id" :key="item.id">{{ item.name }}</Option>
                </Select>
                </Input>
                <!--<MenuItem name="0">-->
                <!--<Icon type="ios-home"/>-->
                <!--首页-->
                <!--</MenuItem>-->
                <MenuItem v-for="(item, index) in headCategory" :name="index" :key="item.id">
                    <Icon :type="item.icon"/>
                    {{ item.name }}
                </MenuItem>

            </div>
        </Menu>

    </div>
</template>
<script>
    export default {
        data() {
            return {
                selectCategory: 0,
            }
        },
        computed: {
            url: function () {
                console.log(this.$route.path);
                console.log(this.$route);
                return '1'
            },
            activeName() {
                let path = this.$route.path;
                return path;
            },
            headCategory(){
                if (!this.$store.state.headCategory) {
                    console.log('TopMenu headCategory');
                    this.$store.commit('initHeadCategory');
                    return null;
                } else {
                    return this.$store.state.headCategory;
                }

            }
        },
        methods: {
            selectMenu(name) {
                console.log(name)
                let category = this.headCategory[name];
                // 首页
//                if (i <= -1) {
//                    this.$router.push('/')
//                    return
//                }
                // 分类
                this.$router.push({
                    name: 'category',
                    params: {
                        id: category.id,
                        name: category.name,
                        title: category.name,
                    }
                })
            },
            search(text){
                console.log(`搜索[${text}]`);
                this.$refs.searchInput.blur(); // 失去焦点，收起键盘
                if (!(text.replace(/ /g, '').length))return;
                this.$router.push({
                    name: 'search',
                    query: {
                        search: text,
                        category: this.selectCategory === 0 ? '' : this.selectCategory,
                    }
                })
            },
        }
    }
</script>
<style media="screen">
    .layout-logo {
        width: 100px;
        height: 40px;
        background: #5b6270;
        border-radius: 3px;
        float: left;
        position: relative;
        top: 12px;
        left: 20px;
    }

    .layout-logo > img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .layout-nav {
        width: 420px;
        margin: 0 auto;
        margin-right: 20px;
    }

    #searchText {
        width: auto;
        float: right;
        height: 30px;
        top: 15px;
        position: absolute;
        width: 150px;
        right: -70px;;
    }

    .layout-nav .ivu-menu-item {
        display: none;
    }

    @media screen and (min-width: 901px) {
        .layout-nav .ivu-menu-item {
            display: block !important;
        }


        #searchText {
            width: auto;
            float: left;
            position: relative;
            right: unset;
        }
    }

    /* 内容居中 */
    .top-menu {
        margin: 0 auto;
    }

    @media screen and (min-width: 1201px) {

    }

    @media screen and (max-width: 1200px) {

    }

    @media screen and (max-width: 1024px) {

        .top-menu {
            width: 94%;
        }

        #searchText {
            width: 150px;
            position: relative;

        }
    }

    @media screen and (max-width: 901px) {

    }

    @media screen and (max-width: 768px) {
        .top-menu {
            width: 90%;
            position: relative;
        }

        #searchText {
            width: 200px;

        }
    }

    @media screen and (max-width: 500px) {
        .top-menu {
            width: 98%;
            position: absolute;
            left: 20px;
        }

        #searchText {
            right: 0px;
            width: 200px;
        }
    }

    @media screen and (max-width: 425px) {
        .top-menu {
            width: 98%;
            position: absolute;
            left: 20px;
        }

        #searchText {
            right: 0px;
            width: 200px;
        }
    }

    @media screen and (max-width: 375px) {
        .top-menu {
            width: 98%;
            position: absolute;
            left: 20px;
        }

        #searchText {
            right: 0px;
            width: 170px;
        }
    }

    @media screen and (max-width: 320px) {
        .top-menu {
            width: 100%;
            position: absolute;
            left: 20px;
        }

        #searchText {
            right: 0px;
            width: 150px;
        }
    }


</style>
