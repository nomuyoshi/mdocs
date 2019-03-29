<template>
  <div class="section">
    <div class="columns">
      <div class="column is-9">
        <h2 class="is-size-5 margin-bottom20">Myドキュメント</h2>
        <doc-list :query="query" />
      </div>
      <div class="column">
        <ad-sense
          ad-client="ca-pub-4852982764298703"
          ad-slot="8639259692"
          ad-style="display: block"
          ad-format="auto"
        />
      </div>
    </div>
  </div>
</template>

<script>
import DocList from '@/components/DocList.vue';
import AdSense from '@/components/AdSense.vue';

const DocListView = {
  computed: {
    query() {
      return {
        title: this.$route.query.title,
        tag: this.$route.query.tag,
        pin: this.$route.query.pin,
      };
    },
  },
  components: {
    DocList,
    AdSense,
  },
};

export default DocListView;
</script>

<style lang="scss" scoped>
.section {
  padding: 2rem 0 0 0;
}
</style>
