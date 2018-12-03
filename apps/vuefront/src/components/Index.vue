<template>
<div class="index" v-title data-title="首页">
  <card categoryName="yueyu"></card>
  <card categoryName="meiju"></card>
</div>
</template>

<script>

import card from '@/components/card'

export default {
  name: 'HomeIndex',
  data() {
    return {
      msg: 'Welcome to Your HomeIndex',
      activeIndex: '0',
    }
  },
  components: {
    'card': card,
},
  methods: {

  },
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
