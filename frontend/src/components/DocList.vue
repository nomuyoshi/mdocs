<template>
  <div>
    <p v-if="isSearchMode"><strong>「{{ this.query.title }}」検索結果</strong></p>
    <p v-if="isTagFilterMode"><strong>「{{ this.query.tag }}」タグで絞り込み中</strong></p>
    <ul>
      <li class="doc-item" v-for="doc in docList" :key="doc.id">
        <section class="section">
          <div class="is-pulled-left is-size-4 has-text-weight-semibold">
            <router-link :to="{ name: 'doc-detail', params: { id: doc.id } }">
              <span class="has-text-grey-dark">{{ doc.title }}</span>
            </router-link>
          </div>
          <div class="is-pulled-right">
            <pin-button :doc="doc" />
          </div>
          <div class="is-clearfix" />
          <doc-tags :doc="doc" />
        </section>
      </li>
    </ul>
    <article class="message" v-if="noData && !isLoading">
      <div class="message-body">
        <div v-if="isSearchMode || isTagFilterMode">
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
    <b-loading :active.sync="isLoading"></b-loading>
  </div>
</template>

<script>
import axios from 'axios';
import DocTags from './DocTags.vue';
import NotificationMixin from '@/mixins/NotificationMixin';
import PinButton from './PinButton.vue';


const DocList = {
  data() {
    return {
      isLoading: false,
      docs: [],
    };
  },
  props: {
    query: {
      type: Object,
    },
  },
  computed: {
    isSearchMode() {
      return !!this.query.title;
    },
    isTagFilterMode() {
      return !!this.query.tag;
    },
    docList() {
      return this.docs;
    },
    noData() {
      return this.docs.length === 0;
    },
  },
  mounted() {
    this.fetchDocs(this.query);
  },
  watch: {
    query(newQuery) {
      this.fetchDocs(newQuery);
    },
  },
  methods: {
    fetchDocs(params = {}) {
      this.isLoading = true;
      axios.get('/docs/', {
        params,
      })
        .then((response) => {
          this.docs = response.data;
        })
        .catch(() => {
          this.notifyError('読み込みに失敗しました。');
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
  },
  components: {
    DocTags,
    PinButton,
  },
  mixins: [NotificationMixin],
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
