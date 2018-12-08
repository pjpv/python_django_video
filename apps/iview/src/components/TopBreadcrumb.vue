<template>

    <Breadcrumb :style="{margin: '20px 0'}">
        <BreadcrumbItem>
            <router-link :to="{ name: 'index', params: {} }">首页</router-link>
        </BreadcrumbItem>

        <BreadcrumbItem v-for="(item, index) in breadData" :key="index">
                        <span v-if="item.id">
                         <router-link :to="{ name: item.type, params: {id:item.id} }">{{ item.name }}</router-link>
                        </span>
            <span v-else>
                         {{ item.name }}
                        </span>
        </BreadcrumbItem>
    </Breadcrumb>
</template>

<script>
    export default {
        name: 'TopBreadcrumb',
        data() {
            return {}
        },
        computed: {

            breadData() {
                let path = this.$route.path;
                let name = this.$route.name;
                let d = [];
                if (this.$store.state.currentCategory) {
                    let category = this.$store.state.currentCategory;
                    let subject = this.$store.state.currentSubject;
                    let video = this.$store.state.currentVideo;
                    switch (name) {
                        case 'category':
                            d = [{name: category.name, id: category.id, type: 'category'}];
                            break;
                        case 'subject':
                            d = [{name: category.name, id: category.id, type: 'category'}, {
                                name: subject.name,
                                id: subject.id,
                                type: 'subject'
                            },];
                            break;
                        case 'play':
                            d = [{name: category.name, id: category.id, type: 'category'}, {
                                name: subject.name,
                                id: subject.id,
                                type: 'subject'
                            }, {name: video.name, id: video.id},];
                            break;
                    }
                } else {
                    this.$nextTick(() => {
                        this.breadData();
                    })
                }
                return d;
            },
        },
        methods: {
            selectMenu(name) {
            },

        },
    }
</script>

<style lang="css">
</style>
