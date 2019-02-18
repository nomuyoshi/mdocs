<template>
  <div class="columns">
    <div class="column is-three-quarters">
      <section class="section">
        <div class="container">
          <h1 class="title">{{ doc.title }}</h1>
          <hr/>
          <preview :compiled-html="compiledHtml"/>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import marked from 'marked';
import Preview from './Preview.vue';

export default {
  computed: {
    doc() {
      return this.$store.getters.getDocById(this.$route.params.id);
    },
    compiledHtml() {
      if (!this.doc) { return ''; }
      return marked(this.doc.body, { sanitize: true, breaks: true });
    },
  },
  components: {
    Preview,
  },
};
</script>
