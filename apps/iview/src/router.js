const routers = [{
        name: 'index',
        path: '/',
        meta: {
            title: '首页',
            keepAlive: true
        },
        component: (resolve) => require(['./views/index.vue','./components/SubjectCover.vue'], resolve)
    },
    {
        name: 'search',
        path: '/search/',
        meta: {
            title: '搜索',
            keepAlive: true
        },
        component: (resolve) => require(['./views/search.vue'], resolve)
    },
    {
        name: 'category',
        path: '/:id/',
        meta: {
            title: '分类',
            keepAlive: true
        },
        component: (resolve) => require(['./views/category.vue'], resolve)
    },
    {
        name: 'subject',
        path: '/:cid/:id/',
        meta: {
            title: '主题',
            keepAlive: false
        },
        component: (resolve) => require(['./views/subject.vue'], resolve)
    },
    {
        name: 'play',
        path: '/:cid/:sid/:vid',
        meta: {
            title: '播放',
            keepAlive: true
        },
        component: (resolve) => require(['./views/play/play.vue'], resolve)
    },
];
export default routers;
