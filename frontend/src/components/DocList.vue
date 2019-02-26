<template>
  <div class="columns">
    <div class="column is-three-quarters">
      <ul>
        <li v-for="doc in docList" :key="doc.id">
          <section class="section">
            <router-link :to="{ name: 'doc', params: { id: doc.id } }">
              <h1 class="title">{{ doc.title }}</h1>
            </router-link>
            <b-taglist>
              <b-tag>作成日: {{ doc.created_at | datetimeFormat }}</b-tag>
              <b-tag>更新日: {{ doc.updated_at | datetimeFormat }}</b-tag>
            </b-taglist>
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
