<template slot-scope="props">
    <div class="subject">

           <img src="http://i1.fuimg.com/604243/077c3c823968aac9t.jpg" class="image">
           <el-form label-position="left" inline class="demo-table-expand">
             <el-form-item label="商品名称">
               <span>名称</span>
             </el-form-item>
             <el-form-item label="所属店铺">
               <span>所属店铺</span>
             </el-form-item>
             <el-form-item label="商品 ID">
               <span>商品 ID</span>
             </el-form-item>
             <el-form-item label="店铺 ID">
               <span>店铺 ID</span>
             </el-form-item>
             <el-form-item label="商品分类">
               <span>商品分类</span>
             </el-form-item>
             <el-form-item label="店铺地址">
               <span>店铺地址</span>
             </el-form-item>
             <el-form-item label="商品描述">
               <span>商品描述</span>
             </el-form-item>
           </el-form>

           </div>
 </template>


 <script>
 export default {
   name: 'Subject',
   data() {
     return {

     }
   },
   methods: {

   },
   computed: {
       thistitle: function(){

       }
   }
 }
 </script>

 <!-- Add "scoped" attribute to limit CSS to this component only -->
 <style scoped>
 label {
    width: 90px;
    color: #99a9bf;
  }
 .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
 </style>
