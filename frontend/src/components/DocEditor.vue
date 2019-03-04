<template>
  <div>
    <b-field>
      <b-input v-model="doc.title" placeholder="タイトル" maxlength="100" required></b-input>
    </b-field>
    <tag-input :selected-tags="doc.tags" />
    <hr>
    <div class="columns body-area">
      <div class="column is-half">
        <div class="editor">
          <b-field>
            <b-input
              type="textarea"
              placeholder="本文"
              @input="updateBody"
              :value="doc.body"
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
import Preview from './common/Preview.vue';
import TagInput from './common/TagInput.vue';
import NotificationMixin from '../mixins/NotificationMixin';

export default {
  data() {
    return {
      doc: {
        id: this.$route.params.id || null,
        title: '',
        body: '',
        tags: [],
      },
      errors: {},
    };
  },
  computed: {
    compiledHtml() {
      return marked(this.doc.body, { sanitize: true, breaks: true });
    },
    apiUrl() {
      return this.doc.id ? `/docs/${this.doc.id}/` : '/docs/';
    },
    httpMethod() {
      return this.doc.id ? 'PUT' : 'POST';
    },
  },
  mounted() {
    if (!this.doc.id) { return; }

    axios.get(`/docs/${this.doc.id}/`)
      .then((response) => {
        this.doc = response.data;
      })
      .catch(() => {
        this.notifyError('データが存在しません');
        router.push('/');
      });
  },
  methods: {
    // eslint-disable-next-line func-names
    updateBody: debounce(function (value) {
      this.doc.body = value;
    }, 300),
    onSubmit() {
      const { title, body } = this.doc;

      axios({
        method: this.httpMethod,
        url: this.apiUrl,
        data: {
          title,
          body,
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
    TagInput,
  },
  mixins: [NotificationMixin],
};
</script>

<style lang="scss" scoped>
.body-area {
  height: calc(100vh - 200px);
}
</style>
