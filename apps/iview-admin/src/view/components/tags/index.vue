<template>

  <div class="input tags-wrap">
    <div class="tags" transition="tags" :style="{backgroundColor: bgc[item.bgc_no]}" v-for="(item,index) in dis_source">
      <span class="content">{{item.text}}</span><span class="del" @click="del(index, false)">&times;</span>
    </div>
    <input class="tags-input" type="text" placeholder="添加标签（,分割)" v-model="text" @keyup.enter="add(text)"
           @keydown.delete="del(source.length - 1, true)">
  </div>
</template>
<script>


  export default {
    name: 'tags',
    props: {
      source: {
        type: Array,
        default: []
      }
    },
    data() {
      var dis_source = [];
      this.source.forEach(function (item) {
        var obj = {
          text: item,
          bgc_no: Math.ceil(Math.random() * 10) - 1
        }
        dis_source.push(obj)
      });
      return {
        text: '',
        bgc: ['#e961b4', '#ed664b', '#7b6ac7', '#56abd1', '#f7af4c', '#fe5467', '#52c7bd', '#a479b7', '#cb81ce', '#5eabc5'],
        dis_source: dis_source
      }
    },
    methods: {
      add(text){
        if (text != '') {
          let arr = text.split(',');
          for (let text of arr) {
            var count = this.source.length
            this.$set(this.source, count, text)
            this.$set(this.dis_source, count, {
              text: text,
              bgc_no: Math.ceil(Math.random() * 10) - 1
            })
          }
          this.text = ''
        }
      },
      del(index, way){
        if (way) {
          if (index >= 0 && this.text == '') {
            this.source.splice(index, 1)
            this.dis_source.splice(index, 1)
          }
        } else {
          this.source.splice(index, 1)
          this.dis_source.splice(index, 1)
        }
      }
    }

  }

</script>

<style type="scss" scoped>
  //输入框tags
  .tags-wrap {
    width: 100%;
    height: 100%;
    outline: none;
    display: inline-table;

    &::after {
      content: "";
      display: block;
      height: 0;
      clear: both;
    }

  }

  .tags, .tags-input {
    position: relative;
    float: left;
    color: #fff;
    line-height: 28px;
    margin: 0 4px 4px 0;
    padding: 0 22px 0 10px;
    border-radius: 6px;

    .content {
      line-height: 28px;
    }

    .del {
      width: 22px;
      height: 28px;
      text-align: center;
      cursor: pointer;
      position: absolute;
      top: -1px;
      right: 0;
    }

  }

  .tags-input {
    font-size: 14px;
    padding: 0;
    background-color: inherit;
    border: none;
    color: inherit;
    width: 10em;
    border-bottom: 1px dashed;
    border-radius: 0;
  }

  .tags .del, .tags-input .del {
    width: 22px;
    height: 28px;
    text-align: center;
    cursor: pointer;
    position: absolute;
    top: -1px;
    right: 0;
  }

  .tags-input:focus {
    outline: none;
  }

  .tags-wrap {
    display: inline-table;
  }
</style>
