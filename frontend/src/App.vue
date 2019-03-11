<template>
  <div id="app">
    <notifications group="notifications" position="bottom right" />
    <navbar v-if="navbarVisible" />
    <div class="container">
      <div class="columns">
        <div class="column is-3" v-if="sidebarVisible">
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
import Navbar from './components/common/Navbar.vue';
import Sidebar from './components/common/Sidebar.vue';

const App = {
  components: {
    Navbar,
    Sidebar,
  },
  computed: {
    sidebarVisible() {
      return ['doc-new', 'doc-edit', 'not-found'].indexOf(this.$route.name) < 0;
    },
    navbarVisible() {
      return ['not-found'].indexOf(this.$route.name) < 0;
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
