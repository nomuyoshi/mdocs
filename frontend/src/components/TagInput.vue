<template>
  <b-field>
    <b-taginput
      v-model="selectedTags"
      size="is-small"
      :data="filteredTags"
      autocomplete
      :allow-new="true"
      field="name"
      placeholder="タグ追加"
      @typing="getFilteredTags">
    </b-taginput>
  </b-field>
</template>

<script>
import axios from 'axios';
import NotificationMixin from '@/mixins/NotificationMixin';

const TagInput = {
  data() {
    return {
      tags: [],
      filteredTags: [],
    };
  },
  props: {
    selectedTags: {
      type: Array,
      required: true,
      default: [],
    },
  },
  mounted() {
    axios.get('/tags/')
      .then((response) => {
        this.tags = response.data;
      })
      .catch(() => {
        this.notifyError();
      });
  },
  methods: {
    getFilteredTags(text) {
      const keyword = text.toLowerCase();
      const tags = this.tags.filter(tag => tag.name.toLowerCase().indexOf(keyword) >= 0);
      this.filteredTags = tags;
    },
  },
  mixins: [NotificationMixin],
};

export default TagInput;
</script>
