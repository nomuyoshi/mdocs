<template>
  <div class="columns">
    <div class="column is-three-quarters">
      <ul>
        <li v-for="doc in docList" :key="doc.id">
          <router-link :to="{ name: 'doc', params: { id: doc.id } }">
            <section class="section">
              <h1 class="title">{{ doc.title }}</h1>
            </section>
          </router-link>
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
