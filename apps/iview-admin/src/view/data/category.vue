<template>
  <div>
    <Card>
      <tables ref="tables" editable searchable search-place="top" v-model="tableData" :columns="columns"
              @on-delete="handleDelete"/>
      <Button style="margin: 10px 0;" type="primary" @click="exportExcel">导出为Csv文件</Button>
    </Card>
  </div>
</template>

<script>
  import Tables from '_c/tables'
  //import { getTableData } from '@/api/data'
  import {getCategorys} from '@/api/data'
  export default {
    name: 'categorys',
    components: {
      Tables
    },
    data () {
      return {
        columns: [
          {title: 'ID', key: 'id', sortable: true},
          {title: '名称', key: 'name', editable: true},
          {title: '排序', key: 'order'},
          {
            title: 'Handle',
            key: 'handle',
            options: ['delete'],
            button: [
              (h, params, vm) => {
                return h('Poptip', {
                  props: {
                    confirm: true,
                    title: '你确定要删除吗?'
                  },
                  on: {
                    'on-ok': () => {
                      console.log(params)
                      vm.$emit('on-delete', params)
                      vm.$emit('input', params.tableData.filter((item, index) => index !== params.row.initRowIndex))
                    }
                  }
                }, [
                  h('Button', '自定义删除')
                ])
              }
            ]
          }
        ],
        tableData: []
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
      }
    },
    created(){
      getCategorys().then(res => {
        this.tableData = res.data.results
      })
    },
    mounted () {
//    getTableData().then(res => {
//      this.tableData = res.data
//    })
//    getCategorys().then(res => {
//      this.tableData = res.data.results
//    })
    }
  }
</script>

<style>

</style>
