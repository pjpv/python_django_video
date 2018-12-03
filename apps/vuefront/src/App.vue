<template>
<div id="app">
  <el-container>
    <el-header>
      <Header></Header>
    </el-header>
    <el-main>
      <!--<img src="./assets/logo.png">-->
      <router-view />
    </el-main>
  </el-container>
</div>
</template>

<script>
import Header from './components/Header'

export default {
  name: 'App',
  components: {
    Header: Header,
    Card: Card,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /*margin-top: 60px;*/
}
</style>
