<template>
  <div id="app">
    <notifications group="notifications" position="bottom right" />
    <navbar v-if="navbarVisible" brand-width="230" />
    <div class="columns">
      <div class="column is-narrow sidebar-column" v-if="sidebarVisible">
        <sidebar side-width="230" />
      </div>
      <div class="column">
        <router-view/>
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
  computed: {
    sidebarVisible() {
      return ['doc-new', 'doc-edit', 'not-found', 'contact'].indexOf(this.$route.name) < 0;
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
  .sidebar-column {
    position: sticky;
    top: calc(3.25rem - 0.75rem);
    padding-bottom: 0;
    height: calc(100vh - 3.25rem + 0.75rem);
  }
}
</style>
