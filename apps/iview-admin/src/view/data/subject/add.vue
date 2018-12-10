<style lang="less">
  /*@import '../../../styles/common.less';*/
  @import './article-publish.less';
</style>

<template>
  <div v-if="!resetPage">
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
              <DatePicker type="date" v-model="pub_date_date" placeholder="Select date"></DatePicker>
              <!-- - -->
              <!--<TimePicker type="time" v-model="pub_date_time" format="HH:mm" placeholder="Select time"></TimePicker>-->
              <Button size="small" icon="ios-clock" type="text" title="Now" shape="circle" @click="setPubDate"></Button>
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

      </Col>
      <Col span="6" class="padding-left-10">
      <Card>
        <p slot="title">
          <Icon type="paper-airplane"></Icon>
          豆瓣导入
        </p>
        <p>
          导入：
        </p>
        <Input placeholder="https://movie.douban.com/subject/12345678/" v-model="doubanURL">
        <Button slot="append" class="doubanImportBtn" icon="ios-download-outline" @click="doubanImport"
                shape="circle"></Button>
        </Input>
        <Divider/>
        <p>
          搜索：
        </p>
        <!--<Input placeholder="影片名称" v-model="doubanName">-->
        <!--<Button slot="append" class="doubanImportBtn" icon="ios-search" @click="doubanSearch"-->
        <!--shape="circle"></Button>-->
        <!--</Input>-->
        <!--<AutoComplete-->
        <!--v-model="doubanName"-->
        <!--icon="ios-search"-->
        <!--placeholder="影片名称"-->
        <!--@on-change="doubanSearch"-->
        <!--@on-select="doubanSelect"-->
        <!--style="">-->
        <!--<div class="demo-auto-complete-item">-->
        <!--<div class="demo-auto-complete-group" style="min-height: 30px;">-->
        <!--&lt;!&ndash;<span>{{ doubanName }}</span>&ndash;&gt;-->
        <!--&lt;!&ndash;<a href="https://www.google.com/search?q=iView" class="external-link" target="_blank" style="float: right;">更多</a>&ndash;&gt;-->
        <!--</div>-->
        <!--<Option v-for="item in doubanSearchData" :value="item.id" :key="item.id">-->
        <!--<span class="douban-title">{{ item.title }}</span>-->
        <!--<span class="douban-year">{{ item.year }} 年</span>-->
        <!--</Option>-->
        <!--</div>-->
        <!--<a :href="'https://movie.douban.com/subject_search?cat=1002&search_text=' + doubanName" target="_blank"-->
        <!--class="external-link"-->
        <!--style="display: block;margin: 0 auto;padding: 4px;text-align: center;font-size: 12px;">查看所有结果</a>-->
        <!--</AutoComplete>-->
        <Poptip v-model="showDoubanSearchData" class="douban-search">

          <Input placeholder="https://movie.douban.com/subject/12345678/" v-model="doubanName" search @on-search="doubanSearch">
          <Button slot="append" class="doubanImportBtn" icon="ios-search" @click="doubanSearch"
                  shape="circle"></Button>
          </Input>
          <div slot="title"><i>搜索结果</i></div>
          <div slot="content">
            <div id="search_suggest" style="/* display: none; */top: 78px;left: 593.906px;"
                 v-if="doubanSearchData.length">
              <ul>
                <li :data-link="'https://movie.douban.com/subject/' + item.id + '/'" v-for="item in doubanSearchData"
                    :value="item.id" :key="item.id">
                  <a @click="doubanSelect(item.id)">
                    <img :src="item.img" width="40">
                    <p>
                      <em>{{ item.title }}</em> <span>{{ item.year }}</span>
                      <br>
                      <span>{{ item.sub_title }}</span>
                      <br>
                      <span v-if="item.type == 'tv'">
                        电视剧<span>共{{ item.episode }}集</span>
                      </span>
                      <span v-else-if="item.type == 'movie'">
                        电影
                      </span>
                    </p>
                  </a>
                </li>
              </ul>
            </div>
            <div style="lf">

            </div>
            <a :href="'https://movie.douban.com/subject_search?cat=1002&search_text=' + doubanName" target="_blank"
               class="external-link"
               style="display: block;margin: 0 auto;padding: 4px;text-align: center;font-size: 12px;">查看所有结果</a>

          </div>
        </Poptip>
      </Card>
      <Card>
        <p slot="title">
          <Icon type="paper-airplane"></Icon>
          发布
        </p>

        <Row class="margin-top-20 publish-button-con">
          <span class="publish-button"><Button>预览</Button></span>
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
          <!--<Tabs type="card">-->
          <!--<TabPane label="所有分类目录">-->
          <!--<div class="classification-con">-->
          <!--<Tree :data="classificationList" @on-check-change="setClassificationInAll" show-checkbox></Tree>-->
          <!--</div>-->
          <!--</TabPane>-->
          <!--<TabPane label="常用目录">-->
          <!--<div class="classification-con">-->
          <!--&lt;!&ndash;@on-change="setClassificationInOffen"&ndash;&gt;-->
          <!--&lt;!&ndash; v-model="offenUsedClassSelected" &ndash;&gt;-->
          <!--<CheckboxGroup>-->
          <!--<p v-for="item in offenUsedClass" :key="item.title">-->
          <!--<Checkbox :label="item.title">{{ item.title }}</Checkbox>-->
          <!--</p>-->
          <!--</CheckboxGroup>-->
          <!--</div>-->
          <!--</TabPane>-->
          <!--</Tabs>-->
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
  import {getDoubanMovie, searchDoubanMovie, searchDoubanMovie2} from '@/api/other'
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
    pub_date: "开播时间",
    state: '状态',
    tags: "标签",
    update_time: "更新时间",
  };

  export default {
    name: 'subject_add',
    data () {
      return {

        offenUsedClass: [],
        classificationList: [],
        articleTagList: [],

        resetPage: false,
        loading: false,

        // 分类列表
        categoryList: [],

        isInit: false,
        // 主题信息

        actress: "",
        area: "",
        category: '',
        cover: "",
        desc: "",
        director: "",
        id: '',
        name: "",
        pub_date: "",
        pub_date_date: '',
        pub_date_time: '',
        state: 0,
        tags: "",
        update_time: "",
        update_time_date: '',
        update_time_time: '',

        tags_list: [], // 标签
        tagsResetSwitch: false,

        // 豆瓣URL
        doubanURL: '',
        doubanName: '',
        doubanSearchData: [],
        showDoubanSearchData: false,


      };
    },
    methods: {

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
          that.pub_date = new datetime(res.data.pub_date);
          that.pub_date_date = that.pub_date.getDate();
          that.pub_date_time = that.pub_date.getTime();
          that.state = res.data.state;
          that.tags_list = res.data.tags.split(',');
          that.tags = res.data.tags;

          that.update_time = new datetime(res.data.update_time);
          that.update_time_date = that.update_time.getDate();
          that.update_time_time = that.update_time.getTime();

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
          pub_date: this.margeDateTime(this.pub_date_date, this.pub_date_time),
          state: this.state,
          tags: this.tags_list.join(','),
          update_time: new Date(),
        };
        this.loading = true;
        saveSubject(data).then(res => {
          console.log('保存主题成功', res);
          this.$Message.success('保存成功');

          let route = {
            name: 'subject_detail',
            params: {
              id: res.data.id
            },
            query: {
              id: res.data.id,
              name: res.data.name
            },
            meta: {
              title: `主题-${res.data.name}`
            }
          };
          this.$router.push(route)

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
      doubanImportData(id){
        let that = this;

        getDoubanMovie(id).then(res => {
          console.log('获取豆瓣信息成功', res);


          // 主演
          that.actress = res.casts.map(i => i.name).join(',');
          // 地区
          that.area = res.countries.join(',');
//        that.category =
          // 封面
          that.cover = res.images["large"];
          // 简介
          that.desc = res.summary;
          // 导演
          that.director = res.directors.map(i => i.name).join(',');
          that.name = res.title;

          let initPubdate = false;
          if (res.pubdates) {
            let reg = res.pubdates[0].match(/(\d{4}-\d{2}-\d{2})/);
            if (reg) {

              that.pub_date = new datetime(reg[1]);
              that.pub_date_date = reg[1];
              that.pub_date_time = '00:00:00';
              initPubdate = true;
            }
          }
          if (!initPubdate) {
            that.pub_date = '';
            that.pub_date_date = '';
            that.pub_date_time = '';
          }


          that.state = 0;
          that.tags = res.tags.join(',');
          that.tags_list = res.tags;

          that.tagsReset();
        }, res => {
          console.log('获取豆瓣信息失败', res);
        }).then(() => {
          console.log('获取豆瓣信息完成');

        })
      },
      doubanImport(){
        let that = this;
        let reg = this.doubanURL.match(/subject\/(\d+)\//);
        if (reg) {
          let id = reg[1];
          that.doubanImportData(id);

        } else {
          this.$Message.error('豆瓣链接有误，');
        }
      },
      doubanSearch(e){
        console.log(e);
        if (this.doubanName.replace(/ /, '').length > 1)
          searchDoubanMovie2(this.doubanName).then(res => {
            console.log('获取豆瓣信息成功', res);
            this.doubanSearchData = JSON.parse(res);
          }, res => {
            console.log('获取豆瓣信息失败', res);

          }).then(() => {
            console.log('获取豆瓣信息完成');
            this.showDoubanSearchData = true;
          });
      },
      doubanSelect(id){
        console.log(id);
        this.doubanImportData(id);
      },
      /* 初始化分类信息 */
      initCategorys(){
        getCategorys().then(res => {
          this.categoryList = res.data.results
        })
      },
    },
    computed: {},
    created(){
      this.initCategorys();
    },
    mounted () {
      /* 载入信息 */


      this.articleTagList = [
        {value: 'vue'},
        {value: 'iview'},
        {value: 'ES6'},
        {value: 'webpack'},
        {value: 'babel'},
        {value: 'eslint'}
      ];
      this.classificationList = [
        {
          title: 'Vue实例',
          expand: true,
          children: [
            {
              title: '数据与方法',
              expand: true
            },
            {
              title: '生命周期',
              expand: true
            }
          ]
        },
        {
          title: 'Class与Style绑定',
          expand: true,
          children: [
            {
              title: '绑定HTML class',
              expand: true,
              children: [
                {
                  title: '对象语法',
                  expand: true
                },
                {
                  title: '数组语法',
                  expand: true
                },
                {
                  title: '用在组件上',
                  expand: true
                }
              ]
            },
            {
              title: '生命周期',
              expand: true
            }
          ]
        },
        {
          title: '模板语法',
          expand: true,
          children: [
            {
              title: '插值',
              expand: true
            },
            {
              title: '指令',
              expand: true
            },
            {
              title: '缩写',
              expand: true
            }
          ]
        }
      ];
      this.offenUsedClass = [
        {
          title: 'vue实例'
        },
        {
          title: '生命周期'
        },
        {
          title: '模板语法'
        },
        {
          title: '插值'
        },
        {
          title: '缩写'
        }
      ];
    },
    destroyed () {
    },
    components: {
      vTags
    },
    watch: {
      '$route' (to, form) {

      },
    },
  };
</script>
<style scoped>
  .doubanImportBtn:focus {
    -webkit-box-shadow: none !important;
    box-shadow: none !important;;
  }

  .external-link:after {
    content: "\F3F2";
    font-family: Ionicons;
    color: #aaa;
    margin-left: 3px;
  }

  .douban-title {
    /*float: left;*/
  }

  .douban-year {
    float: right;
    color: #999;
  }

  .douban-images {
    width: 50px;
  }

  /**/

  #search_suggest {
    /*background: #fff;*/
    /*border: 1px solid #ddd;*/
    /*position: absolute;*/
    /*z-index: 99;*/
    /*top: 32px;*/
    /*width: 302px;*/
    /*border-top: 0 none;*/
  }

  #search_suggest li {
    /*border-bottom: 1px solid #eee;*/
    overflow: hidden;
  }

  #search_suggest li:last-child {
    border-bottom: 0 none;
  }

  #search_suggest li a {
    color: #999;
    display: block;
    overflow: hidden;
    padding: 6px;
    zoom: 1;
  }

  #search_suggest li a:link, #search_suggest li a:visited {
    text-decoration: none;
  }

  #search_suggest li a:hover {
    background: #f9f9f9;
    color: #999;
  }

  #search_suggest li a em {
    font-style: normal;
    color: #369;
  }

  #search_suggest li p {
    margin: 0;
    zoom: 1;
    overflow: hidden;
  }

  #search_suggest li img {
    float: left;
    margin-right: 8px;
    margin-top: 3px;
  }

  #search_suggest {
    /*width: 468px;*/
    /*margin-left: -5px;*/
    /*margin-top: 2px;*/
  }

</style>
<style>
  .ivu-select-item {
    line-height: 30px;
  }

  .douban-search, .douban-search > div {
    width: 100%;
  }
</style>
