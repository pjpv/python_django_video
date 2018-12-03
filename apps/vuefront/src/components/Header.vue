<template>
<div class="nav">
  <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
    <el-menu-item v-for="(item, index) in category" :index="index" :key="index">
      {{ item.name }}
    </el-menu-item>
    <!-- <el-menu-item index="/">首页</el-menu-item>
    <el-menu-item index="yueyu">粤语剧集</el-menu-item>
    <el-menu-item index="meiju">美国剧集</el-menu-item> -->
    <!-- <el-submenu index="2">
      <template slot="title">我的工作台</template>
      <el-menu-item index="2-1">选项1</el-menu-item>
      <el-menu-item index="2-2">选项2</el-menu-item>
      <el-menu-item index="2-3">选项3</el-menu-item>
      <el-submenu index="2-4">
        <template slot="title">选项4</template>
        <el-menu-item index="2-4-1">选项1</el-menu-item>
        <el-menu-item index="2-4-2">选项2</el-menu-item>
        <el-menu-item index="2-4-3">选项3</el-menu-item>
      </el-submenu>
    </el-submenu> -->
    <!-- <el-menu-item index="3" disabled>消息中心</el-menu-item> -->
  </el-menu>
  <div class="line"></div>
</div>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      activeIndex: '/',
      category: [{
          index: '/',
          name: '首页'
        },
        {
          index: 'yueyu',
          name: '粤语剧集'
        },
        {
          index: 'meiju',
          name: '美国剧集'
        },
      ]
    }
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
      // 首页
      if (key === 0) {
        this.$router.push('/')
        return
      }

      // 分类
      this.$router.push({
        name: 'category',
        params: {
          id: this.category[key].index,
          name: this.category[key].name,
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
