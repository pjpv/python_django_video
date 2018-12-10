<template>
  <div class="category-detail">
    <Row>
      <Col span="18">
      <Card>

        <Row>
          <Col span="18">
          <Form :label-width="80" :model="formData">

            <FormItem label="分类名称">
              <Input v-model="formData.name" icon="android-list"/>
            </FormItem>

            <FormItem label="是否顶部显示">
              <i-switch v-model="formData.inHead" size="large">
                <span slot="open">是</span>
                <span slot="close">否</span>
              </i-switch>
            </FormItem>

            <FormItem label="排序">
              <InputNumber v-model="formData.order" placeholder="Enter something..."></InputNumber>
            </FormItem>

          </Form>

          </Col>

        </Row>
      </Card>
      <!-- 爬虫 -->
      <spider v-if="isInit" :ownerId="categoryId" :spiderType="0"></spider>

      </Col>
      <Col span="6" class="padding-left-10">
      <Card>
        <p slot="title">
          <Icon type="ios-paper-plane-outline"/>
          发布
        </p>
        <Form :label-width="80"></Form>

        <Row class="margin-top-20 publish-button-con">
          <span class="publish-button"><Button>预览</Button></span>
          <span class="publish-button"><Button type="primary" @click="saveData">保存</Button></span>
        </Row>
      </Card>
      </Col>
      <Spin size="large" fix v-if="loading"></Spin>
    </Row>
  </div>
</template>

<script>
  import {getCategory, saveCategory} from '@/api/data'
  import Spider from '_v/data/spider/spider.vue'

  /* 字段名称 */
  const fieldName = {
    id: 'ID',
    name: "标题",
    order: "排序",
    isHead: "是否顶部显示",
  };

  export default {
    name: 'category_detail',
    data () {
      return {
        isInit: false,
        loading: false,
        categoryId: '',
        formData: {
          id: '',
          name: '',
          order: 999,
          isHead: false,
        }
      };
    },
    methods: {
      loadInfo(){
        let id = this.$route.params.id;
        this.categoryId = id;
        getCategory(id).then(res => {
          console.log('getCategory', res)
          this.formData = res.data;
          this.isInit = true;
        }, res => {

        })
      },
      saveData(){
        // 保存
        let data = this.formData;
        this.loading = true;
        saveCategory(data).then(res => {
          console.log('保存主题成功', res);
          this.$Message.success('保存成功');
        }, res => {
          console.log('保存主题失败', res);
          let err = '错误信息：';
          if (res.response && res.response.status === 400) {
            for (let key of Object.keys(res.response.data)) {
              err += `<br>${fieldName[key]}：${res.response.data[key]}`;
            }
          }

          this.$Notice.error({
            title: '保存失败',
            desc: err,
            duration: 0,
          });
//          this.$Message.error(err);
        }).then(() => {
          console.log('保存主题完成');
          this.loading = false;
        })
      }
    },
    computed: {},
    created(){
    },
    mounted () {
      this.loadInfo();
    },
    destroyed () {
    },
    components: {
      Spider
    },
    watch: {
      '$route' (to, form) {
//        console.log('line.line watch init');
//        console.log('to', to);
//        console.log('form', form);
//        if (to.name === 'subject_detail' && to.params.id != this.subjectId) {
//          this.loadInfo();
//          this.reset();
//        }
      },
    },
  };
</script>
<style>
  .category-detail .ivu-form-item {
    margin-bottom: 5px;
  }
</style>
