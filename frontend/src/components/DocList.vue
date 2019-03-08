<template>
  <div>
    <ul>
      <li class="doc-item" v-for="doc in docList" :key="doc.id">
        <section class="section">
          <router-link :to="{ name: 'doc-detail', params: { id: doc.id } }">
            <h1 class="title">{{ doc.title }}</h1>
          </router-link>
          <doc-tags :doc="doc" />
        </section>
      </li>
    </ul>
  </div>
</template>

<script>
import DocTags from './common/DocTags.vue';

export default {
  computed: {
    docList() {
      return this.$store.state.docs;
    },
  },
  created() {
    this.$store.dispatch('fetchDocs');
  },
  components: {
    DocTags,
  },
};
</script>

<style lang="scss" scoped>
li.doc-item {
  border-top: 1px solid #B5B5B5;
  &:last-child {
    border-bottom: 1px solid #B5B5B5;
  }
}
</style>
