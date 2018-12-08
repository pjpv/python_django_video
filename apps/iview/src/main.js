import Vue from 'vue';
import Vuex from 'vuex'
import iView from 'iview';
import VueRouter from 'vue-router';
import Routers from './router';
import Meta from 'vue-meta'
// axios
import axios from 'axios'
import Qs from 'qs'

import Util from './libs/util';
import App from './app.vue';

// 图片懒加载
import VueLazyload from 'vue-lazyload'

import 'iview/dist/styles/iview.css';

// vuex store
import store from './store/store'

// API
import api from  './axios/index'

Vue.use(VueRouter);
Vue.use(iView);
Vue.use(Vuex);
Vue.use(Meta);
// axios
Vue.prototype.axios = axios;
Vue.prototype.qs = Qs;

// API
Vue.use(api);
// 图片懒加载
// Vue.use(VueLazyload)
Vue.use(VueLazyload, {
    preLoad: 1.3,
    // loading: 'dist/loading.gif',
    error: '//ws1.sinaimg.cn/small/6260f60dly1fxslxnwva9j206d07y0sy.jpg',
    loading: '//ws1.sinaimg.cn/large/6260f60dly1fxt87tx6fug20jo0k0tbx.gif',
    attempt: 1
});


Vue.prototype.$util = Util;

// 路由配置
const RouterConfig = {
    mode: 'history',
    routes: Routers,
    base: '/',
};
const router = new VueRouter(RouterConfig);

router.beforeEach((to, from, next) => {
    iView.LoadingBar.start();
    let title = to.params.title ? to.params.title : to.meta.title;
    Util.title(title);
    next();
});

router.afterEach((to, from, next) => {
    iView.LoadingBar.finish();
    window.scrollTo(0, 0);
});

/* 手动设置标题 */
// Vue.directive('title', {
//     inserted: function (el, binding) {
//         document.title = el.dataset.title + ' | ZFDev影视';
//     }
// });


export const app = new Vue({
    el: '#app',
    router: router,
    store,
    render: h => h(App),
    components: {},
    http: {
        root: '/root',
        headers: {
            Authorization: 'Basic YXBpOnBhc3N3b3Jk'
        }
    },
    metaInfo: {
        title: '首页',
        titleTemplate: '%s | ZFDev影视',
    }
});
