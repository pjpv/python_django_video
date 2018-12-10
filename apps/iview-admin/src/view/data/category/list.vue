<template>
  <div>
    <Card>

      <div class="toolsbox" style="padding: 10px 0px;">
        <div class="box-left" style="display: inline-table;">
          <Input ref="searchInput" v-model="searchValue" search enter-button="搜索" style="width: auto;padding: 10px 0;"
                 placeholder="Enter something..." @on-search="search">
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
  import {getCategorys, saveCategory} from '@/api/data'
  export default {
    name: 'category_list',
    components: {
      Tables
    },
    data () {
      return {
        searchValue: '',
        columns: [
          {title: 'ID', key: 'id', sortable: true},
          {title: '名称', key: 'name', editable: true},
          {title: '排序', key: 'order'},

          {
            title: '在顶部显示',
            key: 'inHead',
            render: (h, params) => {
//              console.log(params);
              const row = params.row;
//              const color = row.inHead === 1 ? 'primary' : row.status === 2 ? 'success' : 'error';
              const text = row.inHead ? '是' : '否';

              return h('i-switch', {
                props: {
                  value: params.row.inHead
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
                        name: 'category_detail',
                        params: {
                          id: row.id
                        },
                        query: {
                          id: row.id,
                          name: row.name
                        },
                        meta: {
                          title: `主题-${params.row.name}`
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
        console.log('tableData', this.tableData[index].inHead);
        this.tableData[index].inHead = !this.tableData[index].inHead;
        let data = {
          id: this.tableData[index].id,
          inHead: this.tableData[index].inHead,
        };
        this.save(data, true);
      },
      save(data, portion){
        return new Promise(function (resolve, reject) {
          saveCategory(data, portion).then(res => {
            console.log()
          }).then(res => {
            console.log('修改分类信息成功', res);
          }, res => {
            console.log('修改分类信息失败', res);
          })
        });
      },
      search(){
        this.loadInfo();
      },
      changePage(){

      },
      loadInfo(){
        getCategorys(this.searchValue, this.currentPage).then(res => {
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
