import Vue from 'vue';
import Vuex from 'vuex';
import * as main from '../main'
// import {getCategory, getHeadCategorys} from '../api/api'

Vue.use(Vuex);


export default new Vuex.Store({
    state: {
        currentCategory: {},
        currentSubject: {},
        currentVideo: {},
        headCategory: null,
    },
    actions: {
        initCategory(context, cid){

            console.log('app', main.app);
            context.commit("initCategory", cid);
        },
        initHeadCategory(context){
            context.commit("initHeadCategory");
        },
        initSubject(context, sid){

            console.log('app', main.app);
            context.commit("initSubject", sid);
        },
    },
    mutations: {
        initCategory(state, cid){
            main.app.$api.getCategory(cid).then(res => {
                if (res.hasOwnProperty('id')) {
                    state.currentCategory = res;
                } else {
                    console.log('分类错误')
                }
            })
        },
        initHeadCategory(state){
            setTimeout(function () {

                try {
                    main.app.$api.getHeadCategorys().then(res => {
                        if (res.hasOwnProperty('count')) {
                            state.headCategory = res.results;
                        } else {
                            console.log('获取菜单失败')
                        }
                    })
                } catch (e) {
                    throw new Error('未完成初始化')
                }
            }, 100);
        },
        initSubject(state, sid){
            main.app.$api.getSubject(sid).then(res => {
                if (res.hasOwnProperty('id')) {
                    state.currentSubject = res;
                    state.currentCategory = res.category;
                } else {
                    console.log('分类错误')
                }
            })
        },
    },
    getters: {}
})