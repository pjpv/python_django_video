<template>
  <div class="video-item" ref="thisItem">
    <!--<Button >{{props.item}}</Button>-->
    <Card style="margin: 5px;">
      <div class="video-title" style="text-align:center;display: inline-flex;">
        {{item.name}}
      </div>
      <ButtonGroup style="float: right;" v-show="btnDisabled" :disabled="!btnDisabled">

        <Button :size="buttonSize" ghost type="primary" icon="ios-create" @click="editBtn"></Button>
        <Poptip confirm title="确定删除该视频?" @on-ok="delBtn">
          <Button :size="buttonSize" ghost type="error" icon="ios-trash"></Button>
        </Poptip>
      </ButtonGroup>

    </Card>
  </div>
</template>

<script>
  export default {
    name: 'lineItem',
    props: ['item', 'btnDisabled'],
    data() {
      return {
        buttonSize: 'small',
      }
    },
    methods: {

      editBtn(){
        this.$emit('videoEdit', this.item.id);
      },
      delBtn(){
        this.$emit('videoDel', {id: this.item.id, dom: this.$refs.thisItem.parentNode});
      }
    },
    mounted(){
    },
    watch: {
//      'line' () {
//        console.log('item.item watch init');
//        this.itemData = this.item;
//      },
    },
  };

</script>
<style>
  .video-title {
    text-align: center;
    display: inline-flex;
    width: 70px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .video-item .ivu-card-body {
    padding: 10px 3px;
  }
</style>
