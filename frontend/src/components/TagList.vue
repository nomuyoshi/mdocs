<template>
  <nav class="panel">
    <p class="panel-heading is-size-6">
      <b-icon icon="tags" size="is-small"></b-icon>
      タグ一覧
    </p>
    <a class="panel-block" v-for="tag in tags" :key="tag.id">
      {{ tag.name }} ({{ tag.documents_count }})
    </a>
  </nav>
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
