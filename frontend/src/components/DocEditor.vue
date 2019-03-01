<template>
  <div>
    <b-field>
      <b-input v-model="title" placeholder="タイトル" maxlength="100" required></b-input>
    </b-field>
    <hr>
    <div class="columns body-area">
      <div class="column is-half">
        <div class="editor">
          <b-field>
            <b-input
              type="textarea"
              placeholder="本文"
              @input="updateBody"
              :value="body"
              maxlength="10000"
              required
            />
          </b-field>
        </div>
      </div>
      <div class="column is-half">
        <preview :compiled-html="compiledHtml"/>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <button class="button primary is-pulled-right" type="button" @click="onSubmit">
          保存
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import marked from 'marked';
import { debounce } from 'lodash';
import router from '../router';
import Preview from './Preview.vue';
import NotificationMixin from '../mixins/NotificationMixin';

export default {
  data() {
    return {
      id: this.$route.params.id || null,
      title: '',
      body: '',
      errors: {},
    };
  },
  computed: {
    compiledHtml() {
      return marked(this.body, { sanitize: true, breaks: true });
    },
    apiUrl() {
      return this.id ? `/docs/${this.id}/` : '/docs/';
    },
    httpMethod() {
      return this.id ? 'PUT' : 'POST';
    },
  },
  mounted() {
    this.notifySuccess();
    if (!this.id) { return; }

    axios.get(`/docs/${this.id}/`)
      .then((response) => {
        const { title, body } = response.data;
        this.title = title;
        this.body = body;
      })
      .catch(() => {
        this.notifyError('データが存在しません');
        router.push('/');
      });
  },
  methods: {
    // eslint-disable-next-line func-names
    updateBody: debounce(function (value) {
      this.body = value;
    }, 300),
    onSubmit() {
      axios({
        method: this.httpMethod,
        url: this.apiUrl,
        data: {
          title: this.title,
          body: this.body,
        },
      })
        .then(() => {
          router.push('/');
        })
        .catch((error) => {
          this.errors = error.response.data;
          this.notifyError('入力内容を確認してください');
        });
    },
  },
  components: {
    Preview,
  },
  mixins: [NotificationMixin],
};
</script>

<style lang="scss" scoped>
.body-area {
  height: calc(100vh - 200px);
}
</style>
