<template>
  <nav id="sidebar" class="has-background-grey-dark" :style="{ width: sideWidth + 'px'}">
    <div class="new-doc-button has-text-centered">
      <router-link to="/docs/new" class="button is-primary is-rounded">
        <b-icon icon="plus"></b-icon><span>ドキュメント作成</span>
      </router-link>
    </div>
    <tag-list/>
  </nav>
</template>

<script>
import TagList from './TagList.vue';

const Sidebar = {
  props: {
    sideWidth: {
      type: String,
      required: true,
    },
  },
  components: {
    TagList,
  },
};

export default Sidebar;
</script>

<style lang="scss" scoped>
#sidebar {
  height: 100%;
  padding: 2rem 1rem 0 1rem;
  margin: 0;

  .new-doc-button {
    margin-bottom: 2rem;
  }
}
</style>
