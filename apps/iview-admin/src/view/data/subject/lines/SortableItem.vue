<template>
  <li class="list-item">
    <!--<Row>-->
    <!--<Col span="1">-->
    <!--<span v-handle class="handle" v-if="showHandle"><Icon type="md-move" /></span>-->
    <!--</Col>-->
    <!--<Col span="23">-->
    <slot/>
    <!--</Col>-->
    <!--</Row>-->
  </li>
</template>

<script>

  import {ElementMixin, HandleDirective} from 'vue-slicksort';

  export default {
    mixins: [ElementMixin],
    props: ['item', 'showHandle'],
    directives: {handle: HandleDirective},
  };
</script>
<style>
  .handle {
    /*display: block;*/
    /*width: 0px;*/
    /*height: 0px;*/
    /*padding: 10px;*/
    /*background-image: url('data:image/svg+xml; charset=utf-8,<svg xmlns= "http://www.w3.org/2000/svg" width= "50" height= "50" viewBox= "0 0 50 50" ><path d= "M0 7.5v5h50v-5H0zm0 15v5h50v-5H0zm0 15v5h50v-5H0z" color= "%23000" /></svg> ');*/
    /*background-size: contain;*/
    /*background-repeat: no-repeat;*/
    /*opacity: .25;*/
    /*margin-right: 20px;*/
    cursor: row-resize;
    /*position: absolute;*/
    /*left: 100px;*/
    /*z-index: 1;*/
    /*margin: 5px;*/
    font-size: 20px;
    float: right;
  }

  li {
    list-style-type: none;
  }
</style>
