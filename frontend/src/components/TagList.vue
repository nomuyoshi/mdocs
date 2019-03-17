<template>
  <div class="tag-list">
    <p class="is-size-7 has-text-weight-bold">
      <b-icon icon="tags" size="is-small"></b-icon>
      タグ
    </p>
    <ul>
      <li v-for="tag in tags" :key="tag.id" class="tag-item">
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
        console.error('error');
      });
  },
};

export default TagList;
</script>

<style lang="scss" scoped>
.tag-list {
  color: white !important;
  .tag-item {
    padding: .5rem;
    border-bottom: solid 1px #363636;
    a { color: white; }
  }
}
</style>
