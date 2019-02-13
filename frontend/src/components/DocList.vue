<template>
  <div class="columns">
    <div class="column is-three-quarters">
      <ul>
        <li v-for="doc in docList" :key="doc.id">
          <section class="section">
            <h1 class="title">{{ doc.title }}</h1>
            <p>summary...</p>
          </section>
        </li>
      </ul>
    </div>
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
