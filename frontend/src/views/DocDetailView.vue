<template>
  <div class="section">
    <div class="is-pulled-left doc-title">
      <p class="title is-4">{{ doc.title }}</p>
    </div>
    <div class="is-pulled-right action-button">
      <button class="button is-danger is-rounded" type="button" @click="onClickDelete">
        削除
      </button>
    </div>
    <div class="is-pulled-right action-button">
      <router-link
        :to="{ name: 'doc-edit', params: { id: doc.id } }"
        class="button is-light is-rounded"
      >
        編集
      </router-link>
    </div>
    <div class="is-pulled-right action-button">
      <pin :doc="doc" />
    </div>
    <div class="is-clearfix"></div>
    <doc-tags :doc="doc" />
    <hr/>
    <preview :markdown="doc.body"/>
  </div>
</template>

<script>
import axios from 'axios';

import DocTags from '@/components/DocTags.vue';
import Preview from '@/components/Preview.vue';
import Pin from '@/components/Pin.vue';
import NotificationMixin from '@/mixins/NotificationMixin';

const DocDetailView = {
  data() {
    return {
      doc: {
        id: this.$route.params.id,
        title: '',
        body: '',
        tags: [],
        pin: null,
        created_at: '',
        updated_at: '',
      },
    };
  },
  mounted() {
    axios.get(`/docs/${this.$route.params.id}/`)
      .then((response) => {
        this.doc = response.data;
      })
      .catch(() => {
        this.notifyError('データが存在しません');
        this.$router.push('/');
      });
  },
  methods: {
    onClickDelete() {
      // eslint-disable-next-line no-alert
      if (window.confirm('削除します。よろしいですか？')) {
        axios.delete(`/docs/${this.doc.id}/`)
          .then(() => {
            this.notifySuccess('削除成功');
            this.$router.push('/');
          })
          .catch(() => {
            this.notifyError('削除できませんでした。時間をおいて再度お試しください。');
          });
      }
    },
  },
  components: {
    DocTags,
    Preview,
    Pin,
  },
  mixins: [NotificationMixin],
};

export default DocDetailView;
</script>

<style lang="scss" scoped>
.doc-title {
  max-width: 80%;
}
.action-button {
  margin: 0 1rem;
}
</style>
