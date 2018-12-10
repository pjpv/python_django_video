<style lang="less">
  /*@import '../../../styles/common.less';*/
  @import './article-publish.less';
</style>
<style>
  .subject-detail .ivu-form-item {
    margin-bottom: 5px;
  }
</style>

<template>
  <div v-if="!resetPage" class="subject-detail">
    <Row>
      <Col span="18">
      <Card>

        <Row>
          <Col span="18">
          <Form :label-width="80">
            <!--:error="articleError" -->
            <FormItem label="标题">
              <Input v-model="name" @on-blur="handleArticletitleBlur" icon="android-list"/>
            </FormItem>

            <FormItem label="封面图片">
              <Input v-model="cover" icon="android-list"/>
            </FormItem>

            <FormItem label="主演">
              <Input v-model="actress" placeholder="Enter something..."></Input>
            </FormItem>
            <FormItem label="描述">
              <Input v-model="desc" type="textarea" :autosize="{minRows: 2,maxRows: 5}"
                     placeholder="Enter something..."></Input>
            </FormItem>
          </Form>

          </Col>
          <Col span="6" class="padding-left-10">
          <div>
            <div class=""
                 style="padding: 6px;box-shadow: rgba(0, 0, 0, 0.2) 0px 2px 4px -1px, rgba(0, 0, 0, 0.14) 0px 4px 5px 0px, rgba(0, 0, 0, 0.12) 0px 1px 10px 0px;margin: 0 auto;width: 200px;">
              <!--<img class="mdui-img-rounded"-->
              <!--style="display: block;width: 100%;border-radius: 4px;    min-height: 100px;"-->
              <!--v-lazy="subject.cover">-->
              <img :src="cover" alt="" style="width: 100%">
            </div>
          </div>
          </Col>
        </Row>
      </Card>
      <!-- 播放列表 -->
      <!--<Card>-->
      <lines v-if="isInit" :subjectId="subjectId"></lines>
      <!--</Card>-->
      <!-- 爬虫 -->
      <spider v-if="isInit" :ownerId="subjectId" :spiderType="1"></spider>

      </Col>
      <Col span="6" class="padding-left-10">
      <Card>
        <p slot="title">
          <Icon type="ios-paper-plane-outline"/>
          发布
        </p>
        <Form :label-width="80">
          <FormItem label="地区">
            <Input v-model="area" placeholder="Enter something..."></Input>
          </FormItem>
          <FormItem label="导演">
            <Input v-model="director" placeholder="Enter something..."></Input>
          </FormItem>
          <FormItem label="状态">
            <Select v-model="state">
              <Option v-bind:value="0">连载中</Option>
              <Option v-bind:value="1">全集</Option>
            </Select>
          </FormItem>
          <FormItem label="开播时间">
            <Row>
              <Col span="10">
              <DatePicker type="date" v-model="pub_date_date" placeholder="Select date"></DatePicker>
              </Col>
              <!--<Col span="1" style="text-align: center">-->
              <!-- -</Col>-->
              <!--<Col span="10">-->
              <!--<TimePicker type="time" v-model="pub_date_time" format="HH:mm" placeholder="Select time"></TimePicker>-->
              <!--</Col>-->
              <Col span="3">
              <Button size="small" icon="ios-clock" type="text" title="Now" shape="circle" @click="setPubDate"></Button>
              </Col>
            </Row>
          </FormItem>
          <FormItem label="提示">
            <Input v-model="tips" placeholder="Enter something..."></Input>
          </FormItem>
          <FormItem label="更新时间">
            {{update_time_date}} {{ update_time_time }}
            <!--<Row>-->
            <!--<Col span="11">-->
            <!--<DatePicker type="date" v-model="update_time_date" placeholder="Select date"></DatePicker>-->
            <!--</Col>-->
            <!--<Col span="2" style="text-align: center">-->
            <!-- -</Col>-->
            <!--<Col span="11">-->
            <!--<TimePicker type="time" v-model="update_time_time" format="HH:mm" placeholder="Select time"></TimePicker>-->
            <!--</Col>-->
            <!--</Row>-->
          </FormItem>
        </Form>

        <Row class="margin-top-20 publish-button-con">
          <span class="publish-button"><Button>预览</Button></span>
          <span class="publish-button"><Button type="primary" @click="saveSubject">保存</Button></span>
          <!--<span class="publish-button"><Button :loading="false" icon="ios-checkmark"-->
          <!--style="width:90px;" type="primary">发布</Button></span>-->
        </Row>
      </Card>

      <div class="margin-top-10">
        <Card>
          <p slot="title">
            <Icon type="navicon-round"></Icon>
            所属分类
          </p>
          <RadioGroup v-model="category" vertical>
            <Radio :label="c.id" v-for="c in categoryList" :key="c.id">
              <span>{{ c.name }}</span>
            </Radio>
          </RadioGroup>
        </Card>
      </div>
      <div class="margin-top-10">
        <Card>
          <p slot="title">
            <Icon type="ios-pricetags-outline"></Icon>
            标签
          </p>
          <vTags :source.sync="tags_list" v-if="tags_list && !tagsResetSwitch"></vTags>
        </Card>
      </div>
      </Col>

      <Spin size="large" fix v-if="loading"></Spin>
    </Row>
  </div>
</template>

<script>
  import {getSubject, saveSubject, getCategorys} from '@/api/data'

  import Lines from './lines/lines.vue'
  //  import spider from './spider/spider.vue'
  import spider from '_v/data/spider/spider.vue'
  import vTags from '../../components/tags'

  /* 时间格式 */
  const datetime = function (date) {
    if (date) {
      this.dateobj = new Date(date);
    } else {
      this.dateobj = new Date();
    }
    this.date = this.getDate();
    this.time = this.getTime();
  };
  datetime.prototype.getDate = function () {
    let year = this.dateobj.getFullYear(),
      month = this.dateobj.getMonth() + 1,
      day = this.dateobj.getDate();
    return `${year}-${month}-${day}`;
  };
  datetime.prototype.getTime = function () {
    let hours = this.dateobj.getHours(),
      minutes = this.dateobj.getMinutes(),
      seconds = this.dateobj.getSeconds();
    return `${hours}:${minutes}:${seconds}`;
  };
  datetime.prototype.getDateTime = function () {
    let d = `${this.date} ${this.time}`;
    return d;
  };
  datetime.prototype.setDateTime = function (date, time) {
    this.date = date;
    this.time = time;
    return this.getDateTime();
  };

  /* 字段名称 */
  const fieldName = {
    actress: "主演",
    area: "地区",
    category: '分类',
    cover: "封面图片",
    desc: "描述",
    director: "导演",
    id: 'ID',
    name: "标题",
    tips: "提示",
    pub_date: "开播时间",
    state: '状态',
    tags: "标签",
    update_time: "更新时间",
  };

  export default {
    name: 'subject_detail',
    data () {
      return {
        viewName: 'subject_detail_1',
        offenUsedClass: [],
        classificationList: [],
        articleTagList: [],

        resetPage: false,
        loading: false,

        isInit: false,

        // 分类列表
        categoryList: [],

        // 主题信息
        subjectId: '',

        actress: "",
        area: "",
        category: '',
        cover: "",
        desc: "",
        director: "",
        id: '',
        name: "",
        tips: "",
        pub_date: "",
        pub_date_date: '',
        pub_date_time: '',
        state: 0,
        tags: "",
        update_time: "",
        update_time_date: '',
        update_time_time: '',

        tags_list: '',
        tagsResetSwitch: false,

      };
    },
    methods: {
      reset(){
        this.resetPage = true;
        this.$nextTick(() => {
          this.resetPage = false;
        })
      },
      tagsReset(){
        this.tagsResetSwitch = true;
        this.$nextTick(() => {
          this.tagsResetSwitch = false;
        });
      },
      /**/
      loadInfo(){
        let that = this;
        let sid = that.$route.query.id;
        that.subjectId = sid;
        that.isInit = true;
        getSubject(sid).then(res => {

          that.actress = res.data.actress;
          that.area = res.data.area;
          that.category = res.data.category;
          that.cover = res.data.cover
          that.desc = res.data.desc;
          that.director = res.data.director;
          that.id = res.data.id;
          that.name = res.data.name;
          that.tips = res.data.tips;
          that.pub_date = new datetime(res.data.pub_date);
          that.pub_date_date = that.pub_date.getDate();
          that.pub_date_time = that.pub_date.getTime();
          that.state = res.data.state;
          that.tags = res.data.tags;
          that.tags_list = res.data.tags.split(',');

          that.update_time = new datetime(res.data.update_time);
          that.update_time_date = that.update_time.getDate();
          that.update_time_time = that.update_time.getTime();
          that.tagsReset();
          console.log('载入成功', res);
        }, res => {
          console.log('载入失败', res);

        }).then(() => {
          console.log('载入完成');
        })
      },
      /* 设置发布时间为当前时间 */
      setPubDate(){
        this.pub_date = new datetime();
        this.pub_date_date = this.pub_date.getDate();
        this.pub_date_time = this.pub_date.getTime();
      },
      /**
       * 时间日期字符串 分割日期和时间
       * 返回数组 [0]日期，[1]时间
       */
      date2str(datetime){
        let date = new Date(datetime),
          year = date.getFullYear(),
          month = date.getMonth() + 1,
          day = date.getDate(),
          hours = date.getHours(),
          minutes = date.getMinutes(),
          seconds = date.getSeconds();
        return [`${year}-${month}-${day}`, `${hours}:${minutes}:${seconds}`];
      },
      /* 文本合并成完整时间 */
      margeDateTime(date, time){
        let d = new Date(date),
          year = d.getFullYear(),
          month = d.getMonth() + 1, // 月份+1
          day = d.getDate();
        return `${year}-${month}-${day} ${time}`;
      },
      handleArticletitleBlur () {
        if (this.name.replace('/ /g', '').length === 0)
          this.$Message.error('文章标题不可为空哦');
      },
      setClassificationInAll (selectedArray) {
        this.classificationFinalSelected = selectedArray.map(item => {
          return item.title;
        });
        localStorage.classificationSelected = JSON.stringify(this.classificationFinalSelected);  // 本地存储所选目录列表
      },
      handlePreview () {
        let date = new Date();
        let year = date.getFullYear();
        let month = date.getMonth() + 1;
        let day = date.getDate();
        let hour = date.getHours();
        let minute = date.getMinutes();
        let second = date.getSeconds();
        localStorage.publishTime = year + ' 年 ' + month + ' 月 ' + day + ' 日 -- ' + hour + ' : ' + minute + ' : ' + second;
      },
      handlePublish () {
        this.$Notice.success({
          title: '保存成功',
          desc: '文章《' + this.articleTitle + '》保存成功'
        });
      },

      // 保存
      saveSubject(){
        let data = {
          actress: this.actress,
          area: this.area,
          category: this.category,
          cover: this.cover,
          desc: this.desc,
          director: this.director,
          id: this.subjectId,
          name: this.name,
          tips: this.tips,
          pub_date: this.margeDateTime(this.pub_date_date, this.pub_date_time),
          state: this.state,
          tags: this.tags_list.join(','),
          update_time: this.margeDateTime(this.update_time_date, this.update_time_time),
        };
        this.loading = true;
        saveSubject(data).then(res => {
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
      },
      /* 初始化分类信息 */
      initCategorys(){
        getCategorys().then(res => {
          this.categoryList = res.data.results
        })
      },
    },
    computed: {
      completeUrl () {
        let finalUrl = this.fixedLink + this.articlePath;
        localStorage.finalUrl = finalUrl;  // 本地存储完整文章路径
        return finalUrl;
      }
    },
    created(){
      // 初始化分类
      this.initCategorys();
    },
    mounted () {
      /* 载入信息 */
      this.loadInfo();

    },
    destroyed () {
    },
    components: {
      Lines,
      vTags,
      spider,
    },
    watch: {
      '$route' (to, form) {
        console.log('line.line watch init');
        console.log('to', to);
        console.log('form', form);
        if (to.name === 'subject_detail' && to.params.id != this.subjectId) {
          this.loadInfo();
          this.reset();
        }
      },
    },
  };
</script>
