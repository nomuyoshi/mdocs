<template>
  <div>
    <p v-for="doc in docList" :key="doc.id">{{ doc.title }}</p>
  </div>
</template>

<script>
export default {
  computed: {
    docList() {
      return this.$store.state.docs;
    },
  },
  created() {
    this.$store.dispatch('fetchDocs');
  },
};
</script>
