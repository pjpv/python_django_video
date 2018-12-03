<template>
<el-card class="box-card">
  <div slot="header" class="clearfix">
    <span style="float: left; padding: 3px 0" type="text">{{ item.name }} {{ categoryName }}</span>
    <el-button style="float: right; padding: 3px 0" type="text">更多</el-button>
  </div>
  <el-row :gutter="10">
    <el-col :xs="100" :sm="6" :md="6" :lg="4" :xl="3" v-for="(i, index) in 6" :key="i">
      <el-card :body-style="{ padding: '0px' }" shadow="never">
        <img src="http://i1.fuimg.com/604243/077c3c823968aac9t.jpg" class="image">
        <div style="padding: 14px;">
          <span><router-link :to="{ name: 'Subject', params: {id:1} }">好吃的汉堡</router-link></span>
          <div class="bottom clearfix">
            <time class="time">time</time>
            <el-button type="text" class="button">操作按钮</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>
</el-card>
</template>
<script>
export default {
  name: 'card',
  data() {
    return {
      item: {
        name: '标题',
        id: '123',
        cover: '/img.jpg'
      },
    }
  },
  methods: {

  },
  props: ['categoryName']
}
</script>
<style>
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both
}

.box-card {
  width: 100%;
  margin: 10px 0
}

.el-col {
  padding: 10px;
}

.el-card {
  border: none;
}
</style>
