<style lang="css">
    .content-card {
        /*background: #eee !important;*/
    }

    .category {
        margin: 10px 0;
    }

    .subject img {
    }

    .subject .subject-title {
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;

        display: block;
        padding-top: 10px;
    }

</style>
<template>
    <div class="index">
        <Row style="" v-if="categorys.length">
            <Col v-for="category in categorys" :key="category.id" span="24" class="">
            <Card :bordered="true">
                <p slot="title">
                    <Icon type="ios-film-outline"></Icon>
                    {{ category.name }}
                </p>
                <router-link slot="extra" :to="{ name: 'category', params: {id: category.id } }">
                    <Icon type="md-more"/>
                    更多
                </router-link>

                <Row style="" v-if="category.list.length" >
                    <Col :xs="12" :sm="6" :md="5" :lg="4" v-for="subject in category.list" :key="subject.id"
                         class="subject">
                    <!--<router-link :to="{ name: 'subject', params: {cid: category.id, id: subject.id} }" :title="subject.name">-->
                    <!--<Card class="cover" style="" :bordered="false" :shadow="false" :disHover="true">-->
                    <!--<div style="text-align:center">-->
                    <!--<div  class="cover-img" :style="backgroundImgUrl(subject.cover)" :src="subject.cover"></div>-->
                    <!--<h3 class="subject-title">{{ subject.name }}</h3>-->
                    <!--</div>-->
                    <!--</Card>-->
                    <!--</router-link>-->
                    <subject-cover :subject="subject" :category="category"></subject-cover>
                    </Col>
                </Row>
                <loadingCard v-else></loadingCard>
            </Card>
            </Col>
        </Row>
        <loadingCard v-else></loadingCard>
    </div>
</template>
<script>

    //    import {getIndexList}  from '../api/api'
//    import SubjectCover from '../components/SubjectCover'
//    import loadingCard from '../components/loadingCard.vue'
    export default {
        components: {
            SubjectCover:resolve => {require(['../components/SubjectCover'], resolve)},//懒加载
            loadingCard:resolve => {require(['../components/loadingCard'], resolve)},//懒加载
        },
        created(){
            this.init();
        },
        data(){
            return {
                categorys: []
            }
        },
        methods: {
            backgroundImgUrl(url) {
                return `background-image: url(${url});`;
            },
            init(){

                this.$api.getIndexList().then(res => {
                    console.log(res);
                    this.categorys = res.results;
                }, () => {
                    console.log('http get error')
                })
            }

        },
        watch: {
            '$route' (to, from) {
                console.log('Subject watch init');

                if (from.name != 'index')
                    this.init();
            }
        },
    }
</script>
