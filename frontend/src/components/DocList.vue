<template>
  <div>
    <p v-if="isSearchMode"><strong>「{{ this.titleQuery }}」検索結果</strong></p>
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
    fetch: {
      type: Boolean,
      default: true,
    },
    titleQuery: {
      type: String,
    },
  },
  computed: {
    isSearchMode() {
      return !!this.titleQuery;
    },
    docList() {
      return this.$store.state.docs;
    },
    noData() {
      return this.$store.state.docs.length === 0;
    },
  },
  created() {
    if (this.fetch) {
      this.$store.dispatch('fetchDocs', this.titleQuery);
    }
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
}
</style>
