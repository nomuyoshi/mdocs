<template>
  <div>
    <h2 class="is-size-2 margin-bottom20">Myドキュメント</h2>
    <doc-list :fetch="fetch" :title-query="titleQuery" />
  </div>
</template>

<script>
import DocList from '@/components/DocList.vue';

const DocListView = {
  props: {
    fetch: {
      type: Boolean,
      default: true,
    },
  },
  computed: {
    titleQuery() {
      return this.$route.query.title;
    },
  },
  components: {
    DocList,
  },
};

export default DocListView;
</script>
