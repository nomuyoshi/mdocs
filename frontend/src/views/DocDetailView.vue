<template>
  <div class="section">
    <div class="level">
      <div class="level-left">
        <div class="level-item">
          <p class="title">{{ doc.title }}</p>
        </div>
        <div class="level-item">
          <router-link :to="{ name: 'doc-edit', params: { id: doc.id } }" class="button is-light">
            編集
          </router-link>
        </div>
      </div>
      <div class="level-right">
        <div class="level-item">
          <button class="button is-danger" type="button" @click="onClickDelete">
            削除
          </button>
        </div>
      </div>
    </div>
    <doc-tags :doc="doc" />
    <hr/>
    <preview :markdown="doc.body"/>
  </div>
</template>

<script>
import axios from 'axios';

import DocTags from '@/components/DocTags.vue';
import Preview from '@/components/Preview.vue';
import NotificationMixin from '@/mixins/NotificationMixin';

const DocDetailView = {
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
      axios.delete(`/docs/${this.doc.id}/`)
        .then(() => {
          this.notifySuccess('削除成功');
          this.$router.push('/');
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

export default DocDetailView;
</script>
