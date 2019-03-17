<template>
  <div class="section">
    <h2 class="is-size-5 margin-bottom20">Myドキュメント</h2>
    <doc-list :query="query" />
  </div>
</template>

<script>
import DocList from '@/components/DocList.vue';

const DocListView = {
  computed: {
    query() {
      return {
        title: this.$route.query.title,
        tag: this.$route.query.tag,
      };
    },
  },
  components: {
    DocList,
  },
};

export default DocListView;
</script>
