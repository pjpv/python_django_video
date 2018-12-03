<template>
<div class="category" v-title v-bind:data-title='thistitle'>
 Category {{ thistitle }}
</div>
</template>

<script>
export default {
  name: 'Category',
  data() {
    return {

    }
  },
  methods: {

  },
  computed: {
      thistitle: function(){
          document.title = this.$route.params.name
          return this.$route.params.name
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
