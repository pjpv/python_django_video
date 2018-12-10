<template>
  <div>
    <Card>

      <div class="toolsbox" style="padding: 10px 0px;">
        <div class="box-left" style="display: inline-table;">
          <Input ref="searchInput" v-model="searchValue" search enter-button="搜索" style="width: auto;padding: 10px 0;"
                 placeholder="Enter something..." @on-search="search">
          <Select placeholder="全部" v-model="searchType" slot="prepend" style="width: 80px">
            <Option v-bind:value="-1">全部</Option>
            <Option v-bind:value="0">分类</Option>
            <Option v-bind:value="1">主题</Option>
          </Select>
          </Input>

        </div>
        <div class="box-right" style="float: right;">
          <Button @click="addCategory">添加分类</Button>
        </div>
      </div>
      <tables ref="tables" editable search-place="top" v-model="tableData" :columns="columns"
              @on-delete="handleDelete"/>
      <div style="margin: 10px;overflow: hidden">
        <div style="float: right;">
          <Page :total="total" :current="currentPage" @on-change="changePage"></Page>
        </div>
      </div>
    </Card>
  </div>
</template>

<script>
  import Tables from '_c/tables'
  import {getSpiders, saveSpider} from '@/api/data'
  export default {
    name: 'spider_list',
    components: {
      Tables
    },
    data () {
      return {
        searchValue: '',
        searchType: '',
        columns: [
          {title: 'ID', key: 'id', sortable: true},
          {title: '名称', key: 'name',},
          {title: '项目名称', key: 'project', sortable: true},
          {title: '排序', key: 'order', sortable: true},
          {
            sortable: true,
            title: '爬虫类型',
            key: 'spider_type',
            render: (h, params) => {
              const row = params.row;
              const color = row.spider_type === 0 ? 'primary' : row.spider_type === 1 ? 'success' : 'error';
              const text = row.spider_type === 0 ? '分类' : row.spider_type === 1 ? '主题' : '未知';

              return h('Tag', {
                props: {
                  type: 'dot',
                  color: color
                }
              }, text);
            }
          },
          {
            title: '是否启用',
            key: 'inHead',
            render: (h, params) => {
//              console.log(params);
              const row = params.row;
//              const color = row.inHead === 1 ? 'primary' : row.status === 2 ? 'success' : 'error';
              const text = row.enable ? '是' : '否';

              return h('i-switch', {
                props: {
                  value: params.row.enable
                },
                on: {
                  'on-change': (value) => {//触发事件是on-change,用双引号括起来，
                    //参数value是回调值，并没有使用到
                    this.switch(params.index) //params.index是拿到table的行序列，可以取到对应的表格值
                  }
                }
              }, text);
            }
          },
          {
            title: 'Handle',
            key: 'handle',
            options: ['view'],
            button: [
              (h, params, vm) => {
                return h('Button', {
                  on: {
                    'click': () => {
//                      vm.$emit('on-delete', params)
                      let row = params.row;
                      let route = {
                        name: row.spider_type == 0 ? 'category_detail' : 'subject_detail',
                        params: {
                          id: row.owner
                        },
                        query: {
                          id: row.owner,
                          name: row.owner
                        },
                        meta: {
                          title: `${row.spider_type == 0 ? '分类' : '主题'}-${row.owner}`
                        }
                      };
                      this.$router.push(route);
                    }
                  }
                }, '查看')
              }
            ]
          }
        ],
        tableData: [],
        total: 0,
        currentPage: 1,
      }
    },
    methods: {
      handleDelete (params) {
        console.log('删除', params)
        console.log('删除', params.row.id, params.row.name)
      },

      switch(index){
        console.log('switch', index);
        console.log('tableData', this.tableData[index].enable);
        this.tableData[index].enable = !this.tableData[index].enable;
        let data = {
          id: this.tableData[index].id,
          enable: this.tableData[index].enable,
        };
        this.save(data, true);
      },
      save(data, portion){
        return new Promise(function (resolve, reject) {
          saveSpider(data, portion).then(res => {
            console.log('修改爬虫信息成功', res);
          }, res => {
            console.log('修改爬虫信息失败', res);
          })
        });
      },
      search(){
        this.loadInfo();
      },
      changePage(){

      },
      loadInfo(){
        let searchType = this.searchType === -1 ? '' : this.searchType;
        getSpiders('', searchType, this.searchValue).then(res => {
          this.tableData = res.data.results;
          this.total = res.data.count;
        })
      },
      addCategory(){
        this.$router.push({
          name: 'category_add'
        })
      }
    },
    created(){
    },
    mounted () {
      this.loadInfo();
    }
  }
</script>

<style>

</style>
