<template>
  <div class="columns">
    <div class="column is-three-quarters">
      <section class="section">
        <div class="container">
          <div class="level">
            <div class="level-left">
              <div class="level-item">
                <p class="title">{{ title }}</p>
              </div>
              <div class="level-item">
                <router-link :to="{ name: 'doc-edit', params: { id: id } }" class="button">
                  <b-icon pack="fas" icon="edit" type="is-info"></b-icon>
                </router-link>
              </div>
            </div>
            <div class="level-right">
              <div class="level-item">
                <button class="button" type="button" @click="onClickDelete">
                  <b-icon pack="fas" icon="trash-alt" type="is-danger"></b-icon>
                </button>
              </div>
            </div>
          </div>
          <hr/>
          <preview :compiled-html="compiledHtml"/>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import marked from 'marked';

import router from '../router';
import Preview from './Preview.vue';

export default {
  data() {
    return {
      id: this.$route.params.id,
      title: '',
      body: '',
    };
  },
  components: {
    Preview,
  },
  computed: {
    compiledHtml() {
      if (!this.body) { return ''; }
      return marked(this.body, { sanitize: true, breaks: true });
    },
  },
  mounted() {
    axios.get(`/docs/${this.id}/`)
      .then((response) => {
        const { title, body } = response.data;
        this.title = title;
        this.body = body;
      })
      .catch(() => {
        this.$notify({
          group: 'notifications',
          type: 'error',
          title: 'エラー',
          text: 'データが存在しません。',
        });
        router.push('/');
      });
  },
  methods: {
    onClickDelete() {
      axios.delete(`/docs/${this.id}/`)
        .then(() => router.push('/'))
        .catch(() => {
          this.$notify({
            group: 'notifications',
            type: 'error',
            title: 'エラー',
            text: '削除できませんでした。時間をおいて再度お試しください。',
          });
        });
    },
  },
};
</script>
