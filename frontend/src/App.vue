<template>
  <div id="app">
    <notifications group="notifications" position="bottom right" />
    <navbar/>
    <div class="container">
      <div class="columns">
        <div class="column is-3" v-show="sidebarVisible()">
          <sidebar/>
        </div>
        <div class="column">
          <router-view/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import Sidebar from './components/Sidebar.vue';

const App = {
  components: {
    Navbar,
    Sidebar,
  },
  methods: {
    sidebarVisible() {
      const newUrlRegex = /\/docs\/new(\/)?$/;
      const editUrlRegex = /\/docs\/\d+\/edit(\/)?$/;
      // 新規作成と編集ページではサイドバー非表示
      if (newUrlRegex.test(this.$route.path) || editUrlRegex.test(this.$route.path)) {
        return false;
      }
      return true;
    },
  },
};

export default App;
</script>

<style lang="scss">
@import './assets/application.scss';
</style>

<style lang="scss" scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.container {
  margin-top: 30px;
}
</style>
