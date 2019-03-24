<template>
  <div class="tag-list">
    <p class="is-size-7 has-text-weight-bold">
      <b-icon icon="tags" size="is-small"></b-icon>
      タグ
    </p>
    <ul>
      <li v-for="tag in tags" :key="tag.id" class="tag-item is-size-7">
        <router-link
          :to="{ name: 'doc-list', query: { tag: tag.name }}"
        >
          {{ tag.name }} ({{ tag.documents_count }})
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
import NotificationMixin from '@/mixins/NotificationMixin';

const TagList = {
  data() {
    return {
      tags: [],
    };
  },
  mounted() {
    axios.get('/tags/')
      .then((response) => {
        this.tags = response.data;
      })
      .catch(() => {
        this.notifyError('タグの取得に失敗しました。時間をおいて再度お試しください。');
      });
  },
  mixins: [NotificationMixin],
};

export default TagList;
</script>

<style lang="scss" scoped>
.tag-list {
  color: white !important;
  height: 85%;
  overflow-y: auto;
  .tag-item {
    padding: .5rem;
    border-bottom: solid 1px #363636;
    a { color: white; }
  }
}
</style>
