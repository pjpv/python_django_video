<template>
  <div ref="thisline">
    <Card dis-hover style="margin: 5px;    background: #f8f8f9;">
      <div ref="linediv" style="">
        <span v-handle class="handle" v-if="srotSwitch"><Icon type="md-move"/></span>
        <div class="handle">
          <ButtonGroup shape="circle">
            <Button icon="ios-add-circle-outline" v-if="!srotSwitch" @click="addVideo" title="添加视频"></Button>
            <Button icon="ios-create-outline" v-if="!srotSwitch" @click="lineRename" title="重命名"></Button>
            <Button icon="ios-trash-outline" v-if="!srotSwitch" @click="lineDel" title="删除列表"></Button>
          </ButtonGroup>
        </div>
        <h2>{{line.name}}</h2>
        <Divider style="margin: 3px 0;"/>
        <grid ref="linegrid"
              :draggable="srotSwitch"
              :sortable="srotSwitch"
              :items="line.list"
              :height="100"
              :cellWidth="150"
              :windowWidth="maxWidth"
              @sort="sort"
        >
          <template slot="cell" scope="props">
            <lintItem style="width: 100%;" :btnDisabled="!srotSwitch"
                      @videoEdit="videoEdit" @videoDel="videoDel"
                      :item="props.item">
            </lintItem>
          </template>

        </grid>
      </div>
    </Card>
  </div>
</template>

<script>

  import {HandleDirective} from 'vue-slicksort';

  import lintItem from './item.vue'

  export default {
    name: 'lineList',
    props: ['line', 'srotSwitch'],
    directives: {handle: HandleDirective},
    data() {
      return {
        maxWidth: 100,
        isInit: false,
      };
    },
    methods: {
      /* 排序结果 */
      sort(list){
        // 传递给负组件
        this.$emit('lineSort', this.line, list);
      },
      /* 初始化宽度 */
      InitWidth(){
        if (this.$refs.linediv) {
          this.maxWidth = this.$refs.linediv.offsetWidth;
          this.isInit = true;
        }
      },
      videoEdit(videoId){
        this.$emit('videoEdit', videoId);
      },
      videoDel(videoId){
        this.$emit('videoDel', videoId);
      },
      lineRename(){
        this.$emit('lineRename', this.line);
      },
      lineDel(){
        this.$emit('lineDel', {line: this.line, dom: this.$refs.thisline.parentNode});
      },
      addVideo(){
        this.$emit('addVideo', this.line);
      }
    },
    updated(){
      console.log('updated');
      this.InitWidth();
    },
    mounted(){
      console.log('mounted');
      let that = this;
      this.$nextTick(function () {

        that.InitWidth();
      });
    },
    computed: {
      offsetWidth(){
        return this.$refs.linediv.offsetWidth;
      }
    },
    components: {
      lintItem
    },
    watch: {
//      'line' () {
//        console.log('line.line watch init');
//        this.lineData = this.line;
//      },
    },
  };

</script>
<style>
  .v-grid-item-wrapper.v-grid-item-animate {
    transition: transform 200ms ease;
  }
</style>
