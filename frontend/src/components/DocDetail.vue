<template>
  <div class="columns">
    <div class="column">
      <section class="section">
        <div class="level">
          <div class="level-left">
            <div class="level-item">
              <p class="title">{{ doc.title }}</p>
            </div>
            <div class="level-item">
              <router-link :to="{ name: 'doc-edit', params: { id: doc.id } }" class="button">
                <b-icon icon="edit" type="is-info"></b-icon>
              </router-link>
            </div>
          </div>
          <div class="level-right">
            <div class="level-item">
              <button class="button" type="button" @click="onClickDelete">
                <b-icon icon="trash-alt" type="is-danger"></b-icon>
              </button>
            </div>
          </div>
        </div>
        <doc-tags :doc="doc" />
        <hr/>
        <preview :compiled-html="compiledHtml"/>
      </section>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import marked from 'marked';

import router from '../router';
import DocTags from './common/DocTags.vue';
import Preview from './common/Preview.vue';
import NotificationMixin from '../mixins/NotificationMixin';

export default {
  data() {
    return {
      doc: {
        id: this.$route.params.id,
        title: '',
        body: '',
        tags: [],
        created_at: '',
        updated_at: '',
      },
    };
  },
  computed: {
    compiledHtml() {
      if (!this.doc.body) { return ''; }
      return marked(this.doc.body, { sanitize: true, breaks: true });
    },
  },
  mounted() {
    axios.get(`/docs/${this.$route.params.id}/`)
      .then((response) => {
        this.doc = response.data;
      })
      .catch(() => {
        this.notifyError('データが存在しません');
        router.push('/');
      });
  },
  methods: {
    onClickDelete() {
      axios.delete(`/docs/${this.doc.id}/`)
        .then(() => {
          this.notifySuccess('削除成功');
          router.push('/');
        })
        .catch(() => {
          this.notifyError('削除できませんでした。時間をおいて再度お試しください。');
        });
    },
  },
  components: {
    DocTags,
    Preview,
  },
  mixins: [NotificationMixin],
};
</script>
