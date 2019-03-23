<template>
  <div class="section">
    <b-field>
      <b-input
        v-model="doc.title"
        placeholder="タイトル"
        required>
      </b-input>
    </b-field>
    <tag-input :selected-tags="doc.tags" />
    <hr>
    <div class="columns body-area">
      <div class="column is-half">
        <b-field>
          <textarea
            id="editor"
            class="textarea has-fixed-size"
            v-model="doc.body"
            placeholder="本文"
            maxlength="10000"
            required
            v-scroll="onScroll"
          ></textarea>
        </b-field>
      </div>
      <div class="column is-half">
        <preview :markdown="doc.body" :inputting="true" :scrollPercents="scrollPercents"/>
      </div>
    </div>
    <button class="button is-primary is-pulled-right" type="button" @click="onSubmit">
      保存
    </button>
  </div>
</template>

<script>
import axios from 'axios';
import { scroll } from '@/directives';
import Preview from '@/components/Preview.vue';
import TagInput from '@/components/TagInput.vue';
import NotificationMixin from '@/mixins/NotificationMixin';

const labelNames = {
  body: '本文',
  title: 'タイトル',
};

const DocEditorView = {
  data() {
    return {
      doc: {
        id: this.$route.params.id || null,
        title: '',
        body: '',
        tags: [],
      },
      scrollPercents: 0,
    };
  },
  computed: {
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
        this.$router.push('/');
      });
  },
  methods: {
    onSubmit() {
      axios({
        method: this.httpMethod,
        url: this.apiUrl,
        data: this.buildSubmitData(),
      })
        .then(() => {
          this.$router.push('/');
        })
        .catch((error) => {
          const errors = error.response.data;
          Object.keys(errors).forEach((key) => {
            const message = `${labelNames[key]}: ${errors[key].join('。')}`;
            this.notifyError(message);
          });
        });
    },
    buildSubmitData() {
      const { title, body } = this.doc;
      // Buefyのtaginputだと新規タグが文字列になってしまうのでオブジェクトに変換
      const tags = this.doc.tags.map((tag) => {
        if (typeof tag === 'string') {
          return { id: null, name: tag };
        }
        return tag;
      });

      return {
        title,
        body,
        tags,
      };
    },
    onScroll(event, el) {
      this.scrollPercents = el.scrollTop / (el.scrollHeight - el.clientHeight);
    },
  },
  components: {
    Preview,
    TagInput,
  },
  directives: { scroll },
  mixins: [NotificationMixin],
};

export default DocEditorView;
</script>

<style lang="scss" scoped>
#editor {
  height: calc(100vh - 250px);
  max-height: calc(100vh - 250px);
}
hr { margin: 5px 0; }
.field { margin-bottom: 0; }
.section { padding-top: 1.5rem; }
.body-area {
  margin-bottom: 0;

  .column {
    padding-bottom: 0;
  }
}
</style>
