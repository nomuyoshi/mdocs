<template>
  <div>
    <p v-if="isSearchMode"><strong>「{{ this.query.title }}」検索結果</strong></p>
    <ul>
      <li class="doc-item" v-for="doc in docList" :key="doc.id">
        <section class="section">
          <router-link :to="{ name: 'doc-detail', params: { id: doc.id } }">
            <p class="is-size-4 has-text-grey-dark has-text-weight-semibold">{{ doc.title }}</p>
          </router-link>
          <doc-tags :doc="doc" />
        </section>
      </li>
    </ul>
    <article class="message" v-if="noData">
      <div class="message-body">
        <div v-if="isSearchMode">
          <p>見つかりませんでした・・・</p>
        </div>
        <div v-else>
          <p><strong>mDocはMarkDownで書けるクローズドな自分だけのドキュメント管理ツールです。</strong></p>
          <ul class="margin20">
            <li>・公開するほどではない細かなTips</li>
            <li>・公開できないけど残しておきたいドキュメント</li>
          </ul>
          <p>などを書き溜めて、<strong>ナレッジ</strong>を蓄積していきましょう!!</p>
          <p>早速、<a class="button is-primary" href="/docs/new">作成する</a></p>
        </div>
      </div>
    </article>
  </div>
</template>

<script>
import DocTags from './DocTags.vue';

const DocList = {
  props: {
    query: {
      type: Object,
    },
  },
  computed: {
    isSearchMode() {
      return this.query.title;
    },
    docList() {
      return this.$store.state.docs;
    },
    noData() {
      return this.$store.state.docs.length === 0;
    },
  },
  mounted() {
    this.$store.dispatch('fetchDocs', this.query);
  },
  watch: {
    query(newQuery) {
      this.$store.dispatch('fetchDocs', newQuery);
    },
  },
  components: {
    DocTags,
  },
};

export default DocList;
</script>

<style lang="scss" scoped>
li.doc-item {
  border-top: 1px solid #B5B5B5;
  &:last-child {
    border-bottom: 1px solid #B5B5B5;
  }
  .section {
    padding: 1.5rem;
  }
}
</style>
