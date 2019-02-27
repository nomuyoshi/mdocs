<template>
  <div class="columns">
    <div class="column is-three-quarters">
      <section class="section" v-if="doc">
        <div class="container">
          <div class="level">
            <div class="level-left">
              <div class="level-item">
                <p class="title">{{ doc.title }}</p>
              </div>
            </div>
            <div class="level-right">
              <div class="level-item">
                <router-link :to="{ name: 'doc-edit', params: { id: doc.id } }" class="button">
                  <b-icon pack="fas" icon="edit" type="is-info"></b-icon>
                </router-link>
              </div>
            </div>
          </div>
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
