<template>
  <div>
    <Card>
      <div class="toolsbox" style="padding: 10px 0px;">
        <div class="box-left" style="display: inline-table;">
          <Input ref="searchInput" v-model="searchValue" search enter-button="搜索" style="width: auto;padding: 10px 0;"
                 placeholder="Enter something..." @on-search="search">
          <Select placeholder="全部" v-model="searchCategory" slot="prepend" style="width: 80px">
            <Option v-bind:value="0">全部</Option>
            <Option v-for="item in categorys" v-model="item.id" :key="item.id">{{ item.name }}</Option>
          </Select>
          </Input>
        </div>
        <div class="box-right" style="float: right;">
          <Button @click="doubanPage">从豆瓣添加主题</Button>
        </div>
      </div>

      <tables ref="tables" editable :searchable="false" search-place="top" v-model="tableData" :columns="columns"
              sortable='custom' @on-sort-change="sortChange"
              @on-delete="handleDelete"/>
      <!--<Button style="margin: 10px 0;" type="primary" @click="exportExcel">导出为Csv文件</Button>-->
      <div style="margin: 10px;overflow: hidden">
        <div style="float: right;">
          <Page :total="total" :current="currentPage" @on-change="changePage"></Page>
        </div>
      </div>
    </Card>
  </div>
</template>

<script>
  import Main from '@/components/main'

  import Tables from '_c/tables'
  //import { getTableData } from '@/api/data'
  import {getCategorys, getSubjects} from '@/api/data'
  export default {
    name: 'subjects',
    components: {
      Tables
    },
    data () {
      return {
        categorys: [],
        searchCategory: '',

        searchValue: '',
        sortkey: '-update_time', // 默认排序
        columns: [
          {title: 'ID', key: 'id', sortable: false, type: 'index', width: 100},
          {title: '名称', key: 'name', editable: false},
          {title: '发布时间', sortable: 'custom', key: 'pub_date', width: 150},
          {title: '更新时间', sortable: 'custom', sortType: 'desc', key: 'update_time', width: 150},
          {title: '分类', key: 'category_name', width: 150},
          {
            title: 'Handle',
            key: 'handle',
//            options: ['delete'],
//            button: [
//              (h, params, vm) => {
//                return h('Poptip', {
//                  props: {
//                    confirm: false,
//                    title: '你确定要删除吗?'
//                  },
//                  on: {
//                    'on-ok': () => {
//                      console.log(params)
////                      vm.$emit('on-delete', params)
//                      vm.$emit('input', params.tableData.filter((item, index) => index !== params.row.initRowIndex))
//                    }
//                  }
//                }, [
//                  h('Button', '自定义删除'),
//                  h('Button', '自定义删除'),
//                ])
//              }
//            ]
            button: [(h, params) => {
              return h('div', [
                h('Button', {
                  props: {
                    type: 'primary',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      let route = {
                        name: 'subject_detail',
                        params: {
                          id: params.row.id
                        },
                        query: {
                          id: params.row.id,
                          name: params.row.name

                        },
                        meta: {
                          title: `主题-${params.row.name}`
                        }
                      };

                      this.$router.push(route)
                    }
                  }
                }, '打开'),
              ]);
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
        console.log(params)
      },
      exportExcel () {
        this.$refs.tables.exportCsv({
          filename: `table-${(new Date()).valueOf()}.csv`
        })
      },
      getList(page){
        let that = this;
        that.currentPage = page;

        let category = that.searchCategory === 0 ? '' : that.searchCategory;
//        this.$refs.tables.searchKey
        getSubjects(that.searchValue, that.sortkey, category, page).then(res => {

          that.tableData = res.data.results;
          that.total = res.data.count;
        })
      },
      /* 修改分页 */
      changePage (page) {
        // The simulated data is changed directly here, and the actual usage scenario should fetch the data from the server

        this.getList(page);
      },
      /* 搜索 */
      search(){

        this.getList(1);
      },
      /* 排序 */
      sortChange(e){
        console.log(e.column, e.key, e.order);
        if (e.order === "normal") {
          this.sortkey = '';
        } else {
          let type = e.order === "asc" ? '' : '-';

          this.sortkey = type + e.key;
        }
        this.getList(1);
      },
      /* 初始化分类信息 */
      initCategorys(){
        getCategorys().then(res => {
          this.categorys = res.data.results
        })
      },
      doubanPage(){

      }
    },
    created(){
      this.initCategorys();
      this.getList(1);
    },
    mounted () {
//      this.getList(1)
    }
  }
</script>

<style>

</style>
