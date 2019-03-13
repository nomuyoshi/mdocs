<template>
  <div id="sidebar">
    <router-link to="/docs/new" class="button is-link is-medium">
      <b-icon icon="edit"></b-icon><span>新規作成</span>
    </router-link>
    <tag-list/>
  </div>
</template>

<script>
import TagList from './TagList.vue';

const Sidebar = {
  components: {
    TagList,
  },
};

export default Sidebar;
</script>
