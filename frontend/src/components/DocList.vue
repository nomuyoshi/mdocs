<template>
  <div class="columns">
    <div class="column is-three-quarters">
      <ul>
        <li v-for="doc in docList" :key="doc.id">
          <section class="section">
            <router-link :to="{ name: 'doc-detail', params: { id: doc.id } }">
              <h1 class="title">{{ doc.title }}</h1>
            </router-link>
            <doc-tags :doc="doc" />
          </section>
        </li>
      </ul>
    </div>
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
