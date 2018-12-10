<template>
  <div>

    <Card style="width:100%">
      <div slot="title">
        <p style="display: initial;">
          <Icon type="ios-list-box-outline"/>
          爬虫列表
        </p>
        <div class="sortBox" style="float:right;line-height:30px;">
          <Button size="small" icon="ios-add-circle-outline" v-if="!srotSwitch" @click="addSpider">添加爬虫</Button>
          <Button size="small" type="primary" icon="ios-cloud-upload-outline" v-if="srotSwitch" @click="saveSort">保存
          </Button>
          排序：
          <i-switch v-model="srotSwitch"/>
        </div>
      </div>


      <SortableList lockAxis="y"
                    v-model="spiders"
                    :useDragHandle="true"
                    :transitionDuration="300"
                    @sort-end="sortEnd"
                    @input="saveLines"
      >
        <SortableItem v-for="(spider, index) in spiders" :index="index" collection="lines" :showHandle="srotSwitch"
                      :key="index">

          <Card>
            <Row>
              <Col span="5">
              {{ spider.name }}</Col>
              <Col span="5">
              {{ spider.project }}</Col>
              <Col span="10">
              {{ spider.link }}</Col>
              <Col span="4">

              <i-switch v-model="spider.enable" @on-change="enableSpider(spider.id, spider.enable)">
                <span slot="open">开</span>
                <span slot="close">关</span>
              </i-switch>
              <Button size="small" type="info" icon="ios-create-outline" @click="spiderEdit(spider.id)"></Button>
              <Poptip confirm title="确定删除该爬虫?" @on-ok="spiderDel(spider.id)">
                <Button size="small" ghost type="error" icon="ios-trash"></Button>
              </Poptip>
              <span v-handle class="handle" v-if="srotSwitch" style=""><Icon type="md-move"/></span>
              </Col>
            </Row>
          </Card>
        </SortableItem>
      </SortableList>


      <Spin size="large" v-if="loading"></Spin>

    </Card>

    <Modal
      v-model="showEditModel"
      :title="modelTitle"
      @on-ok="spiderSave"
    >
      <Form :model="formData" :label-width="80">
        <FormItem label="名称">
          <Input v-model="formData.name" placeholder="爬虫名称"></Input>
        </FormItem>
        <FormItem label="链接">
          <Input v-model="formData.link" placeholder="爬取起始链接"></Input>
        </FormItem>
        <FormItem label="项目名称">
          <Input v-model="formData.project" placeholder="爬虫的项目名称"></Input>
        </FormItem>
        <FormItem label="是否启用">
          <i-switch v-model="formData.enable" size="large">
            <span slot="open">是</span>
            <span slot="close">否</span>
          </i-switch>
        </FormItem>
      </Form>
    </Modal>
  </div>
</template>

<script>
  import {ContainerMixin, ElementMixin} from 'vue-slicksort';
  import {HandleDirective} from 'vue-slicksort';
  //  import {SlickList, SlickItem} from 'vue-slicksort';
  import SortableItem from '_v/data/subject/lines/SortableItem.vue'
  import SortableList from '_v/data/subject/lines/SortableList.vue'


  import {getSpiders, saveSpider, getSpider, delSpider, setSpiderSort} from '@/api/data'

  export default {
    name: 'spider',
    props: ['ownerId', 'spiderType'],
    directives: {handle: HandleDirective},
    data() {
      return {
        srotSwitch: false,
        spiders: [],
        changeListIndex: false,
        newSpiders: [],

        loading: true,


        // 编辑属性
        showEditModel: false,
        formData: {
          id: '', // id
          name: '', // 名称
          order: 999, // 播放器
          spider_type: '', // 爬虫类型
          owner: '', // 拥有者ID
          link: '', // 爬取URL
          project: '', // 项目名称
          enable: true, // 是否启用
        },

        // 对话框类型 0 新建, 1 编辑
        modelType: 0,

      };
    },
    computed: {
      modelTitle(){
        return (this.modelType ? '编辑' : '添加') + '爬虫';
      },
    },
    methods: {
      initData(){
        let that = this;
        that.loading = false;
        return new Promise(function (resolve, reject) {
          getSpiders(that.ownerId, that.spiderType).then(res => {
            that.spiders = res.data.results;
            console.log('载入爬虫成功');
            that.loading = false;
            resolve()
          }, res => {
            console.log('载入爬虫失败');
          })
//          .then(() => {
//          console.log('载入播放线路完成');
//        })
        });
      },
      sortEnd(e){
        console.log(e.event, e.newIndex, e.oldIndex, e.collection);
        if (e.newIndex != e.oldIndex)
          this.changeListIndex = true;
      },
      saveLines(newSpiders){
        this.newSpiders = newSpiders;
      },

      saveSpiderSort(){
        let that = this;
        return new Promise(function (resolve, reject) {
          if (that.changeListIndex) {
            console.log('修改了列表排序, 新顺序：', that.newSpiders.map(l => l.id))
            let data = {
              sid: that.ownerId,
              indexs: that.newSpiders.map(l => l.id),
            };
            setSpiderSort(data).then(res => {
              console.log('修改了列表排序成功');
              that.newSpiders = [];
              that.changeListIndex = false;
              resolve();
            }, res => {
              console.log('修改了列表排序失败');
              this.$Message.error(res.data);
              reject();
            })
//              .then(() => {
//              console.log('修改了列表排序完成');
//            });
          } else {
            resolve();
          }
        });

      },
      saveSort(){
        let that = this;
        that.saveSpiderSort()
          .then(() => {
            that.$Message.success('排序成功');
            that.srotSwitch = false;
          }).catch(() => {
          that.$Message.error('排序失败');

        })


      },
      spiderEdit(spiderId){
        let that = this;
        console.log('编辑爬虫', spiderId);
        getSpider(spiderId).then(res => {
          let data = res.data;
          console.log('获取到爬虫', res.data);
          let add_time = new Date(data.add_time);
          that.formData = data;
          that.modelType = 1;
          that.showEditModel = true;
        }, res => {
          console.log('获取爬虫信息失败', res.data);
        }).then(() => {
          console.log('获取爬虫信息完成');
        });
      },
      spiderDel(spiderId){
        let that = this;
        console.log('删除爬虫', spiderId);
        delSpider(spiderId).then(res => {
          console.log('删除爬虫成功', res.data);
          that.$Message.success('删除成功');
          // 将元素删除
//          video.dom.remove();
          for (let i = 0; i < that.spiders.length; i++) {
            if (that.spiders[i].id === spiderId) {
              that.spiders.splice(i, 1);
              break
            }
          }

        }, res => {
          console.log('删除爬虫失败', res.data);
        }).then(() => {
          console.log('删除爬虫完成');
        });
      },
      enableSpider(spiderId, enable){
        let that = this;
        console.log('修改爬虫启用状态', spiderId, enable);

        saveSpider({id: spiderId, enable: enable}).then(res => {
          console.log('保存启用状态成功', res.data);

        }, res => {
          console.log('保存启用状态失败', res.data);
        }).then(() => {
          console.log('保存启用状态完成');
        });

      },
      spiderSave(){
        let that = this;
        let data = this.formData;

        saveSpider(data).then(res => {
          console.log('保存视频信息成功', res.data);

          that.$Message.success('保存成功');
          // 重新获取数据，并强制刷新组件
          that.initData();


        }, res => {
          console.log('保存视频信息失败', res.data);
        }).then(() => {
          console.log('保存视频信息完成');
        });
      },
      /**
       * 添加爬虫
       */
      addSpider(line){

        this.formData = {
          name: `${this.spiderType}_${this.ownerId}_`, // 名称
          order: 999, // 播放器
          spider_type: this.spiderType, // 爬虫类型
          owner: this.ownerId, // 拥有者ID
          link: '', // 爬取URL
          project: '', // 项目名称
          enable: true, // 是否启用
        };
        this.modelType = 0;
        this.showEditModel = true;
      },
    },
    components: {

      SortableList,
      SortableItem,
//      SlickList,
//      SlickItem,

    }
    ,
    mounted()
    {
      console.log('spider created', this.ownerId);
      this.initData();
    }
  }
  ;

</script>
