<template>
  <div>

    <Card style="width:100%">
      <div slot="title">
        <p style="display: initial;">
          <Icon type="ios-list-box-outline"/>
          播放列表
        </p>
        <div class="sortBox" style="float:right;line-height:30px;">
          <!--<Button icon="ios-add-circle-outline" v-if="!srotSwitch" @click="addVideo">添加视频</Button>-->
          <Button size="small" icon="ios-add-circle-outline" v-if="!srotSwitch" @click="addVideoList">添加列表</Button>
          <Button size="small" type="primary" icon="ios-cloud-upload-outline" v-if="srotSwitch" @click="saveSort">保存</Button>
          排序：
          <i-switch v-model="srotSwitch" @on-change="trigger"/>
        </div>
      </div>

      <Spin size="large" v-if="loading"></Spin>

      <!--<draggable class="drop-box1" :options="options" :value="lines">-->
      <!--<div class="drag-list-item" v-for="(line, index) in lines" :key="`drag_li1_${index}`">-->
      <!--<slot name="left" :line="line">-->
      <!--<lineList style="padding-top: 30px;" :line="line"></lineList>-->
      <!--</slot>-->
      <!--</div>-->
      <!--</draggable>-->
      <!--<SortableList lockAxis="y" v-model="lines">-->
      <!--<SortableItem v-for="(line, index) in lines" :index="index" :key="index" :item="line"/>-->
      <!--</SortableList>-->

      <SortableList lockAxis="y"
                    v-model="lines"
                    :useDragHandle="true"
                    :transitionDuration="300"
                    style="padding-top: 30px"
                    @sort-end="sortEnd"
                    @input="saveLines"
                    v-if="hackReset"
      >
        <SortableItem v-for="(line, index) in lines" :index="index" collection="lines" :showHandle="srotSwitch"
                      :key="index">
          <!--<span v-handle class="handle" style="padding: 50px;width: 50px;height: 50px;"></span>-->
          <lineList style="" :srotSwitch="srotSwitch" :line="line" v-on:lineSort="lineSort"
                    @videoEdit="videoEdit" @videoDel="videoDel"
                    @lineRename="lineRename" @lineDel="lineDel" @addVideo="addVideo"
          ></lineList>
        </SortableItem>
      </SortableList>
    </Card>

    <Modal
      v-model="showVideoEditModel"
      :title="modelTitle"
      @on-ok="videoSave"
      @on-cancel="videoSaveCancel">
      <Form :model="formData" :label-width="80">
        <FormItem label="名称">
          <Input v-model="formData.name" placeholder="显示名称"></Input>
        </FormItem>
        <FormItem label="链接">
          <Input v-model="formData.link" placeholder="链接"></Input>
        </FormItem>
        <FormItem label="播放器">
          <Select v-model="formData.player">
            <Option v-bind:value="0">DPlayer</Option>
            <Option v-bind:value="1">ckPlayer</Option>
            <Option v-bind:value="2">iframe</Option>
            <Option v-bind:value="3">站外链接</Option>
          </Select>
        </FormItem>
        <FormItem label="添加时间">
          <Row>
            <Col span="11">
            <DatePicker type="date" placeholder="日期" v-model="formData.date"></DatePicker>
            </Col>
            <Col span="2" style="text-align: center">
            -</Col>
            <Col span="11">
            <TimePicker type="time" format="HH:mm" placeholder="时间" v-model="formData.time"></TimePicker>
            </Col>
          </Row>
        </FormItem>
        <FormItem label="是否直播">
          <i-switch v-model="formData.live" size="large">
            <span slot="open">是</span>
            <span slot="close">否</span>
          </i-switch>
        </FormItem>
        <FormItem label="所属列表">
          <Select v-model="formData.line">
            <Option v-for="l in lines" v-bind:value="l.id">{{l.name}}</Option>
          </Select>
        </FormItem>
      </Form>
    </Modal>
  </div>
</template>

<script>
  import draggable from 'vuedraggable'
  import {ContainerMixin, ElementMixin} from 'vue-slicksort';
  //  import {SlickList, SlickItem} from 'vue-slicksort';
  import SortableItem from './SortableItem.vue'
  import SortableList from './SortableList.vue'


  import lineList from './line'
  import {getlines, setlinesSort, setVideoSort, getVideo, saveVideo, delVideo, saveLine, delLine} from '@/api/data'

  export default {
    name: 'lines',
    props: ['subjectId'],
    data() {
      return {
        srotSwitch: false,
        lines: [
//            {
//          name: 'line - 1',
//          list: ['1 1', '1 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7', 'Item 8', 'Item 9', 'Item 10', 'Item 11', 'Item 12', 'Item 13', 'Item 14', 'Item 15']
//        }, {
//          name: 'line - 2',
//          list: ['Item 122222222', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7', 'Item 8', 'Item 9', 'Item 10', 'Item 11', 'Item 12']
//        },
        ],
        changeListIndex: false,
        newLines: [],
        changeItemIndex: false,
        newItemList: {},

        loading: true,

        hackReset: true, // 用于强制刷新组件

        // 视频编辑属性
        showVideoEditModel: false,
        formData: {
          id: '', // id
          line: '', // 所属列表
          name: '', // 名称
          link: '', // 链接
          player: '', // 播放器
          live: '', // 是否直播
          date: '', // 添加时间
          time: '', // 添加时间
        },

        // 对话框类型 0 新建, 1 编辑
        modelType: 0,


        // 添加播放列表
        addlineName: '',
      };
    },
    computed: {
      modelTitle(){
        return (this.modelType ? '编辑' : '添加') + '视频';
      },
    },
    methods: {
      clickBtn(e){
        console.log(e)
      },
      sort(e){
        console.log(e)
        console.log(e.items.map(i => i.item))

      },
      trigger(e){
        this.draggable = this.srotSwitch;
        this.sortable = this.srotSwitch;
      },
      initData(){
        let that = this;
        that.loading = false;
        return new Promise(function (resolve, reject) {
          getlines(that.subjectId).then(res => {
            that.lines = res.data.results;
            console.log('载入播放线路成功');
            that.loading = false;
            resolve()
          }, res => {
            console.log('载入播放线路失败');
          })
//          .then(() => {
//          console.log('载入播放线路完成');
//        })
        });
      },
      resetLines(){
        this.hackReset = false;
        this.$nextTick(() => {
          this.hackReset = true;
          this.loading = false;
        });
      },
      sortEnd(e){
        console.log(e.event, e.newIndex, e.oldIndex, e.collection);
        if (e.newIndex != e.oldIndex)
          this.changeListIndex = true;
      },
      saveLines(newLlines){
        this.newLines = newLlines;
      },
      lineSort(line, list){
        console.log('lines lineSort', line, list);
        this.newItemList[line.id] = list.items.map(i => i.item);
        this.changeItemIndex = true;
      },
      saveLinesSort(){
        let that = this;
        return new Promise(function (resolve, reject) {
          if (that.changeListIndex) {
            console.log('修改了列表排序, 新顺序：', that.newLines.map(l => l.id))
            let data = {
              sid: that.subjectId,
              indexs: that.newLines.map(l => l.id),
            };
            setlinesSort(data).then(res => {
              console.log('修改了列表排序成功');
              that.newLines = [];
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
      saveVideoSort(){

        let that = this;
        return new Promise(function (resolve, reject) {

          if (that.changeItemIndex) {
            console.log('修改了分集排序', that.newItemList);
//            let data = [];
//            let keys = Object.keys(that.newItemList);
//            for (let i = 0; i < keys.length; i++) {
//              console.log('line_id', keys[i], 'itemIndexs', that.newItemList[keys[i]].map(i => i.id));
//              data.push({
//                lineId: keys[i],
//                indexs: that.newItemList[keys[i]].map(i => i.id),
//              });
//            }
            let data = Object.keys(that.newItemList).map(key => {
              return {
                lineId: key,
                indexs: that.newItemList[key].map(i => i.id)
              }
            });

            setVideoSort(data).then(res => {
              console.log('修改了视频排序成功');
              that.newItemList = {};
              that.changeItemIndex = false;
              resolve();
            }, res => {
              console.log('修改了视频排序失败');
              reject();
            })
          } else {
            resolve();
          }
        });
      },
      saveSort(){
        let that = this;
        that.saveLinesSort()
          .then(that.saveVideoSort)
          .then(() => {
            that.$Message.success('排序成功');
            that.srotSwitch = false;
          }).catch(() => {
          that.$Message.error('排序失败');

        })


      },
      videoEdit(video){
        let that = this;
        console.log('编辑视频', video);
        getVideo(video).then(res => {
          let data = res.data;
          console.log('获取到视频', res.data);
          let add_time = new Date(data.add_time);
          that.formData = {
            id: data.id, // 所属列表
            line: data.line, // 所属列表
            name: data.name, // 名称
            link: data.link, // 链接
            player: data.player, // 播放器
            live: data.live, // 是否直播
            date: `${add_time.getFullYear()}-${add_time.getMonth() + 1}-${add_time.getDate()}`, // 添加时间
            time: `${add_time.getHours()}:${add_time.getMinutes()}:${add_time.getSeconds()}}`, // 添加时间
          };
          that.modelType = 1;
          that.showVideoEditModel = true;
        }, res => {
          console.log('获取视频信息失败', res.data);
        }).then(() => {
          console.log('获取视频信息完成');
        });
      },
      videoDel(video){
        let that = this;
        console.log('删除视频', video);
        delVideo(video.id).then(res => {
          console.log('删除视频成功', res.data);
          that.$Message.success('删除成功');
          // 将元素删除
          video.dom.remove();

        }, res => {
          console.log('删除视频失败', res.data);
        }).then(() => {
          console.log('删除视频完成');
        });
      },
      videoSave(){
        let that = this;
        let data = this.formData;

        let date = new Date(this.formData.date);
        data.add_time = `${date.getFullYear()}-${date.getMonth()}-${date.getDate()} ${this.formData.time}:00`;
        saveVideo(data).then(res => {
          console.log('保存视频信息成功', res.data);

          that.$Message.success('保存成功');
//          let newLines = this.lines;
//          for (let i = 0; i < newLines.length; i++) {
//            if (newLines[i].id === res.data.line) {
//              let list = newLines[i].list;
//              for (let j = 0; j < list.length; j++) {
//                if (list[j].id === res.data.id) {
//                  newLines[i].list[j] = res.data;
//                  that.lines = newLines;
//                  break;
//                }
//              }
//            }
//          }
          // 重新获取数据，并强制刷新组件
          that.initData().then(that.resetLines);


        }, res => {
          console.log('保存视频信息失败', res.data);
        }).then(() => {
          console.log('保存视频信息完成');
        });
      },
      videoSaveCancel(){
        console.log('videoSaveCancel');

      },
      /**
       * 添加视频
       */
      addVideo(line){

        this.formData = {
//            id: data.id, // 没有ID
          line: line.id, // 所属列表
          name: '', // 名称
          link: '', // 链接
          player: 0, // 播放器
          live: false, // 是否直播
        };
        this.modelType = 0;
        this.showVideoEditModel = true;
      },
      /**
       * 添加视频列表
       */
      addVideoList(){
        this.$Modal.confirm({
          render: (h) => {
            return h('Input', {
              props: {
                value: this.addlineName,
                autofocus: true,
                placeholder: '输入列表名称'
              },
              on: {
                input: (val) => {
                  this.addlineName = val;
                }
              }
            })
          },
          loading: true,
          title: '播放列表添加',
          onOk: () => {
            let val = this.addlineName;
            console.log('添加播放列表', val);

            saveLine({name: val, subject: this.subjectId}).then(res => {
              console.log('保存播放列表题成功', res);
              this.$Message.success('保存成功');

              // 重新获取数据，并强制刷新组件
              this.initData().then(this.resetLines);
            }, res => {
              console.log('保存播放列表失败', res);
              this.$Message.error('保存失败');
            }).then(() => {
              this.$Modal.remove();
            });


            this.addlineName = '';
          }
        })

      },
      /**
       * 播放列表重命名
       */
      lineRename(line){
        this.addlineName = line.name;
        this.$Modal.confirm({
          render: (h) => {
            return h('Input', {
              props: {
                value: this.addlineName,
                autofocus: true,
                placeholder: '输入列表名称'
              },
              on: {
                input: (val) => {
                  this.addlineName = val;
                }
              }
            })
          },
          loading: true,
          title: '播放列表重命名',
          onOk: () => {
            let val = this.addlineName;
            console.log('重命名播放列表', val);

            saveLine({id: line.id, name: val, subject: this.subjectId}).then(res => {
              console.log('保存播放列表题成功', res);
              this.$Message.success('保存成功');
              // 重新获取数据，并强制刷新组件
              this.initData().then(this.resetLines);
            }, res => {
              console.log('保存播放列表失败', res);
              this.$Message.error('保存失败');
            }).then(() => {
              this.$Modal.remove();
            });
            this.addlineName = '';
          }
        })
      },
      /**
       * 播放列表删除
       */
      lineDel(lineObj){
        let line = lineObj.line,
          dom = lineObj.dom,
          that = this;
        console.log('lineDel', line);
        that.$Modal.confirm({
          title: '删除播放列表',
          content: `确认删除 ${line.name} 吗？<br>该列表下的所有视频也将被删除！<br>此操作不可恢复！！！`,
          loading: true,
          onOk: () => {
            delLine(line.id).then(res => {
              console.log('删除播放列表成功', res);
              that.$Message.success('删除成功');
              // 重新获取数据，并强制刷新组件
//              that.initData().then(that.resetLines);
              // 删除元素
              dom.remove();
            }, res => {
              console.log('删除播放列表失败', res);
              that.$Message.error('删除失败');
            }).then(() => {
              that.$Modal.remove();
            });

          }
        })
      },
    },
    components: {
      lineList,

      draggable,
      SortableList,
      SortableItem,
//      SlickList,
//      SlickItem,

    }
    ,
    mounted()
    {
      console.log('lines created', this.subjectId);
      this.initData();
    }
  }
  ;

</script>
