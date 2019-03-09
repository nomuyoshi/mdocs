<template>
  <div>
    <h2 class="is-size-2 margin-bottom20">Myドキュメント</h2>
    <ul v-if="docExists">
      <li class="doc-item" v-for="doc in docList" :key="doc.id">
        <section class="section">
          <router-link :to="{ name: 'doc-detail', params: { id: doc.id } }">
            <h1 class="title">{{ doc.title }}</h1>
          </router-link>
          <doc-tags :doc="doc" />
        </section>
      </li>
    </ul>
    <article class="message is-medium" v-else>
      <div class="message-body">
        <p><strong>mDocはMarkDownで書けるクローズドな自分だけのドキュメント管理ツールです。</strong></p>
        <ul class="margin20">
          <li>・公開するほどではない細かなTips</li>
          <li>・公開できないけど残しておきたいドキュメント</li>
        </ul>
        <p>などを書き溜めて、<strong>ナレッジ</strong>を蓄積していきましょう!!</p>
        <p>早速、<a class="button is-primary" href="/docs/new">作成する</a></p>
      </div>
    </article>
  </div>
</template>

<script>
import DocTags from './common/DocTags.vue';

export default {
  computed: {
    docList() {
      return this.$store.state.docs;
    },
    docExists() {
      return this.$store.state.docs.length > 0;
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
